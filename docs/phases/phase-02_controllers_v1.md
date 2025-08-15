---
id: DOC-PHASE-02
title: Phase 02 — Controllers v1 (Baseline)
owner: Reasoning Guild
status: draft
version: 2025.08.0
depends_on: [DOC-PHASE-01, DOC-CORE-CONTROL-PLANE, DOC-CTRL-BUDGETER, DOC-CTRL-MECO, DOC-CTRL-PLANNER, DOC-CTRL-MVR, DOC-CTRL-VERIFIER, DOC-CTRL-TASK-ORCH, DOC-TOOL-REGISTRY]
---

# Phase 02 — Controllers v1 (Baseline)

## Objective
Implement the baseline version of the five-axis controller system with basic functionality, tool registry, MVR preflight, and receipt storage.

## Scope
- Basic Control Plane implementation
- Five-axis controllers (Budgeter, MeCo Gate, Planner, MetaVerifier, VerifierAgent, Task Orchestrator)
- Tool Registry with MVR preflight
- Receipt storage and audit trail
- Demo tools (web_search, calculator, sql_query)

## Inputs
- [DOC-CORE-CONTROL-PLANE](/docs/core/control_plane_spec.md) - Control plane specification
- [DOC-CTRL-BUDGETER](/docs/controllers/budgeter_spec.md) - Budgeter controller specification
- [DOC-CTRL-MECO](/docs/controllers/mecogate_design.md) - MeCo Gate controller specification
- [DOC-CTRL-PLANNER](/docs/controllers/planner_spec.md) - Planner controller specification
- [DOC-CTRL-MVR](/docs/controllers/metaverifier_spec.md) - MetaVerifier controller specification
- [DOC-CTRL-VERIFIER](/docs/controllers/verifieragent_spec.md) - VerifierAgent controller specification
- [DOC-CTRL-TASK-ORCH](/docs/controllers/task_orchestrator_spec.md) - Task Orchestrator specification
- [DOC-TOOL-REGISTRY](/docs/tooling/tool_registry_spec.md) - Tool registry specification

## Dependencies
- Phase 01 completion (contracts and streaming)
- All controller specifications
- Tool registry specification

## Artifacts

### Documentation
- **DOC-CTRL-BUDGETER** — `/docs/controllers/budgeter_spec.md` - Budgeter controller specification
- **DOC-CTRL-MECO** — `/docs/controllers/mecogate_design.md` - MeCo Gate controller specification
- **DOC-CTRL-PLANNER** — `/docs/controllers/planner_spec.md` - Planner controller specification
- **DOC-CTRL-MVR** — `/docs/controllers/metaverifier_spec.md` - MetaVerifier controller specification
- **DOC-CTRL-VERIFIER** — `/docs/controllers/verifieragent_spec.md` - VerifierAgent controller specification
- **DOC-CTRL-TASK-ORCH** — `/docs/controllers/task_orchestrator_spec.md` - Task Orchestrator specification
- **DOC-TOOL-REGISTRY** — `/docs/tooling/tool_registry_spec.md` - Tool registry specification

### Code Structure
```
/packages/controllers/
├── pyproject.toml
├── src/
│   └── axiom25/
│       └── controllers/
│           ├── __init__.py
│           ├── budgeter_v1.py      # Basic budget allocation
│           ├── meco_gate_v1.py     # Simple tool gating
│           ├── planner_v1.py       # Basic planning
│           ├── metaverifier_v1.py  # Basic MVR
│           ├── verifier_v1.py      # Basic verification
│           └── task_orch_v1.py     # Task orchestration
└── tests/
    └── test_controllers_v1.py

/packages/tooling/
├── pyproject.toml
├── src/
│   └── axiom25/
│       └── tooling/
│           ├── __init__.py
│           ├── registry.py         # Tool registry
│           ├── mvr_preflight.py    # MVR preflight
│           ├── receipts.py         # Receipt storage
│           └── demo_tools/         # Demo tools
│               ├── web_search.py
│               ├── calculator.py
│               └── sql_query.py
└── tests/
    └── test_tooling.py

/apps/api/app/
├── control.py                     # Control plane wiring
├── controllers/                   # Controller integration
│   ├── __init__.py
│   └── coordinator.py
└── tooling/                       # Tool integration
    ├── __init__.py
    └── manager.py
```

## Steps

### Step 1: Controller Specifications
**Owner:** Architecture Guild  
**Duration:** 6 hours  
**Deliverables:**
- All controller specifications designed and documented
- Interface definitions and contracts
- Baseline functionality requirements
- Integration patterns defined

**Documents to create:**
- `/docs/controllers/budgeter_spec.md` - Basic budget allocation with fixed limits
- `/docs/controllers/mecogate_design.md` - Simple tool gating based on trust levels
- `/docs/controllers/planner_spec.md` - Basic planning with simple goal decomposition
- `/docs/controllers/metaverifier_spec.md` - Basic MVR with schema validation
- `/docs/controllers/verifieragent_spec.md` - Basic verification with simple checks
- `/docs/controllers/task_orchestrator_spec.md` - Task lifecycle management

### Step 2: Tool Registry Implementation
**Owner:** Platform Eng  
**Duration:** 3 hours  
**Deliverables:**
- Tool registry with CRUD operations
- Tool specification validation
- Trust level management
- Tool discovery and lookup

**Files to create:**
- `packages/tooling/src/axiom25/tooling/registry.py` - Tool registry implementation
- `packages/tooling/tests/test_registry.py` - Registry tests

### Step 3: MVR Preflight Implementation
**Owner:** Platform Eng  
**Duration:** 3 hours  
**Deliverables:**
- MVR preflight procedure
- Schema validation for tools
- Example invocation testing
- Safety checks and validation

**Files to create:**
- `packages/tooling/src/axiom25/tooling/mvr_preflight.py` - MVR preflight implementation
- `packages/tooling/tests/test_mvr_preflight.py` - Preflight tests

### Step 4: Receipt Storage System
**Owner:** Platform Eng  
**Duration:** 2 hours  
**Deliverables:**
- Receipt storage and retrieval
- Audit trail management
- Receipt validation and integrity
- Performance optimization

**Files to create:**
- `packages/tooling/src/axiom25/tooling/receipts.py` - Receipt storage implementation
- `packages/tooling/tests/test_receipts.py` - Receipt tests

### Step 5: Demo Tools Implementation
**Owner:** Platform Eng  
**Duration:** 3 hours  
**Deliverables:**
- Web search tool with API integration
- Calculator tool with safe evaluation
- SQL query tool with database connection
- Tool specifications and documentation

**Files to create:**
- `packages/tooling/src/axiom25/tooling/demo_tools/web_search.py`
- `packages/tooling/src/axiom25/tooling/demo_tools/calculator.py`
- `packages/tooling/src/axiom25/tooling/demo_tools/sql_query.py`

### Step 6: Controller Implementation
**Owner:** Reasoning Guild  
**Duration:** 8 hours  
**Deliverables:**
- All six controllers implemented
- Basic functionality working
- Integration with tool registry
- Error handling and logging

**Files to create:**
- `packages/controllers/src/axiom25/controllers/budgeter_v1.py`
- `packages/controllers/src/axiom25/controllers/meco_gate_v1.py`
- `packages/controllers/src/axiom25/controllers/planner_v1.py`
- `packages/controllers/src/axiom25/controllers/metaverifier_v1.py`
- `packages/controllers/src/axiom25/controllers/verifier_v1.py`
- `packages/controllers/src/axiom25/controllers/task_orch_v1.py`

### Step 7: Control Plane Integration
**Owner:** Platform Eng  
**Duration:** 4 hours  
**Deliverables:**
- Control plane wiring
- Controller coordination
- Event flow management
- API integration

**Files to create:**
- `apps/api/app/control.py` - Control plane main implementation
- `apps/api/app/controllers/coordinator.py` - Controller coordination
- `apps/api/app/tooling/manager.py` - Tool management integration

### Step 8: Integration Testing
**Owner:** Platform Eng  
**Duration:** 3 hours  
**Deliverables:**
- End-to-end controller testing
- Tool registry integration tests
- MVR preflight validation
- Receipt storage verification

**Test scenarios:**
- Untrusted tools blocked without preflight
- Receipts exist for each tool call
- Schema validation works correctly
- Controller coordination functions properly

## Acceptance Criteria

### Controller Implementation
- [ ] All six controllers implemented with basic functionality
- [ ] Controllers integrate with tool registry
- [ ] Error handling and logging implemented
- [ ] Unit tests for all controllers

### Tool Registry
- [ ] Tool registry CRUD operations work
- [ ] Tool specification validation functions
- [ ] Trust level management implemented
- [ ] Tool discovery and lookup working

### MVR Preflight
- [ ] MVR preflight procedure implemented
- [ ] Schema validation for tools works
- [ ] Example invocation testing functional
- [ ] Safety checks and validation active

### Receipt Storage
- [ ] Receipt storage and retrieval working
- [ ] Audit trail management implemented
- [ ] Receipt validation and integrity checks
- [ ] Performance meets requirements

### Demo Tools
- [ ] Web search tool integrated and working
- [ ] Calculator tool safe and functional
- [ ] SQL query tool connected and tested
- [ ] All tools have proper specifications

### Integration
- [ ] Control plane coordinates all controllers
- [ ] Event flow management working
- [ ] API integration functional
- [ ] End-to-end testing passes

## KPIs
- **Controller Coverage:** 100% of planned controllers implemented
- **Tool Safety:** 100% of untrusted tools blocked without preflight
- **Receipt Coverage:** 100% of tool calls generate receipts
- **Test Coverage:** > 85% code coverage for controllers and tooling

## Risks & Mitigations

### Risk: Controller Complexity
- **Mitigation:** Start with simple implementations, evolve complexity
- **Fallback:** Manual coordination if automation fails

### Risk: Tool Security Issues
- **Mitigation:** Strict MVR preflight and sandboxing
- **Fallback:** Disable untrusted tools entirely

### Risk: Performance Bottlenecks
- **Mitigation:** Async processing and caching
- **Fallback:** Synchronous processing with timeouts

### Risk: Integration Complexity
- **Mitigation:** Clear interfaces and contracts
- **Fallback:** Simplified integration with manual coordination

## Rollback Plan
If issues arise:
1. Disable problematic controllers
2. Fall back to manual tool execution
3. Document issues in ADR
4. Simplify approach and retry

## Links
- [DOC-PHASE-01](/docs/phases/phase-01_contracts_streaming.md) - Previous phase
- [DOC-CORE-CONTROL-PLANE](/docs/core/control_plane_spec.md) - Control plane specification
- [DOC-TOOL-REGISTRY](/docs/tooling/tool_registry_spec.md) - Tool registry specification
- [Phase 03](/docs/phases/phase-03_controllers_v2_sota.md) - Next phase

---

## Acceptance & Traceability
- **Acceptance:** All acceptance criteria met, controllers functional, tooling working
- **Traceability:** Phase 03 depends on this phase completion