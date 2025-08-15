# AXIOM-25 Matrix AI Agent Architecture

A **multi-axis, engine-agnostic agent architecture** with budgeted reasoning, verified tooling, and enterprise-grade observability.

## 🎯 Vision

AXIOM-25 Matrix delivers a **graph-native, budget-aware, self-verifying** agent runtime that separates ideology from execution engines. Built on 2025 arXiv research for Test-Time Compute (TTC), search-aware planning, and unified verification.

## 🏗️ Architecture Overview

### Five-Axis Doctrine
- **Reasoning** × **Assignment** × **Planning** × **Production** × **Tasks**
- Each axis operates independently but coordinates through the Control Plane
- Engine-agnostic design allows swapping between LangGraph, OpenAI Agents, AG2, Local

### Key Features
- **Budgeted Reasoning (TTC):** Adaptive depth/width/reflection/time allocation
- **Verified Tooling:** Meta-Verification & Reflection (MVR) for all tool calls  
- **Search Integration:** RL-with-search policies treat search as first-class actions
- **Receipts & Telemetry:** Complete audit trail for all operations
- **Multi-Agent Safety:** TRiSM frameworks and MultiAgentBench evaluation

## 📚 Documentation

### Quick Start
- [**Table of Contents**](docs/TOC.md) - Master index of all documentation
- [**Glossary**](docs/GLOSSARY.md) - Terminology and definitions
- [**Agent Handover**](agent-handover.md) - Complete project context

### Development Phases
- [**Phase Manifest**](docs/phases/_manifest.yaml) - Execution order and dependencies
- [**Cursor Tasks**](cursor-tasks.json) - Development orchestration

### Next Steps
1. Generate core architecture documents
2. Execute Phase 00 (Bootstrap & CI)
3. Build contracts and streaming foundation
4. Implement five-axis controllers

## 🛠️ Technical Stack

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

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ and pnpm
- Python 3.11+ and uv
- Docker (for local development)

### Development Setup
```bash
# Clone repository
git clone <repository-url>
cd axiom-25-matrix

# Install dependencies
pnpm install
uv sync

# Start development
pnpm dev
```

## 📋 Development Status

### Completed ✅
- [x] Documentation structure and conventions
- [x] Master Table of Contents (DOC-META-TOC)
- [x] Glossary and taxonomy (DOC-META-GLOSSARY)
- [x] Phase manifest and dependencies
- [x] Cursor development orchestration
- [x] Agent handover documentation

### In Progress 🔄
- [ ] Core architecture documents (DOC-CORE-*)
- [ ] Contract schemas (DOC-CONTRACTS-*)
- [ ] Controller specifications (DOC-CTRL-*)

### Planned 📅
- [ ] Phase 00: Bootstrap & CI
- [ ] Phase 01: Contracts & Streaming
- [ ] Phase 02: Controllers v1 (Baseline)
- [ ] Phase 03: Controllers v2 (SOTA)
- [ ] Phase 04: UI v2 (Five-Axis Control)
- [ ] Phase 05: Evaluation & Governance
- [ ] Phase 06: Security & TRiSM
- [ ] Phase 07: Deployment & SRE

## 🤝 Contributing

### Development Workflow
1. **Read the handover** - [agent-handover.md](agent-handover.md)
2. **Follow the phase sequence** - [cursor-tasks.json](cursor-tasks.json)
3. **Maintain Doc ID conventions** - [docs/TOC.md](docs/TOC.md)
4. **Update documentation** - Keep cross-links consistent

### Key Conventions
- **Doc IDs:** Upper-snake format (e.g., `DOC-CORE-ARCH-OVERVIEW`)
- **Front-matter:** Standardized metadata with dependencies
- **Cross-linking:** Always by Doc ID + absolute path
- **Acceptance blocks:** Every doc ends with tests and traceability

## 📖 Research Foundation

Based on 2025 arXiv research:
- **TTC Methods:** Plan-and-Budget, length control (LCPO/LAPO), adaptive reasoning
- **Search Integration:** RL-with-search policies, search as first-class action  
- **Verification:** SVS (Self-Verification Sampling), unified verification agents
- **Tool Reliability:** MVR (Meta-Verification & Reflection), auto-repair loops
- **Multi-Agent Safety:** MultiAgentBench, TRiSM frameworks

## 📄 License

[License information to be added]

---

**AXIOM-25 Matrix** - Building the future of AI agent orchestration, one axis at a time.