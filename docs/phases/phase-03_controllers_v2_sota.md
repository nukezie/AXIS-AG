---
id: DOC-PHASE-03
title: Phase 03 — Controllers v2 (TTC, Search-Aware, SVS/MVR v2) + Adapters
owner: Reasoning Guild
status: draft
version: 2025.08.0
depends_on: [DOC-PHASE-02, DOC-CTRL-BUDGETER, DOC-CTRL-PLANNER, DOC-CTRL-MVR, DOC-ADAPT-LANGGRAPH, DOC-ADAPT-OPENAI]
---

# Phase 03 — Controllers v2 (SOTA)

## Objective
Implement state-of-the-art controllers with dynamic TTC (Test-Time Compute), search-aware planning, SVS (Self-Verification Sampling), MVR v2, and engine adapters for LangGraph and OpenAI.

## Scope
- Dynamic TTC with early-stop mechanisms
- Search-aware planning with PRM scoring
- SVS (k=3) with bounded reflection
- MVR v2 with enhanced verification
- LangGraph and OpenAI engine adapters
- Policy bundle for TTC & verification profiles

## Inputs
- [DOC-CTRL-BUDGETER](/docs/controllers/budgeter_spec.md) - Budgeter controller specification
- [DOC-CTRL-PLANNER](/docs/controllers/planner_spec.md) - Planner controller specification
- [DOC-CTRL-MVR](/docs/controllers/metaverifier_spec.md) - MetaVerifier controller specification
- [DOC-ADAPT-LANGGRAPH](/docs/adapters/langgraph_adapter.md) - LangGraph adapter specification
- [DOC-ADAPT-OPENAI](/docs/adapters/openai_adapter.md) - OpenAI adapter specification
- [DOC-POLICY-BUNDLE](/docs/policy_bundle/2025.08-matrix-v3.2.yaml) - Policy bundle specification

## Dependencies
- Phase 02 completion (baseline controllers)
- Controller specifications for v2 enhancements
- Engine adapter specifications

## Artifacts

### Documentation
- **DOC-POLICY-BUNDLE** — `/docs/policy_bundle/2025.08-matrix-v3.2.yaml` - Policy bundle for TTC & verification

### Code Structure
```
/packages/controllers/
├── src/
│   └── axiom25/
│       └── controllers/
│           ├── budgeter_v2.py      # Dynamic TTC with early-stop
│           ├── planner_v2.py       # Search-aware planning
│           ├── metaverifier_v2.py  # Enhanced MVR
│           └── svs_controller.py   # SVS implementation

/packages/adapters/
├── pyproject.toml
├── src/
│   └── axiom25/
│       └── adapters/
│           ├── __init__.py
│           ├── base.py            # Base adapter interface
│           ├── langgraph_adapter.py
│           ├── openai_adapter.py
│           ├── ag2_adapter.py
│           └── local_adapter.py
└── tests/
    └── test_adapters.py

/packages/planning/
├── pyproject.toml
├── src/
│   └── axiom25/
│       └── planning/
│           ├── __init__.py
│           ├── search_node.py     # Search node implementation
│           ├── prm_scorer.py      # Process Reward Model
│           └── graph_of_thought.py # GoT implementation
└── tests/
    └── test_planning.py

/docs/policy_bundle/
└── 2025.08-matrix-v3.2.yaml      # Policy bundle configuration
```

## Steps

### Step 1: Dynamic TTC Implementation
**Owner:** Reasoning Guild  
**Duration:** 4 hours  
**Deliverables:**
- Dynamic budget allocation based on task difficulty
- Early-stop mechanisms for efficiency
- Adaptive depth/width/reflection allocation
- Performance monitoring and adjustment

**Files to create:**
- `packages/controllers/src/axiom25/controllers/budgeter_v2.py` - Dynamic TTC implementation
- `packages/controllers/tests/test_budgeter_v2.py` - TTC tests

### Step 2: Search-Aware Planning
**Owner:** Reasoning Guild  
**Duration:** 6 hours  
**Deliverables:**
- Search node implementation
- PRM (Process Reward Model) scoring
- Graph-of-Thought (GoT) construction
- Branch scoring and selection

**Files to create:**
- `packages/planning/src/axiom25/planning/search_node.py` - Search node implementation
- `packages/planning/src/axiom25/planning/prm_scorer.py` - PRM scoring
- `packages/planning/src/axiom25/planning/graph_of_thought.py` - GoT implementation
- `packages/controllers/src/axiom25/controllers/planner_v2.py` - Search-aware planner

### Step 3: SVS Implementation
**Owner:** Reasoning Guild  
**Duration:** 4 hours  
**Deliverables:**
- SVS (Self-Verification Sampling) with k=3
- Bounded reflection mechanisms
- Candidate selection and verification
- Performance optimization

**Files to create:**
- `packages/controllers/src/axiom25/controllers/svs_controller.py` - SVS implementation
- `packages/controllers/tests/test_svs_controller.py` - SVS tests

### Step 4: MVR v2 Enhancement
**Owner:** Reasoning Guild  
**Duration:** 3 hours  
**Deliverables:**
- Enhanced verification mechanisms
- Auto-repair capabilities
- Reflection integration
- Performance improvements

**Files to create:**
- `packages/controllers/src/axiom25/controllers/metaverifier_v2.py` - Enhanced MVR
- `packages/controllers/tests/test_metaverifier_v2.py` - MVR v2 tests

### Step 5: Engine Adapters
**Owner:** Platform Eng  
**Duration:** 6 hours  
**Deliverables:**
- Base adapter interface
- LangGraph adapter implementation
- OpenAI adapter implementation
- AG2 and Local adapters (basic)

**Files to create:**
- `packages/adapters/src/axiom25/adapters/base.py` - Base adapter interface
- `packages/adapters/src/axiom25/adapters/langgraph_adapter.py` - LangGraph adapter
- `packages/adapters/src/axiom25/adapters/openai_adapter.py` - OpenAI adapter
- `packages/adapters/src/axiom25/adapters/ag2_adapter.py` - AG2 adapter
- `packages/adapters/src/axiom25/adapters/local_adapter.py` - Local adapter

### Step 6: Policy Bundle
**Owner:** Architecture Guild  
**Duration:** 2 hours  
**Deliverables:**
- Policy bundle configuration
- TTC profiles (Tight, Balanced, Max)
- Verification thresholds
- Performance tuning parameters

**Files to create:**
- `/docs/policy_bundle/2025.08-matrix-v3.2.yaml` - Policy bundle configuration

### Step 7: Integration and Testing
**Owner:** Platform Eng  
**Duration:** 4 hours  
**Deliverables:**
- Controller v2 integration
- Adapter integration
- Performance testing
- Regression testing

**Test scenarios:**
- Accuracy@SLA improvement vs v1
- Cost/solve bounded within targets
- Engines produce comparable outcomes
- Policy bundle switching works

## Acceptance Criteria

### Dynamic TTC
- [ ] Dynamic budget allocation based on task difficulty
- [ ] Early-stop mechanisms functional
- [ ] Adaptive allocation working
- [ ] Performance monitoring active

### Search-Aware Planning
- [ ] Search nodes implemented and functional
- [ ] PRM scoring working correctly
- [ ] Graph-of-Thought construction working
- [ ] Branch scoring and selection functional

### SVS Implementation
- [ ] SVS with k=3 working correctly
- [ ] Bounded reflection mechanisms active
- [ ] Candidate selection and verification functional
- [ ] Performance meets requirements

### MVR v2
- [ ] Enhanced verification mechanisms working
- [ ] Auto-repair capabilities functional
- [ ] Reflection integration working
- [ ] Performance improvements achieved

### Engine Adapters
- [ ] Base adapter interface implemented
- [ ] LangGraph adapter working
- [ ] OpenAI adapter working
- [ ] AG2 and Local adapters functional

### Policy Bundle
- [ ] Policy bundle configuration complete
- [ ] TTC profiles working
- [ ] Verification thresholds set
- [ ] Performance tuning parameters configured

### Integration
- [ ] Controller v2 integration complete
- [ ] Adapter integration working
- [ ] Performance testing passed
- [ ] Regression testing successful

## KPIs
- **Accuracy@SLA:** Improvement vs v1 baseline
- **Cost Efficiency:** Bounded cost per solve
- **Engine Compatibility:** Comparable outcomes across engines
- **Performance:** Meets latency and throughput targets

## Risks & Mitigations

### Risk: SOTA Complexity
- **Mitigation:** Incremental implementation with fallbacks
- **Fallback:** Revert to v1 controllers if issues arise

### Risk: Engine Compatibility
- **Mitigation:** Comprehensive adapter testing
- **Fallback:** Focus on primary engines (LangGraph, OpenAI)

### Risk: Performance Degradation
- **Mitigation:** Performance monitoring and optimization
- **Fallback:** Dynamic scaling and resource allocation

### Risk: Policy Bundle Complexity
- **Mitigation:** Clear documentation and testing
- **Fallback:** Default policies with manual override

## Rollback Plan
If issues arise:
1. Revert to v1 controllers
2. Disable problematic SOTA features
3. Document issues in ADR
4. Simplify approach and retry

## Links
- [DOC-PHASE-02](/docs/phases/phase-02_controllers_v1.md) - Previous phase
- [DOC-CTRL-BUDGETER](/docs/controllers/budgeter_spec.md) - Budgeter specification
- [DOC-ADAPT-LANGGRAPH](/docs/adapters/langgraph_adapter.md) - LangGraph adapter
- [Phase 04](/docs/phases/phase-04_ui_operator_v2.md) - Next phase

---

## Acceptance & Traceability
- **Acceptance:** All acceptance criteria met, SOTA features working, adapters functional
- **Traceability:** Phase 04 depends on this phase completion