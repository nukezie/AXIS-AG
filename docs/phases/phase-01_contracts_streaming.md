---
id: DOC-PHASE-01
title: Phase 01 — Contracts & Streaming
owner: Platform Eng
status: draft
version: 2025.08.0
depends_on: [DOC-PHASE-00, DOC-CORE-ARCH-OVERVIEW, DOC-API-EVENT-MODEL]
---

# Phase 01 — Contracts & Streaming

## Objective
Implement the foundational data contracts, API event model, and streaming infrastructure that enables real-time communication between the Control Plane and UI.

## Scope
- Pydantic/TypeScript contract schemas
- FastAPI Server-Sent Events (SSE) implementation
- React SSE client for real-time UI updates
- Schema validation and versioning
- Event streaming infrastructure

## Inputs
- [DOC-CORE-ARCH-OVERVIEW](/docs/core/architecture_overview.md) - System architecture
- [DOC-API-EVENT-MODEL](/docs/api/event_model.md) - Event streaming specification
- [DOC-CONTRACTS-TASKSPEC](/docs/contracts/taskspec_schema.md) - Task specification schema
- [DOC-CONTRACTS-BUDGET](/docs/contracts/budget_schema.md) - Budget allocation schema
- [DOC-CONTRACTS-VERIFY](/docs/contracts/verifycontract_schema.md) - Verification contract schema
- [DOC-CONTRACTS-TOOLSPEC](/docs/contracts/toolspec_schema.md) - Tool specification schema
- [DOC-CONTRACTS-RUNEVENT](/docs/contracts/runevent_schema.md) - Run event schema

## Dependencies
- Phase 00 completion (repository structure, CI pipeline)
- Core architecture documentation
- API event model specification

## Artifacts

### Documentation
- **DOC-CONTRACTS-TASKSPEC** — `/docs/contracts/taskspec_schema.md` - Task specification contract
- **DOC-CONTRACTS-BUDGET** — `/docs/contracts/budget_schema.md` - Budget allocation contract
- **DOC-CONTRACTS-VERIFY** — `/docs/contracts/verifycontract_schema.md` - Verification contract
- **DOC-CONTRACTS-TOOLSPEC** — `/docs/contracts/toolspec_schema.md` - Tool specification contract
- **DOC-CONTRACTS-RUNEVENT** — `/docs/contracts/runevent_schema.md` - Run event contract
- **DOC-API-EVENT-MODEL** — `/docs/api/event_model.md` - Event streaming model

### Code Structure
```
/packages/contracts/
├── pyproject.toml
├── src/
│   └── axiom25/
│       └── contracts/
│           ├── __init__.py
│           ├── taskspec.py      # TaskSpec Pydantic model
│           ├── budget.py        # Budget Pydantic model
│           ├── verify.py        # VerifyContract Pydantic model
│           ├── toolspec.py      # ToolSpec Pydantic model
│           └── runevent.py      # RunEvent Pydantic model
└── tests/
    └── test_contracts.py

/apps/ui/src/
├── types/
│   ├── taskspec.ts             # TaskSpec TypeScript interface
│   ├── budget.ts               # Budget TypeScript interface
│   ├── verify.ts               # VerifyContract TypeScript interface
│   ├── toolspec.ts             # ToolSpec TypeScript interface
│   └── runevent.ts             # RunEvent TypeScript interface
└── features/
    └── console/
        ├── RunConsole.tsx      # SSE client component
        ├── useRunStream.ts     # SSE hook
        └── types.ts            # Console-specific types

/apps/api/app/
├── main.py                     # FastAPI app with SSE endpoints
├── contracts/                  # Contract validation
│   ├── __init__.py
│   └── validators.py
└── streaming/
    ├── __init__.py
    ├── sse.py                  # SSE implementation
    └── event_bus.py            # Event bus for streaming
```

## Steps

### Step 1: Contract Schema Design
**Owner:** Architecture Guild  
**Duration:** 4 hours  
**Deliverables:**
- All contract schemas designed and documented
- Pydantic models implemented
- TypeScript interfaces generated
- Schema validation rules defined

**Documents to create:**
- `/docs/contracts/taskspec_schema.md` - Task specification with goal, inputs, tools, budget
- `/docs/contracts/budget_schema.md` - Token, time, width, reflection limits
- `/docs/contracts/verifycontract_schema.md` - Assertions, scorers, refusal thresholds
- `/docs/contracts/toolspec_schema.md` - Tool definition with auth and trust levels
- `/docs/contracts/runevent_schema.md` - Streamed events (token, thought, tool, verdict)

### Step 2: Contract Implementation
**Owner:** Platform Eng  
**Duration:** 3 hours  
**Deliverables:**
- Pydantic models in `/packages/contracts/`
- TypeScript interfaces in `/apps/ui/src/types/`
- Schema validation and serialization
- Unit tests for all contracts

**Commands:**
```bash
# Create contracts package
cd packages/contracts
uv init
uv add pydantic pydantic-settings

# Generate TypeScript types
uv add datamodel-code-generator
datamodel-codegen --input contracts.py --output ../../apps/ui/src/types/
```

### Step 3: API Event Model Design
**Owner:** Architecture Guild  
**Duration:** 2 hours  
**Deliverables:**
- Event streaming specification
- SSE endpoint design
- Event ordering and delivery guarantees
- Error handling and recovery

**Document to create:**
- `/docs/api/event_model.md` - Event streaming semantics and API design

### Step 4: FastAPI SSE Implementation
**Owner:** Platform Eng  
**Duration:** 3 hours  
**Deliverables:**
- FastAPI SSE endpoints
- Event bus implementation
- Contract validation middleware
- Error handling and logging

**Files to create:**
- `apps/api/app/main.py` - FastAPI app with `/runs` and `/runs/{run_id}/stream` endpoints
- `apps/api/app/streaming/sse.py` - SSE implementation with proper headers
- `apps/api/app/streaming/event_bus.py` - Event bus for managing streams

### Step 5: React SSE Client
**Owner:** UX Eng  
**Duration:** 3 hours  
**Deliverables:**
- React SSE client component
- Custom hook for event streaming
- Real-time UI updates
- Error handling and reconnection

**Files to create:**
- `apps/ui/src/features/console/RunConsole.tsx` - Main console component
- `apps/ui/src/features/console/useRunStream.ts` - SSE hook with reconnection
- `apps/ui/src/features/console/types.ts` - Console-specific types

### Step 6: Integration Testing
**Owner:** Platform Eng  
**Duration:** 2 hours  
**Deliverables:**
- End-to-end contract validation
- SSE streaming tests
- Schema versioning tests
- Performance benchmarks

**Test scenarios:**
- POST `/runs` with valid TaskSpec returns run_id
- GET `/runs/{run_id}/stream` returns SSE stream
- UI receives and displays events in real-time
- Invalid contracts rejected with proper errors

## Acceptance Criteria

### Contract Schemas
- [ ] All 5 contract schemas documented and implemented
- [ ] Pydantic models validate correctly
- [ ] TypeScript interfaces match Pydantic models
- [ ] Schema versioning and migration plan in place

### API Implementation
- [ ] POST `/runs` accepts TaskSpec and returns run_id
- [ ] GET `/runs/{run_id}/stream` returns SSE stream
- [ ] Contract validation middleware rejects invalid requests
- [ ] Error responses follow consistent format

### Streaming Infrastructure
- [ ] SSE implementation handles multiple concurrent streams
- [ ] Event bus manages stream lifecycle
- [ ] Proper error handling and recovery
- [ ] Performance meets latency requirements (< 100ms)

### UI Integration
- [ ] React SSE client connects and receives events
- [ ] Real-time updates display correctly
- [ ] Error handling and reconnection work
- [ ] Console UI is responsive and user-friendly

### Testing & Validation
- [ ] All contracts have unit tests
- [ ] End-to-end streaming tests pass
- [ ] Schema validation in CI pipeline
- [ ] Performance benchmarks meet targets

## KPIs
- **Contract Validation:** 100% of requests validated against schemas
- **Streaming Latency:** < 100ms from event generation to UI display
- **Schema Coverage:** 100% of planned contracts implemented
- **Test Coverage:** > 90% code coverage for contracts and streaming

## Risks & Mitigations

### Risk: Schema Evolution Complexity
- **Mitigation:** Versioned schemas with migration paths
- **Fallback:** Backward compatibility for one version

### Risk: SSE Performance Issues
- **Mitigation:** Connection pooling and event batching
- **Fallback:** Polling fallback for high-latency scenarios

### Risk: TypeScript/Python Sync Drift
- **Mitigation:** Automated code generation from Pydantic
- **Fallback:** Manual sync with validation tests

### Risk: Streaming Reliability
- **Mitigation:** Reconnection logic and error recovery
- **Fallback:** Event persistence and replay capability

## Rollback Plan
If issues arise:
1. Revert to previous contract versions
2. Disable streaming, fall back to polling
3. Document issues in ADR
4. Simplify approach and retry

## Links
- [DOC-PHASE-00](/docs/phases/phase-00_bootstrap.md) - Previous phase
- [DOC-CORE-ARCH-OVERVIEW](/docs/core/architecture_overview.md) - System architecture
- [DOC-API-EVENT-MODEL](/docs/api/event_model.md) - Event streaming model
- [Phase 02](/docs/phases/phase-02_controllers_v1.md) - Next phase

---

## Acceptance & Traceability
- **Acceptance:** All acceptance criteria met, streaming working end-to-end, contracts validated
- **Traceability:** Phase 02 depends on this phase completion