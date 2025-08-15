---
id: DOC-META-TOC
title: AXIOM-25 MATRIX — Documentation Table of Contents & Generation Guide
owner: Architecture Guild
status: draft
version: 2025.08.0
depends_on: []
---

# AXIOM-25 MATRIX — Documentation Table of Contents & Generation Guide

## Conventions (apply to all docs)
- **Repo paths:** all docs live under `/docs`.
- **Naming:** `kebab-case`, one topic per file, no spaces.
- **Doc ID:** upper-snake code derived from path, e.g., `/docs/core/architecture_overview.md` → `DOC-CORE-ARCH-OVERVIEW`.
- **Front-matter (first lines in every doc):**
  ```yaml
  ---
  id: DOC-<AREA>-<SUBJECT>
  title: <Human Title>
  owner: <Team/Person>
  status: draft|review|approved
  version: 2025.08.0
  depends_on: [<doc_ids>]
  ---
  ```
- **Acceptance block:** every doc ends with Acceptance & Traceability (tests + dependencies).
- **Cross-linking:** always link by Doc ID and path.

## Directory Map
```
/docs
  /core
  /controllers
  /contracts
  /adapters
  /tooling
  /memory
  /planning
  /verification
  /ui
  /api
  /eval
  /security
  /ops
  /phases
  /ADR
  /policy_bundle
  /runbooks
```

## Document Index

### 0) Meta & Index
- **DOC-META-TOC** — `/docs/TOC.md` (this file)
- **DOC-META-GLOSSARY** — `/docs/GLOSSARY.md`

### 1) Architecture Core
- **DOC-CORE-ARCH-OVERVIEW** — `/docs/core/architecture_overview.md`
- **DOC-CORE-FIVE-AXIS** — `/docs/core/five_axis_doctrine.md`
- **DOC-CORE-CONTROL-PLANE** — `/docs/core/control_plane_spec.md`
- **DOC-CORE-ENGINE-ADAPTER** — `/docs/core/engine_adapter_interface.md`

### 2) Controllers (Five Axes)
- **DOC-CTRL-BUDGETER** — `/docs/controllers/budgeter_spec.md`
- **DOC-CTRL-MECO** — `/docs/controllers/mecogate_design.md`
- **DOC-CTRL-PLANNER** — `/docs/controllers/planner_spec.md`
- **DOC-CTRL-MVR** — `/docs/controllers/metaverifier_spec.md`
- **DOC-CTRL-VERIFIER** — `/docs/controllers/verifieragent_spec.md`
- **DOC-CTRL-TASK-ORCH** — `/docs/controllers/task_orchestrator_spec.md`

### 3) Contracts & Schemas
- **DOC-CONTRACTS-TASKSPEC** — `/docs/contracts/taskspec_schema.md`
- **DOC-CONTRACTS-BUDGET** — `/docs/contracts/budget_schema.md`
- **DOC-CONTRACTS-VERIFY** — `/docs/contracts/verifycontract_schema.md`
- **DOC-CONTRACTS-TOOLSPEC** — `/docs/contracts/toolspec_schema.md`
- **DOC-CONTRACTS-RUNEVENT** — `/docs/contracts/runevent_schema.md`

### 4) Execution Engines & Adapters
- **DOC-ADAPT-LANGGRAPH** — `/docs/adapters/langgraph_adapter.md`
- **DOC-ADAPT-OPENAI** — `/docs/adapters/openai_adapter.md`
- **DOC-ADAPT-AG2** — `/docs/adapters/ag2_adapter.md`
- **DOC-ADAPT-LOCAL** — `/docs/adapters/local_adapter.md`

### 5) Tooling
- **DOC-TOOL-REGISTRY** — `/docs/tooling/tool_registry_spec.md`
- **DOC-TOOL-MVR-PREFLIGHT** — `/docs/tooling/mvr_preflight_procedure.md`
- **DOC-TOOL-RECEIPTS** — `/docs/tooling/tool_receipts_spec.md`
- **DOC-TOOL-SANDBOX** — `/docs/tooling/sandbox_exec.md`

### 6) Memory
- **DOC-MEM-EPISODIC** — `/docs/memory/episodic_memory_spec.md`
- **DOC-MEM-SEMANTIC** — `/docs/memory/semantic_memory_spec.md`
- **DOC-MEM-PROCEDURAL** — `/docs/memory/procedural_memory_spec.md`
- **DOC-MEM-BROKER** — `/docs/memory/memory_broker_spec.md`

### 7) Planning & Search
- **DOC-PLAN-SEARCH-NODE** — `/docs/planning/search_node_design.md`

### 8) Verification & Governance
- **DOC-VERI-SVS** — `/docs/verification/svs_methodology.md`
- **DOC-VERI-UNIFIED** — `/docs/verification/unified_verification_spec.md`
- **DOC-VERI-MABENCH** — `/docs/verification/multiagentbench_harness.md`
- **DOC-VERI-RISK** — `/docs/verification/risk_policy_doc.md`

### 9) Operator UI
- **DOC-UI-MATRIX-DASH** — `/docs/ui/matrix_dashboard_spec.md`
- **DOC-UI-GRAPH-VIEW** — `/docs/ui/graph_view_spec.md`
- **DOC-UI-RUN-CONSOLE** — `/docs/ui/run_console_spec.md`
- **DOC-UI-BUDGET-PANEL** — `/docs/ui/budget_panel_spec.md`
- **DOC-UI-VERIFIER-PANEL** — `/docs/ui/verifier_panel_spec.md`
- **DOC-UI-TOOL-CATALOG** — `/docs/ui/tool_catalog_spec.md`

### 10) API Surface
- **DOC-API-GATEWAY** — `/docs/api/api_gateway_spec.md`
- **DOC-API-EVENT-MODEL** — `/docs/api/event_model.md`

### 11) Evaluation & CI/CD
- **DOC-EVAL-METRICS** — `/docs/eval/metrics_kpis_doc.md`
- **DOC-EVAL-REGRESSION** — `/docs/eval/regression_pack_doc.md`
- **DOC-EVAL-CICD** — `/docs/eval/cicd_gates_doc.md`

### 12) Security & TRiSM
- **DOC-SEC-THREAT** — `/docs/security/threat_model.md`
- **DOC-SEC-REDACTION** — `/docs/security/redaction_policy.md`
- **DOC-SEC-INCIDENT** — `/docs/security/incident_mode_spec.md`

### 13) Deployment & Ops
- **DOC-OPS-DEPLOY** — `/docs/ops/deployment_and_ops.md`
- **DOC-OPS-OBS** — `/docs/ops/observability_stack_spec.md`
- **DOC-OPS-RUNBOOK** — `/docs/ops/sre_runbook.md`

### 14) Phases (Execution Plan)
- **DOC-PHASE-00** — `/docs/phases/phase-00_bootstrap.md`
- **DOC-PHASE-01** — `/docs/phases/phase-01_contracts_streaming.md`
- **DOC-PHASE-02** — `/docs/phases/phase-02_controllers_v1.md`
- **DOC-PHASE-03** — `/docs/phases/phase-03_controllers_v2_sota.md`
- **DOC-PHASE-04** — `/docs/phases/phase-04_ui_operator_v2.md`
- **DOC-PHASE-05** — `/docs/phases/phase-05_eval_governance.md`
- **DOC-PHASE-06** — `/docs/phases/phase-06_security_trism.md`
- **DOC-PHASE-07** — `/docs/phases/phase-07_deployment_sre.md`

### 15) ADRs, Policies, Runbooks
- **DOC-ADR-0001** — `/docs/ADR/0001-repo-architecture.md`
- **DOC-POLICY-BUNDLE** — `/docs/policy_bundle/2025.08-matrix-v3.1.yaml`
- **DOC-RUNBOOK-LOCAL** — `/docs/runbooks/local_dev.md`
- **DOC-RUNBOOK-INCIDENT** — `/docs/runbooks/incident_mode.md`
- **DOC-RUNBOOK-RELEASE** — `/docs/runbooks/release.md`

## Standard Generation Procedure (SOP)

### Request format
```
Generate: <doc_id or path>
Audience: <engineers|operators|exec>
Scope: <narrow|full>  Constraints: <list>
Inputs: <links or paste>  Dependencies: <doc_ids>
Target state: <draft|review|approved>
```

### Process
1. **Assemble inputs** → collect dependencies by Doc ID.
2. **Apply template** → fill sections; add diagrams or placeholders.
3. **Wire cross-refs** → link doc IDs and paths.
4. **Acceptance & Traceability** → add tests/KPIs + dependency list.
5. **Status move** → draft → review → approved.

## Acceptance & Traceability
- **Acceptance:** Every index entry maps to an existing file or stub with front-matter. SOP included. Cross-links use Doc IDs.
- **Traceability:** Changes to the ToC must update version and be referenced in **DOC-ADR-0001**.