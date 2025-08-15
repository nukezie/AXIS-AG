# Agent Handover Document — AXIOM-25 Matrix AI Agent Architecture

## Project Overview

**Project Name:** AXIOM-25 Matrix AI Agent Architecture  
**Current Status:** Documentation Foundation Phase  
**Architecture Version:** v3.1  
**Last Updated:** 2025.08.0  

## What Has Been Accomplished

### 1. Documentation Structure Established
- ✅ **Master Table of Contents** (`/docs/TOC.md`) - Complete index of all required documents
- ✅ **Glossary & Taxonomy** (`/docs/GLOSSARY.md`) - Canonical definitions and terminology
- ✅ **Phase Manifest** (`/docs/phases/_manifest.yaml`) - Execution order and dependencies
- ✅ **Cursor Tasks** (`cursor-tasks.json`) - Development orchestration for Cursor

### 2. Architecture Foundation
The AXIOM-25 Matrix is a **multi-axis, engine-agnostic agent architecture** with these key characteristics:

- **Five-Axis Doctrine:** Reasoning × Assignment × Planning × Production × Tasks
- **Budgeted Reasoning (TTC):** Adaptive depth/width/reflection/time allocation
- **Verified Tooling:** Meta-Verification & Reflection (MVR) for all tool calls
- **Engine Agnosticism:** Swappable backends via EngineAdapter interface
- **Receipts & Telemetry:** Complete audit trail for all operations

### 3. Document Organization
All documentation follows strict conventions:
- **Doc IDs:** Upper-snake format (e.g., `DOC-CORE-ARCH-OVERVIEW`)
- **Front-matter:** Standardized metadata with dependencies
- **Cross-linking:** Always by Doc ID + absolute path
- **Acceptance blocks:** Every doc ends with tests and traceability

## Current State

### Completed Documents
1. **DOC-META-TOC** → `/docs/TOC.md` - Master index
2. **DOC-META-GLOSSARY** → `/docs/GLOSSARY.md` - Terminology
3. **Phase Manifest** → `/docs/phases/_manifest.yaml` - Execution plan
4. **Cursor Tasks** → `cursor-tasks.json` - Development orchestration

### Next Priority Documents (In Order)
1. **DOC-CORE-ARCH-OVERVIEW** → `/docs/core/architecture_overview.md`
2. **DOC-CORE-FIVE-AXIS** → `/docs/core/five_axis_doctrine.md`
3. **DOC-CORE-CONTROL-PLANE** → `/docs/core/control_plane_spec.md`
4. **DOC-CORE-ENGINE-ADAPTER** → `/docs/core/engine_adapter_interface.md`

## Development Phases

### Phase 00: Bootstrap & CI
- **Status:** Ready to start
- **Owner:** Platform Eng
- **Dependencies:** None (root phase)
- **Deliverables:** Repo structure, CI pipeline, ADR-0001

### Phase 01: Contracts & Streaming
- **Status:** Waiting for core docs
- **Owner:** Platform Eng
- **Dependencies:** DOC-CORE-ARCH-OVERVIEW, DOC-API-EVENT-MODEL
- **Deliverables:** Pydantic/TS contracts, FastAPI SSE, UI console

### Phase 02: Controllers v1 (Baseline)
- **Status:** Waiting for core docs + contracts
- **Owner:** Reasoning Guild
- **Dependencies:** All controller specs + tooling
- **Deliverables:** Basic Control Plane, Tool Registry, MVR preflight

### Phase 03: Controllers v2 (SOTA)
- **Status:** Waiting for v1 completion
- **Owner:** Reasoning Guild
- **Dependencies:** v1 controllers + adapter specs
- **Deliverables:** Dynamic TTC, search-aware planning, SVS/MVR v2, adapters

### Phase 04: UI v2 (Five-Axis Control)
- **Status:** Waiting for controllers v2
- **Owner:** UX Eng
- **Dependencies:** All UI specs + event model
- **Deliverables:** Matrix Dashboard, Graph View, Budget/Verifier Panels

### Phase 05: Evaluation & Governance
- **Status:** Waiting for UI v2
- **Owner:** MLOps
- **Dependencies:** Eval specs + verification
- **Deliverables:** Regression pack, CI gates, KPI dashboards

### Phase 06: Security & TRiSM
- **Status:** Waiting for eval completion
- **Owner:** Security Eng
- **Dependencies:** Security specs + tooling
- **Deliverables:** Redaction, sandboxing, incident mode

### Phase 07: Deployment & SRE
- **Status:** Waiting for security completion
- **Owner:** SRE
- **Dependencies:** Ops specs
- **Deliverables:** Containers, k8s, observability, release strategy

## Key Architectural Decisions

### 1. Engine Agnosticism
- **Decision:** Keep ideology separate from execution engines
- **Rationale:** Allows swapping between LangGraph, OpenAI Agents, AG2, Local without touching domain logic
- **Implementation:** EngineAdapter interface with thin adapters

### 2. Five-Axis Control
- **Decision:** Split reasoning into five coordinated controllers
- **Rationale:** Each axis has distinct responsibilities and can be optimized independently
- **Implementation:** Budgeter, MeCo Gate, Planner, MetaVerifier, VerifierAgent, Task Orchestrator

### 3. Budgeted Reasoning (TTC)
- **Decision:** Make compute allocation explicit and adaptive
- **Rationale:** Prevents runaway costs and allows SLA enforcement
- **Implementation:** Dynamic depth/width/reflection/time based on task difficulty

### 4. Verified Tooling
- **Decision:** Wrap all tool calls with pre/post verification
- **Rationale:** Improves reliability and provides audit trail
- **Implementation:** MVR (Meta-Verification & Reflection) with auto-repair

## Technical Stack

### Backend
- **Framework:** FastAPI (Python)
- **Orchestration:** LangGraph (primary), OpenAI Agents, AG2 (adapters)
- **Memory:** Redis (episodic), Postgres + pgvector (semantic)
- **Observability:** OpenTelemetry, Prometheus, Grafana

### Frontend
- **Framework:** React (v0.dev → Next.js)
- **UI Library:** TailwindCSS + shadcn/ui
- **State:** Zustand + @tanstack/react-query
- **Visualization:** react-flow-renderer (graph), recharts (metrics)

### Development
- **Package Manager:** pnpm (workspaces)
- **Python:** uv + poetry
- **CI/CD:** GitHub Actions
- **Documentation:** Markdown with front-matter

## Critical Dependencies

### Research Foundation (2025 arXiv)
- **TTC Methods:** Plan-and-Budget, length control (LCPO/LAPO), adaptive reasoning
- **Search Integration:** RL-with-search policies, search as first-class action
- **Verification:** SVS (Self-Verification Sampling), unified verification agents
- **Tool Reliability:** MVR (Meta-Verification & Reflection), auto-repair loops
- **Multi-Agent Safety:** MultiAgentBench, TRiSM frameworks

### External Platforms
- **LangGraph:** Primary orchestration engine
- **OpenAI Agents/Responses:** Execution backend with web search/computer use
- **v0.dev:** UI scaffolding and generation
- **Cursor:** IDE integration and development workflow

## What Needs to Be Done Next

### Immediate (Next Session)
1. **Generate DOC-CORE-ARCH-OVERVIEW** - System overview and high-level architecture
2. **Generate DOC-CORE-FIVE-AXIS** - Five-axis doctrine and operational rules
3. **Generate DOC-CORE-CONTROL-PLANE** - Control plane specification
4. **Generate DOC-CORE-ENGINE-ADAPTER** - Adapter interface specification

### Short Term (Next Week)
1. **Generate all contract schemas** (DOC-CONTRACTS-*)
2. **Generate all controller specs** (DOC-CTRL-*)
3. **Generate all UI specs** (DOC-UI-*)
4. **Generate all API specs** (DOC-API-*)

### Medium Term (Next Month)
1. **Execute Phase 00** - Bootstrap repository and CI
2. **Execute Phase 01** - Implement contracts and streaming
3. **Execute Phase 02** - Build baseline controllers
4. **Execute Phase 03** - Add SOTA methods and adapters

## Risk Areas & Mitigations

### 1. Documentation Complexity
- **Risk:** Too many documents, hard to navigate
- **Mitigation:** Strict Doc ID system, cross-linking, TOC as single source of truth

### 2. Phase Dependencies
- **Risk:** Circular dependencies blocking progress
- **Mitigation:** Clear dependency graph in manifest, parallel doc generation

### 3. Architecture Drift
- **Risk:** Implementation diverges from documentation
- **Mitigation:** ADRs for decisions, acceptance tests in every phase

### 4. Research Integration
- **Risk:** 2025 methods not properly encoded
- **Mitigation:** Explicit citations, policy bundles for thresholds

## Success Criteria

### Phase 00 Success
- [ ] Monorepo structure established
- [ ] CI pipeline green
- [ ] All core docs generated
- [ ] ADR-0001 written

### Phase 01 Success
- [ ] Contracts implemented (Pydantic/TS)
- [ ] SSE streaming working
- [ ] UI console displaying events
- [ ] Schema validation in CI

### Phase 02 Success
- [ ] Control Plane wired
- [ ] Tool Registry functional
- [ ] MVR preflight working
- [ ] Receipts stored

### Overall Success
- [ ] All 8 phases completed
- [ ] Architecture matches documentation
- [ ] KPIs meet targets
- [ ] Production deployment ready

## Contact & Context

### Key Decisions Made
1. **Repository Structure:** Monorepo with `/apps`, `/packages`, `/docs`, `/infrastructure`
2. **Documentation Strategy:** Doc ID system with cross-linking
3. **Development Approach:** Phase-based with explicit dependencies
4. **Architecture Philosophy:** Engine-agnostic with ideology-first design

### Research Context
- Based on 2025 arXiv papers for TTC, search integration, verification
- Incorporates lessons from OpenAI Agents, LangGraph, v0.dev, Cursor
- Designed for enterprise-grade reliability and observability

### Next Agent Instructions
1. **Read this document completely** - Understand the full context
2. **Review `/docs/TOC.md`** - Understand the document structure
3. **Review `/docs/GLOSSARY.md`** - Understand terminology
4. **Review `cursor-tasks.json`** - Understand development sequence
5. **Start with DOC-CORE-ARCH-OVERVIEW** - Generate the first core document
6. **Follow the phase sequence** - Don't skip dependencies
7. **Maintain Doc ID conventions** - Keep cross-linking consistent
8. **Update this handover** - Add your progress and decisions

## Files to Reference

### Core Documentation
- `/docs/TOC.md` - Master index
- `/docs/GLOSSARY.md` - Terminology
- `/docs/phases/_manifest.yaml` - Phase dependencies
- `cursor-tasks.json` - Development orchestration

### Architecture Foundation
- Chat log analysis (provided in original request)
- 2025 arXiv research papers (cited in chat)
- Platform analysis (OpenAI, LangGraph, v0.dev, Cursor)

### Next Steps
1. Generate DOC-CORE-ARCH-OVERVIEW
2. Generate DOC-CORE-FIVE-AXIS  
3. Generate DOC-CORE-CONTROL-PLANE
4. Generate DOC-CORE-ENGINE-ADAPTER
5. Begin Phase 00 execution

---

**Handover Complete** - The next agent has all necessary context to continue development of the AXIOM-25 Matrix AI Agent Architecture.