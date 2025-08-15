---
id: DOC-CORE-ENGINE-ADAPTER
title: Engine Adapter Interface — Swappable Execution Backends
owner: Architecture Guild
status: draft
version: 2025.08.0
depends_on: [DOC-CORE-CONTROL-PLANE]
---

# Engine Adapter Interface — Swappable Execution Backends

## 1) Adapter Overview

The **EngineAdapter** interface provides a unified abstraction layer between the Control Plane and execution engines. This enables **engine agnosticism**—our ideology (five-axis controllers) remains unchanged while execution backends can be swapped based on requirements.

**Core Principle**: All execution engines must implement the same interface, ensuring **functional parity** and **consistent behavior** across different backends.

## 2) Interface Specification

### 2.1 Core Interface

```python
from abc import ABC, abstractmethod
from typing import AsyncIterator, Dict, Any, Optional, Literal
from dataclasses import dataclass

@dataclass
class ExecutionIntent:
    """Intent passed from Control Plane to adapter"""
    step_type: Literal["reasoning", "tool_call", "search", "verification"]
    payload: Dict[str, Any]
    metadata: Dict[str, Any]

@dataclass
class ExecutionResult:
    """Result returned from adapter to Control Plane"""
    success: bool
    output: Any
    cost: Budget
    latency: float
    metadata: Dict[str, Any]
    error: Optional[str] = None

class EngineAdapter(ABC):
    """Abstract interface for all execution engine adapters"""
    
    @abstractmethod
    async def start_run(self, task_spec: TaskSpec, plan: GraphOfThought, policy: Dict[str, Any]) -> str:
        """Initialize a new run and return run_id"""
        pass
    
    @abstractmethod
    async def execute_step(self, run_id: str, intent: ExecutionIntent) -> ExecutionResult:
        """Execute a single step and return result"""
        pass
    
    @abstractmethod
    async def tool_call(self, run_id: str, tool_spec: ToolSpec, args: Dict[str, Any]) -> ExecutionResult:
        """Execute a tool call"""
        pass
    
    @abstractmethod
    async def checkpoint(self, run_id: str, state: Dict[str, Any]) -> None:
        """Save checkpoint for potential resume"""
        pass
    
    @abstractmethod
    async def resume(self, run_id: str) -> AsyncIterator[RunEvent]:
        """Resume execution from checkpoint"""
        pass
    
    @abstractmethod
    async def cancel(self, run_id: str) -> None:
        """Cancel ongoing execution"""
        pass
    
    @abstractmethod
    async def get_status(self, run_id: str) -> RunStatus:
        """Get current run status"""
        pass
```

### 2.2 Adapter Factory

```python
class AdapterFactory:
    """Factory for creating engine adapters"""
    
    @staticmethod
    def create_adapter(engine_type: str, config: Dict[str, Any]) -> EngineAdapter:
        """Create adapter based on engine type"""
        if engine_type == "langgraph":
            return LangGraphAdapter(config)
        elif engine_type == "openai":
            return OpenAIAdapter(config)
        elif engine_type == "ag2":
            return AG2Adapter(config)
        elif engine_type == "local":
            return LocalAdapter(config)
        else:
            raise ValueError(f"Unknown engine type: {engine_type}")
    
    @staticmethod
    def get_supported_engines() -> List[str]:
        """Get list of supported engine types"""
        return ["langgraph", "openai", "ag2", "local"]
```

## 3) Adapter Implementations

### 3.1 LangGraph Adapter

**Capabilities**:
- Graph-native orchestration with checkpoints
- Built-in streaming and persistence
- Rich state management
- Tool integration via LangChain

**Implementation**:
```python
class LangGraphAdapter(EngineAdapter):
    def __init__(self, config: Dict[str, Any]):
        self.graph = self._build_graph()
        self.checkpointer = self._setup_checkpointer()
        self.tool_registry = self._setup_tools()
    
    async def start_run(self, task_spec: TaskSpec, plan: GraphOfThought, policy: Dict[str, Any]) -> str:
        # Convert plan to LangGraph nodes
        nodes = self._convert_plan_to_nodes(plan)
        
        # Create graph with nodes
        graph = self._create_graph(nodes)
        
        # Start execution
        run_id = await self.graph.astart({
            "task_spec": task_spec,
            "plan": plan,
            "policy": policy
        })
        
        return run_id
    
    async def execute_step(self, run_id: str, intent: ExecutionIntent) -> ExecutionResult:
        # Map intent to LangGraph node
        node = self._map_intent_to_node(intent)
        
        # Execute node
        result = await self.graph.ainvoke({
            "run_id": run_id,
            "node": node,
            "intent": intent
        })
        
        return ExecutionResult(
            success=result.get("success", False),
            output=result.get("output"),
            cost=result.get("cost", Budget()),
            latency=result.get("latency", 0.0),
            metadata=result.get("metadata", {})
        )
    
    def _convert_plan_to_nodes(self, plan: GraphOfThought) -> List[Node]:
        """Convert our plan to LangGraph nodes"""
        nodes = []
        for step in plan.steps:
            if step.type == "reasoning":
                nodes.append(ReasoningNode(step))
            elif step.type == "tool_call":
                nodes.append(ToolCallNode(step))
            elif step.type == "search":
                nodes.append(SearchNode(step))
            elif step.type == "verification":
                nodes.append(VerificationNode(step))
        return nodes
```

### 3.2 OpenAI Adapter

**Capabilities**:
- Native web search and computer use
- Built-in function calling
- Multi-agent handoffs
- Streaming responses

**Implementation**:
```python
class OpenAIAdapter(EngineAdapter):
    def __init__(self, config: Dict[str, Any]):
        self.client = OpenAI(config.get("api_key"))
        self.agent_config = config.get("agent_config", {})
    
    async def start_run(self, task_spec: TaskSpec, plan: GraphOfThought, policy: Dict[str, Any]) -> str:
        # Create OpenAI agent with tools
        tools = self._convert_tools_to_openai_format(task_spec.allowed_tools)
        
        # Start agent thread
        thread = await self.client.beta.threads.create()
        run_id = await self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.agent_config["assistant_id"],
            tools=tools
        )
        
        return f"openai_{thread.id}_{run_id}"
    
    async def execute_step(self, run_id: str, intent: ExecutionIntent) -> ExecutionResult:
        # Parse run_id to get thread and run
        thread_id, run_id = self._parse_run_id(run_id)
        
        # Submit step to OpenAI
        if intent.step_type == "tool_call":
            # Use function calling
            result = await self.client.chat.completions.create(
                model=self.agent_config["model"],
                messages=[{"role": "user", "content": intent.payload["prompt"]}],
                tools=intent.payload["tools"],
                tool_choice="auto"
            )
        else:
            # Use regular completion
            result = await self.client.chat.completions.create(
                model=self.agent_config["model"],
                messages=[{"role": "user", "content": intent.payload["prompt"]}]
            )
        
        return ExecutionResult(
            success=True,
            output=result.choices[0].message.content,
            cost=self._calculate_cost(result),
            latency=result.usage.total_time,
            metadata={"model": result.model, "usage": result.usage}
        )
    
    def _convert_tools_to_openai_format(self, tools: List[ToolSpec]) -> List[Dict[str, Any]]:
        """Convert our ToolSpec to OpenAI function format"""
        openai_tools = []
        for tool in tools:
            openai_tools.append({
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.input_schema
                }
            })
        return openai_tools
```

### 3.3 AG2 Adapter

**Capabilities**:
- Multi-agent conversations
- Built-in human-in-loop
- Rich conversation history
- Agent role management

**Implementation**:
```python
class AG2Adapter(EngineAdapter):
    def __init__(self, config: Dict[str, Any]):
        self.agent_configs = config.get("agents", {})
        self.conversation_manager = self._setup_conversation_manager()
    
    async def start_run(self, task_spec: TaskSpec, plan: GraphOfThought, policy: Dict[str, Any]) -> str:
        # Create conversation with agents
        agents = self._create_agents_for_task(task_spec, plan)
        
        # Start conversation
        conversation = await self.conversation_manager.create_conversation(
            agents=agents,
            initial_message=task_spec.goal
        )
        
        return conversation.id
    
    async def execute_step(self, run_id: str, intent: ExecutionIntent) -> ExecutionResult:
        # Get conversation
        conversation = await self.conversation_manager.get_conversation(run_id)
        
        # Execute step based on intent
        if intent.step_type == "reasoning":
            # Add reasoning message
            message = await conversation.add_message(
                agent="reasoner",
                content=intent.payload["prompt"]
            )
        elif intent.step_type == "tool_call":
            # Execute tool via agent
            result = await conversation.execute_tool(
                agent="executor",
                tool_name=intent.payload["tool_name"],
                args=intent.payload["args"]
            )
            message = result
        else:
            # General conversation step
            message = await conversation.continue_conversation()
        
        return ExecutionResult(
            success=message is not None,
            output=message.content if message else None,
            cost=self._calculate_cost(message),
            latency=message.latency if message else 0.0,
            metadata={"agent": message.agent if message else None}
        )
```

### 3.4 Local Adapter

**Capabilities**:
- Offline execution
- Custom model integration
- Full control over execution
- Debugging and development

**Implementation**:
```python
class LocalAdapter(EngineAdapter):
    def __init__(self, config: Dict[str, Any]):
        self.model = self._load_model(config.get("model_path"))
        self.tool_executor = self._setup_tool_executor()
        self.runs: Dict[str, LocalRun] = {}
    
    async def start_run(self, task_spec: TaskSpec, plan: GraphOfThought, policy: Dict[str, Any]) -> str:
        # Create local run
        run_id = str(uuid.uuid4())
        run = LocalRun(
            task_spec=task_spec,
            plan=plan,
            policy=policy,
            model=self.model,
            tool_executor=self.tool_executor
        )
        
        self.runs[run_id] = run
        return run_id
    
    async def execute_step(self, run_id: str, intent: ExecutionIntent) -> ExecutionResult:
        run = self.runs[run_id]
        
        # Execute step locally
        if intent.step_type == "reasoning":
            result = await run.execute_reasoning(intent.payload["prompt"])
        elif intent.step_type == "tool_call":
            result = await run.execute_tool_call(
                intent.payload["tool_name"],
                intent.payload["args"]
            )
        elif intent.step_type == "search":
            result = await run.execute_search(intent.payload["query"])
        else:
            result = await run.execute_generic(intent)
        
        return ExecutionResult(
            success=result.success,
            output=result.output,
            cost=result.cost,
            latency=result.latency,
            metadata=result.metadata
        )
```

## 4) Adapter Compliance

### 4.1 Compliance Tests

```python
class AdapterComplianceSuite:
    """Test suite to ensure adapter compliance"""
    
    @staticmethod
    async def run_compliance_tests(adapter: EngineAdapter) -> ComplianceReport:
        """Run full compliance test suite"""
        report = ComplianceReport()
        
        # Test basic functionality
        await AdapterComplianceSuite._test_basic_functionality(adapter, report)
        
        # Test error handling
        await AdapterComplianceSuite._test_error_handling(adapter, report)
        
        # Test performance characteristics
        await AdapterComplianceSuite._test_performance(adapter, report)
        
        # Test feature parity
        await AdapterComplianceSuite._test_feature_parity(adapter, report)
        
        return report
    
    @staticmethod
    async def _test_basic_functionality(adapter: EngineAdapter, report: ComplianceReport):
        """Test basic adapter functionality"""
        # Test run lifecycle
        task_spec = create_test_task_spec()
        plan = create_test_plan()
        policy = create_test_policy()
        
        run_id = await adapter.start_run(task_spec, plan, policy)
        assert run_id is not None
        
        # Test step execution
        intent = ExecutionIntent(
            step_type="reasoning",
            payload={"prompt": "Test reasoning step"},
            metadata={}
        )
        
        result = await adapter.execute_step(run_id, intent)
        assert result.success
        assert result.output is not None
        
        # Test tool call
        tool_result = await adapter.tool_call(
            run_id,
            create_test_tool_spec(),
            {"arg1": "value1"}
        )
        assert tool_result.success
        
        # Test checkpoint/resume
        await adapter.checkpoint(run_id, {"state": "test"})
        
        events = []
        async for event in adapter.resume(run_id):
            events.append(event)
        
        assert len(events) > 0
```

### 4.2 Feature Parity Matrix

| Feature | LangGraph | OpenAI | AG2 | Local |
|---------|-----------|--------|-----|-------|
| Graph Execution | ✅ Native | ⚠️ Limited | ⚠️ Limited | ✅ Custom |
| Checkpointing | ✅ Native | ❌ None | ⚠️ Basic | ✅ Custom |
| Streaming | ✅ Native | ✅ Native | ✅ Native | ✅ Custom |
| Tool Integration | ✅ LangChain | ✅ Functions | ⚠️ Limited | ✅ Custom |
| Multi-Agent | ⚠️ Basic | ✅ Handoffs | ✅ Native | ✅ Custom |
| Offline Execution | ❌ No | ❌ No | ❌ No | ✅ Yes |
| Cost Control | ⚠️ Basic | ✅ Native | ⚠️ Basic | ✅ Custom |
| Debugging | ⚠️ Basic | ❌ Limited | ⚠️ Basic | ✅ Full |

## 5) Adapter Selection

### 5.1 Selection Criteria

```python
class AdapterSelector:
    """Select appropriate adapter based on requirements"""
    
    @staticmethod
    def select_adapter(requirements: AdapterRequirements) -> str:
        """Select best adapter for requirements"""
        scores = {}
        
        for engine_type in ["langgraph", "openai", "ag2", "local"]:
            score = AdapterSelector._score_adapter(engine_type, requirements)
            scores[engine_type] = score
        
        return max(scores, key=scores.get)
    
    @staticmethod
    def _score_adapter(engine_type: str, requirements: AdapterRequirements) -> float:
        """Score adapter against requirements"""
        score = 0.0
        
        # Feature requirements
        if requirements.graph_execution and engine_type == "langgraph":
            score += 10.0
        if requirements.multi_agent and engine_type in ["openai", "ag2"]:
            score += 8.0
        if requirements.offline and engine_type == "local":
            score += 10.0
        
        # Performance requirements
        if requirements.latency_sensitive and engine_type == "openai":
            score += 5.0
        if requirements.cost_sensitive and engine_type == "local":
            score += 5.0
        
        # Tool requirements
        if requirements.rich_tools and engine_type in ["langgraph", "openai"]:
            score += 3.0
        
        return score
```

### 5.2 Auto-Selection Logic

```python
class AutoAdapterSelector:
    """Automatically select adapter based on task characteristics"""
    
    @staticmethod
    def select_for_task(task_spec: TaskSpec) -> str:
        """Select adapter based on task characteristics"""
        
        # Check for specific backend preference
        if task_spec.backend_pref != "auto":
            return task_spec.backend_pref
        
        # Analyze task requirements
        if task_spec.goal.lower().contains("research") or "search" in task_spec.allowed_tools:
            return "openai"  # Best for web search
        
        if len(task_spec.allowed_tools) > 5:
            return "langgraph"  # Best for complex tool orchestration
        
        if "multi_agent" in task_spec.goal.lower():
            return "ag2"  # Best for multi-agent scenarios
        
        if task_spec.sla_budget.max_cost < 0.01:
            return "local"  # Best for cost-sensitive tasks
        
        # Default to LangGraph for general cases
        return "langgraph"
```

## 6) Performance & Monitoring

### 6.1 Adapter Metrics

```python
class AdapterMetrics:
    """Metrics collection for adapters"""
    
    def __init__(self):
        self.metrics = {
            "execution_time": [],
            "success_rate": [],
            "cost_per_run": [],
            "error_rate": [],
            "feature_usage": {}
        }
    
    async def record_execution(self, adapter_type: str, execution_time: float, 
                             success: bool, cost: float, error: Optional[str] = None):
        """Record execution metrics"""
        self.metrics["execution_time"].append(execution_time)
        self.metrics["success_rate"].append(1.0 if success else 0.0)
        self.metrics["cost_per_run"].append(cost)
        
        if error:
            self.metrics["error_rate"].append(1.0)
        else:
            self.metrics["error_rate"].append(0.0)
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Generate performance report"""
        return {
            "avg_execution_time": np.mean(self.metrics["execution_time"]),
            "success_rate": np.mean(self.metrics["success_rate"]),
            "avg_cost": np.mean(self.metrics["cost_per_run"]),
            "error_rate": np.mean(self.metrics["error_rate"])
        }
```

## Acceptance & Traceability

**Acceptance**
- All adapters implement the same interface with consistent behavior
- Compliance tests pass for all adapter implementations
- Feature parity matrix shows clear tradeoffs
- Auto-selection logic chooses appropriate adapters

**Traceability**
- This interface enables: DOC-ADAPT-LANGGRAPH, DOC-ADAPT-OPENAI, DOC-ADAPT-AG2, DOC-ADAPT-LOCAL
- Integration with: DOC-CORE-CONTROL-PLANE
- Performance monitoring connects to: DOC-OPS-OBS
- Compliance testing references: DOC-EVAL-CICD