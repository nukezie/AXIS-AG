---
id: DOC-PHASE-00
title: Phase 00 — Bootstrap & CI
owner: Platform Eng
status: draft
version: 2025.08.0
depends_on: [DOC-META-TOC, DOC-META-GLOSSARY]
---

# Phase 00 — Bootstrap & CI

## Objective
Establish the foundational repository structure, development environment, and CI/CD pipeline for the AXIOM-25 Matrix AI Agent Architecture.

## Scope
- Repository monorepo structure
- Development environment setup
- CI/CD pipeline configuration
- Core documentation foundation
- Architecture Decision Records (ADRs)

## Inputs
- [DOC-META-TOC](/docs/TOC.md) - Master documentation index
- [DOC-META-GLOSSARY](/docs/GLOSSARY.md) - Terminology and definitions
- [cursor-tasks.json](/cursor-tasks.json) - Development orchestration

## Dependencies
- None (root phase)

## Artifacts

### Documentation
- **DOC-ADR-0001** — `/docs/ADR/0001-repo-architecture.md` - Repository architecture decisions
- **DOC-RUNBOOK-LOCAL** — `/docs/runbooks/local_dev.md` - Local development setup guide

### Code Structure
```
/
├── apps/
│   ├── api/                    # FastAPI backend
│   │   ├── app/
│   │   │   ├── main.py         # FastAPI application
│   │   │   ├── control.py      # Control plane wiring
│   │   │   └── security/       # Security modules
│   │   ├── tests/
│   │   ├── pyproject.toml
│   │   └── Dockerfile
│   └── ui/                     # React frontend
│       ├── src/
│       │   ├── features/
│       │   │   ├── console/    # Run console
│       │   │   ├── matrix/     # Matrix dashboard
│       │   │   ├── graph/      # Graph view
│       │   │   ├── budget/     # Budget panel
│       │   │   ├── verifier/   # Verifier panel
│       │   │   └── tools/      # Tool catalog
│       │   └── components/
│       ├── package.json
│       └── Dockerfile
├── packages/
│   ├── contracts/              # Pydantic/TS schemas
│   ├── controllers/            # Five-axis controllers
│   ├── adapters/               # Engine adapters
│   ├── tooling/                # Tool registry, MVR, receipts
│   ├── memory/                 # Memory systems
│   └── planning/               # Planning & search
├── docs/                       # Documentation
├── infrastructure/             # Deployment configs
│   ├── docker/
│   ├── k8s/
│   └── helm/
└── .github/
    └── workflows/              # CI/CD pipelines
```

## Steps

### Step 1: Repository Structure Setup
**Owner:** Platform Eng  
**Duration:** 2 hours  
**Deliverables:**
- Monorepo directory structure created
- Package.json and pyproject.toml files initialized
- Workspace configuration for pnpm and uv

**Commands:**
```bash
# Initialize monorepo structure
mkdir -p apps/{api,ui} packages/{contracts,controllers,adapters,tooling,memory,planning} infrastructure/{docker,k8s,helm} .github/workflows

# Initialize package managers
pnpm init -y
pnpm -w add -D typescript eslint prettier @types/node
cd apps/api && uv init && uv add fastapi pydantic redis psycopg2-binary
cd ../ui && pnpm init && pnpm add react react-dom next typescript
```

### Step 2: Development Environment Configuration
**Owner:** Platform Eng  
**Duration:** 1 hour  
**Deliverables:**
- ESLint and Prettier configuration
- TypeScript configuration
- Python linting (ruff, black)
- Pre-commit hooks

**Commands:**
```bash
# Configure linting and formatting
pnpm -w add -D eslint-config-prettier prettier-plugin-tailwindcss
cd apps/api && uv add ruff black mypy
cd ../ui && pnpm add -D @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

### Step 3: CI/CD Pipeline Setup
**Owner:** Platform Eng  
**Duration:** 2 hours  
**Deliverables:**
- GitHub Actions workflows
- Build, test, and lint jobs
- Dependency caching
- Security scanning

**Files to create:**
- `.github/workflows/ci.yml` - Main CI pipeline
- `.github/workflows/security.yml` - Security scanning
- `.github/workflows/release.yml` - Release automation

### Step 4: Core Documentation Foundation
**Owner:** Architecture Guild  
**Duration:** 3 hours  
**Deliverables:**
- DOC-ADR-0001 - Repository architecture decisions
- DOC-RUNBOOK-LOCAL - Local development guide
- Documentation templates and conventions

**Documents to create:**
- `/docs/ADR/0001-repo-architecture.md`
- `/docs/runbooks/local_dev.md`
- `/docs/templates/` - Documentation templates

### Step 5: Basic Application Scaffolding
**Owner:** Platform Eng  
**Duration:** 2 hours  
**Deliverables:**
- FastAPI application skeleton
- React application skeleton
- Basic routing and health checks

**Files to create:**
- `apps/api/app/main.py` - FastAPI app with health check
- `apps/ui/src/pages/index.tsx` - Basic React page
- `apps/ui/next.config.js` - Next.js configuration

## Acceptance Criteria

### Repository Structure
- [ ] All directories exist with proper structure
- [ ] Package managers configured (pnpm workspaces, uv)
- [ ] TypeScript and Python configurations working
- [ ] Linting and formatting rules established

### CI/CD Pipeline
- [ ] GitHub Actions workflows run successfully
- [ ] Build, test, and lint jobs pass
- [ ] Security scanning integrated
- [ ] Dependency caching configured

### Documentation
- [ ] DOC-ADR-0001 written and reviewed
- [ ] DOC-RUNBOOK-LOCAL provides clear setup instructions
- [ ] Documentation templates available
- [ ] All docs follow front-matter conventions

### Application Scaffolding
- [ ] FastAPI app starts and responds to health check
- [ ] React app builds and runs locally
- [ ] Basic routing working in both apps
- [ ] Docker builds succeed

## KPIs
- **Setup Time:** New developer can clone and run locally in < 10 minutes
- **CI Time:** Full pipeline completes in < 15 minutes
- **Documentation Coverage:** 100% of planned docs have templates/stubs
- **Build Success Rate:** 100% of builds pass on main branch

## Risks & Mitigations

### Risk: Complex Monorepo Setup
- **Mitigation:** Clear documentation and automation scripts
- **Fallback:** Start with simpler structure, evolve over time

### Risk: CI Pipeline Complexity
- **Mitigation:** Start with basic jobs, add complexity incrementally
- **Fallback:** Manual verification until automation is stable

### Risk: Documentation Drift
- **Mitigation:** Automated checks for doc structure and links
- **Fallback:** Regular manual audits

## Rollback Plan
If issues arise:
1. Revert to previous commit
2. Document what went wrong in ADR
3. Simplify approach and retry
4. Consider alternative repository structure

## Links
- [DOC-META-TOC](/docs/TOC.md) - Master documentation index
- [DOC-META-GLOSSARY](/docs/GLOSSARY.md) - Terminology
- [cursor-tasks.json](/cursor-tasks.json) - Development orchestration
- [Phase 01](/docs/phases/phase-01_contracts_streaming.md) - Next phase

---

## Acceptance & Traceability
- **Acceptance:** All acceptance criteria met, CI pipeline green, documentation complete
- **Traceability:** Phase 01 depends on this phase completion