---
id: DOC-CORE-ARCH-OVERVIEW
title: Architecture Overview — AXIOM-25 MATRIX (v3.1)
owner: Architecture Guild
status: draft
version: 2025.08.0
depends_on: [DOC-META-TOC, DOC-META-GLOSSARY]
---

# Architecture Overview — AXIOM-25 MATRIX (v3.1)

## 1) Purpose & Vision

AXIOM-25 is a **graph-native, budget-aware, self-verifying** agent architecture. It separates our *ideology* (Five-Axis Doctrine) from *execution engines* (LangGraph, OpenAI Agents, AG2, Local) via a strict **Control Plane** and **EngineAdapter** layer.

**Goals**
- Raise accuracy under **SLA budgets** (tokens, time) via **Test-Time Compute (TTC)** control.
- Make tool use reliable with **Meta-Verification & Reflection (MVR)** + **Unified Verification**.
- Treat **search as a first-class thought** within planning.
- Keep backends **swappable** without touching domain logic.

**Non-Goals**
- Tightly coupling to any single LLM/provider.
- Exposing raw chain-of-thought; we stream **summarized rationales** + receipts only.

## 2) Core Principles (doctrine-aligned)

1. **Five-Axis Control**: Reasoning × Assignment × Planning × Production × Tasks.
2. **Budgeted Reasoning (TTC)**: depth/width/reflection/time are adaptive, not fixed.
3. **Verified Tooling**: every tool call gated + pre/post verified; reflection repairs.
4. **Engine Agnosticism**: all execution goes through **EngineAdapter**.
5. **Receipts & Telemetry**: every artifact cites tools, costs, latencies, and scores.
6. **Governance by Bench**: changes ship only if they improve governed KPIs.

## 3) System Context

```mermaid
flowchart LR
  subgraph UI(Operator UI • React/v0.dev)
    DASH[Matrix Dashboard]
    GRAPH[Graph View]
    CON[Run Console]
  end
  subgraph API(FastAPI • Control Plane)
    GATE[Auth/Policy]
    RUNS[SSE/WS Events]
    CTRL[Controllers (5 Axes)]
    ADAPT[EngineAdapter(s)]
    TOOLREG[Tool Registry + MVR Preflight]
    VERIFY[Verifier Service]
    MEM[Memory Broker]
    OBS[Telemetry/Tracing]
  end
  subgraph Engines(Execution Backends)
    LG[LangGraph]
    OA[OpenAI Agents/Responses]
    AG2[AutoGen-2]
    LOCAL[Local Runner]
  end
  DASH---CON---GRAPH
  UI <--> RUNS
  RUNS --> CTRL
  CTRL <--> TOOLREG
  CTRL <--> VERIFY
  CTRL <--> MEM
  CTRL --> ADAPT
  ADAPT --> LG
  ADAPT --> OA
  ADAPT --> AG2
  ADAPT --> LOCAL
  CTRL --> OBS
```

## 4) Primary Components

### 4.1 Control Plane (see DOC-CORE-CONTROL-PLANE)

Hosts the five controllers and manages state, events, and policies. Never calls engines directly—only via EngineAdapter.

### 4.2 Five Controllers (see DOC-CORE-FIVE-AXIS)

- **Reasoning / Budgeter (TTC)**: allocate depth/width/reflection/time; early-stop.
- **Assignment / MeCo Gate + Assigner**: decide LLM-only vs tool vs delegate; pick tools.
- **Planning / Planner (Search-aware)**: build/repair Graph-of-Thought; schedule search nodes; score branches.
- **Production / MetaVerifier + VerifierAgent**: pre/post tool checks, auto-repair, reflection; unified verification (step/final).
- **Tasks / Orchestrator**: enforce TaskSpec, budgets, VerifyContracts; handle refusal.

### 4.3 Execution Backends (see DOC-CORE-ENGINE-ADAPTER)

Swappable substrates: LangGraph, OpenAI Agents, AG2, Local via a common adapter interface:

`start(task, plan, policy)`, `step(intent)`, `tool_call(spec,args)`, `checkpoint()`, `resume()`.

### 4.4 Contracts & Events (see /docs/contracts/*)

- **TaskSpec**: goal, inputs, allowed_tools, backend_pref, Budget, VerifyContract.
- **Budget**: max_tokens, max_time_s, max_branches, max_reflections.
- **VerifyContract**: assertions, scorers (PRM/heuristics), min_confidence.
- **ToolSpec**: schema-first tool definitions, trust level, limits.
- **RunEvent**: `token|thought|tool_start|tool_end|verdict|budget|error|done`.

## 5) Data Flow (happy path)

1. `POST /runs` with TaskSpec.
2. Planner builds initial graph; Budgeter computes TTC plan.
3. MeCo Gate decides tool/agent need; Assigner selects tool(s).
4. MVR (pre) validates schema/args → Executor calls tool.
5. MVR (post) + Reflection; VerifierAgent scores step.
6. Budgeter updates TTC; Planner repairs/prunes if needed.
7. On pass: finalize artifact + Receipts; stream done.

## 6) Memory Model (see /docs/memory/*)

- **Episodic (Redis)**: compact traces, reflections, checkpoints.
- **Semantic (pgvector/Qdrant)**: embeddings of prior tasks, tools, domain docs.
- **Procedural (Postgres/YAML)**: tool schemas, verification recipes, policy bundles.
- **Memory Broker**: promotion/pruning by utility & coverage.

## 7) Tooling & MVR (see /docs/tooling/*)

- **Registry**: schema-first ToolSpec store; enable only after MVR preflight.
- **Runtime MVR**: pre-call checks (schema/args/trajectory), post-call reflection + bounded retry.
- **Receipts**: redacted args, response hash, latency, cost; linked in final artifacts.

## 8) Verification & Governance (see /docs/verification/*)

- **SVS**: k-way sampling with verification-driven selection/refusal.
- **Unified Verification**: assertions + scorers for both step and final.
- **Bench & CI Gates**: regression pack, KPI thresholds, nightly long-run.

## 9) Security & TRiSM (see /docs/security/*)

- **AuthZ** per-task & per-tool; allow-lists; rate & cost caps.
- **Redaction** in streams/logs; Sandboxed code tools; egress allow-list.
- **Incident Mode**: raise refusal, disable untrusted tools, read-only memory.

## 10) Observability (see /docs/ops/observability_stack_spec.md)

- **OpenTelemetry** spans per node/tool; Prometheus metrics.
- **Dashboards**: accuracy@SLA, cost/solve, refusal rate, tool error taxonomy, search overhead, TTC distributions.

## 11) Deployment & Ops (see /docs/ops/*)

- **Containers** (multi-stage), k8s with HPA, secrets, resource limits.
- **Release**: blue/green or canary; rollback playbook.

## 12) Operator UI (see /docs/ui/*)

- **Matrix Dashboard**: live control of five axes + KPI panels.
- **Graph View**: plan/execution; node inspector (memory, receipts, cost).
- **Run Console**: token stream, tool receipts, verdicts.
- **Budget/Verifier Panels**: profiles, thresholds, refusal policy.
- **Tool Catalog**: register → MVR preflight → enable; trust toggles.

## 13) Roadmap Alignment (see /docs/phases/*)

- **Phase 00**: bootstrap & CI
- **Phase 01**: contracts + streaming
- **Phase 02**: controllers v1
- **Phase 03**: controllers v2 (TTC, search-aware, SVS/MVR v2) + adapters
- **Phase 04**: UI v2 (five-axis control)
- **Phase 05**: eval & governance
- **Phase 06**: security & incident mode
- **Phase 07**: deployment & SRE

## 14) Risks & Mitigations

- **Over-verification latency** → cap depth by budget; batch checks.
- **Search overuse** → penalize in TTC; require marginal gain.
- **Tool schema drift** → nightly MVR preflight; fail fast on mismatch.
- **Adapter skew** → adapter compliance suite across engines.

## Acceptance & Traceability

**Acceptance**
- A new engineer can grok system boundaries, contracts, main flows, and where to find deep specs.
- Diagrams render; all cross-refs point to Doc IDs in the ToC.

**Traceability**
- This overview cites: DOC-CORE-FIVE-AXIS, DOC-CORE-CONTROL-PLANE, DOC-CORE-ENGINE-ADAPTER, all /docs/contracts/*, /docs/memory/*, /docs/tooling/*, /docs/verification/*, /docs/ui/*, /docs/ops/*, /docs/phases/*.