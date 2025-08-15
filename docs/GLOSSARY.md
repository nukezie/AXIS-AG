---
id: DOC-META-GLOSSARY
title: AXIOM-25 MATRIX — Glossary & Taxonomy
owner: Architecture Guild
status: draft
version: 2025.08.0
depends_on: [DOC-META-TOC]
---

# Glossary & Taxonomy

> Canonical definitions for terms used across AXIOM-25. Link terms in docs by **Doc ID** where relevant.

## Core Concepts
- **AXIOM-25 Matrix** — The multi-axis, engine-agnostic agent architecture. (See DOC-CORE-ARCH-OVERVIEW)
- **Five-Axis Doctrine** — Operational split: **Reasoning × Assignment × Planning × Production × Tasks**. (DOC-CORE-FIVE-AXIS)
- **Control Plane** — Host for controllers, state, and policies; talks to engines via adapters. (DOC-CORE-CONTROL-PLANE)
- **EngineAdapter** — Swappable interface for execution backends (LangGraph, OpenAI Agents, AG2, Local). (DOC-CORE-ENGINE-ADAPTER)

## Contracts & Events
- **TaskSpec** — Input contract for a run: goal, inputs, allowed_tools, backend_pref, SLA budget, verification. (DOC-CONTRACTS-TASKSPEC)
- **Budget** — Limits for tokens, time, branch width, reflection passes. (DOC-CONTRACTS-BUDGET)
- **VerifyContract** — Assertions, scorers, refusal thresholds. (DOC-CONTRACTS-VERIFY)
- **ToolSpec** — Schema-first tool definition incl. auth and trust level. (DOC-CONTRACTS-TOOLSPEC)
- **RunEvent** — Streamed event item: `token|thought|tool_start|tool_end|verdict|budget|error|done`. (DOC-CONTRACTS-RUNEVENT)
- **Receipts** — Structured audit of tool calls (args redacted), response hash, latency, cost. (DOC-TOOL-RECEIPTS)

## Controllers (Five Axes)
- **Budgeter / TTC** — Controller that allocates compute (depth/width/reflection/time) and enforces SLA. (DOC-CTRL-BUDGETER)
- **MeCo Gate** — Metacognitive gating: decides LLM-only vs. tool vs. delegate. (DOC-CTRL-MECO)
- **Planner (Search-Aware)** — Builds/repairs Graph-of-Thought; schedules search nodes; scores branches. (DOC-CTRL-PLANNER)
- **MetaVerifier (MVR)** — Pre- and post-tool verification; auto-repair; reflection. (DOC-CTRL-MVR)
- **VerifierAgent** — Unified verification pipeline for step/final verdicts and refusal logic. (DOC-CTRL-VERIFIER)
- **Task Orchestrator** — Enforces TaskSpec, budgets, and lifecycle. (DOC-CTRL-TASK-ORCH)

## Memory
- **Episodic Memory** — Short-lived run traces and reflection notes (Redis). (DOC-MEM-EPISODIC)
- **Semantic Memory** — Vector store for prior tasks, tool specs, domain docs (pgvector/Qdrant). (DOC-MEM-SEMANTIC)
- **Procedural Memory** — Tool schemas, verification recipes, policy bundles. (DOC-MEM-PROCEDURAL)
- **Memory Broker** — Promotes/prunes memory items by utility and coverage. (DOC-MEM-BROKER)

## Planning & Search
- **Graph-of-Thought (GoT)** — Directed graph of subgoals/tools with dependencies. (DOC-CTRL-PLANNER)
- **Search Node** — Planned step that performs information retrieval with budgeted cost. (DOC-PLAN-SEARCH-NODE)
- **PRM (Process Reward Model)** — Heuristic or learned scorer for intermediate steps/branches. (DOC-CTRL-PLANNER, DOC-VERI-UNIFIED)

## Verification & Governance
- **SVS (Self-Verification Sampling)** — Sample k candidates; choose via verification signals. (DOC-VERI-SVS)
- **Unified Verification** — Combined self-checks, tool-assisted checks, and assertions. (DOC-VERI-UNIFIED)
- **MultiAgentBench** — Evaluation harness for multi-agent collaboration/competition stability. (DOC-VERI-MABENCH)
- **Risk Policy** — Allow-lists, refusal thresholds, redaction, sandbox rules. (DOC-VERI-RISK)
- **MVR Preflight** — Tool enablement gate: schema checks + example invocation. (DOC-TOOL-MVR-PREFLIGHT)

## Tooling & Security
- **Tool Registry** — Source of truth for ToolSpecs and trust levels. (DOC-TOOL-REGISTRY)
- **Sandbox Execution** — RestrictedPython/micro-VM isolation + egress allow-list. (DOC-TOOL-SANDBOX)
- **PII Redaction** — Policy for masking personally identifiable info in streams and logs. (DOC-SEC-REDACTION)
- **Incident Mode** — Elevated safety posture: higher refusal, disable untrusted tools, read-only memory. (DOC-SEC-INCIDENT)

## UI / API
- **Matrix Dashboard** — Five-axis live control and KPIs. (DOC-UI-MATRIX-DASH)
- **Graph View** — Real-time plan/execution visualization. (DOC-UI-GRAPH-VIEW)
- **Run Console** — Live tokens, receipts, verdicts. (DOC-UI-RUN-CONSOLE)
- **Budget Panel** — Operator controls for TTC policies. (DOC-UI-BUDGET-PANEL)
- **Verifier Panel** — Manage assertions and thresholds. (DOC-UI-VERIFIER-PANEL)
- **Tool Catalog** — Register tools, run MVR preflight, toggle trust. (DOC-UI-TOOL-CATALOG)
- **API Gateway** — FastAPI surface; endpoints, auth, SSE. (DOC-API-GATEWAY)
- **Event Model** — Semantics of RunEvent stream. (DOC-API-EVENT-MODEL)

## Policies & Execution
- **Policy Bundle** — Versioned YAML of controller thresholds and profiles (Tight, Balanced, Max). (DOC-POLICY-BUNDLE)
- **Profiles** — Named policy presets for TTC & verification.
- **Phases** — Execution plan docs for building the system. (DOC-PHASE-00 … DOC-PHASE-07)
- **ADRs** — Architecture Decision Records; immutable history of tradeoffs. (DOC-ADR-0001+)

---

## Naming & Acronyms
- **TTC** — Test-Time Compute (budgeted reasoning)
- **GoT** — Graph-of-Thought
- **MVR** — Meta-Verification & Reflection
- **MeCo** — Metacognitive Tool Gating
- **PRM** — Process Reward Model
- **SVS** — Self-Verification Sampling
- **SLA** — Service-Level Agreement (budget/latency/accuracy bound)
- **TRiSM** — Trust, Risk, and Security Management

---

## Acceptance & Traceability
- **Acceptance:** Every term above appears consistently across docs; undefined acronyms are eliminated. Each entry references at least one Doc ID for deeper detail.
- **Traceability:** Changes to terms must bump this doc's `version` and be referenced in **DOC-ADR-0001**.