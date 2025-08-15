---
id: DOC-PHASE-04
title: Phase 04 — Operator UI v2 (Five-Axis Control)
owner: UX Eng
status: draft
version: 2025.08.0
depends_on: [DOC-PHASE-03, DOC-UI-MATRIX-DASH, DOC-UI-GRAPH-VIEW, DOC-UI-BUDGET-PANEL, DOC-UI-VERIFIER-PANEL, DOC-UI-TOOL-CATALOG, DOC-API-EVENT-MODEL]
---

# Phase 04 — Operator UI v2 (Five-Axis Control)

## Objective
Build the comprehensive operator UI with five-axis control, real-time graph visualization, budget management, verification panels, and tool catalog with MVR preflight.

## Scope
- Matrix Dashboard with KPIs and toggles
- Graph View with real-time plan/execution visualization
- Budget Panel for TTC policy management
- Verifier Panel for assertion and threshold management
- Tool Catalog with MVR preflight interface
- Real-time event streaming and visualization

## Inputs
- [DOC-UI-MATRIX-DASH](/docs/ui/matrix_dashboard_spec.md) - Matrix dashboard specification
- [DOC-UI-GRAPH-VIEW](/docs/ui/graph_view_spec.md) - Graph view specification
- [DOC-UI-BUDGET-PANEL](/docs/ui/budget_panel_spec.md) - Budget panel specification
- [DOC-UI-VERIFIER-PANEL](/docs/ui/verifier_panel_spec.md) - Verifier panel specification
- [DOC-UI-TOOL-CATALOG](/docs/ui/tool_catalog_spec.md) - Tool catalog specification
- [DOC-API-EVENT-MODEL](/docs/api/event_model.md) - Event streaming model

## Dependencies
- Phase 03 completion (controllers v2 and adapters)
- All UI specifications
- API event model

## Artifacts

### Documentation
- **DOC-UI-MATRIX-DASH** — `/docs/ui/matrix_dashboard_spec.md` - Matrix dashboard specification
- **DOC-UI-GRAPH-VIEW** — `/docs/ui/graph_view_spec.md` - Graph view specification
- **DOC-UI-BUDGET-PANEL** — `/docs/ui/budget_panel_spec.md` - Budget panel specification
- **DOC-UI-VERIFIER-PANEL** — `/docs/ui/verifier_panel_spec.md` - Verifier panel specification
- **DOC-UI-TOOL-CATALOG** — `/docs/ui/tool_catalog_spec.md` - Tool catalog specification

### Code Structure
```
/apps/ui/src/
├── features/
│   ├── matrix/                   # Matrix Dashboard
│   │   ├── MatrixDashboard.tsx
│   │   ├── KPICard.tsx
│   │   ├── AxisToggle.tsx
│   │   └── types.ts
│   ├── graph/                    # Graph View
│   │   ├── GraphView.tsx
│   │   ├── NodeInspector.tsx
│   │   ├── EdgeRenderer.tsx
│   │   └── types.ts
│   ├── budget/                   # Budget Panel
│   │   ├── BudgetPanel.tsx
│   │   ├── TTCControls.tsx
│   │   ├── PolicySelector.tsx
│   │   └── types.ts
│   ├── verifier/                 # Verifier Panel
│   │   ├── VerifierPanel.tsx
│   │   ├── AssertionEditor.tsx
│   │   ├── ThresholdSlider.tsx
│   │   └── types.ts
│   ├── tools/                    # Tool Catalog
│   │   ├── ToolCatalog.tsx
│   │   ├── MVRPreflight.tsx
│   │   ├── TrustLevelEditor.tsx
│   │   └── types.ts
│   └── console/                  # Run Console (enhanced)
│       ├── RunConsole.tsx
│       ├── EventStream.tsx
│       ├── ReceiptViewer.tsx
│       └── types.ts
├── components/
│   ├── common/
│   │   ├── Layout.tsx
│   │   ├── Navigation.tsx
│   │   └── Loading.tsx
│   └── ui/                       # shadcn/ui components
├── hooks/
│   ├── useMatrixState.ts
│   ├── useGraphData.ts
│   ├── useBudgetControls.ts
│   ├── useVerifierState.ts
│   └── useToolRegistry.ts
├── stores/
│   ├── matrixStore.ts            # Zustand store for matrix state
│   ├── graphStore.ts             # Graph state management
│   └── settingsStore.ts          # User settings
└── utils/
    ├── graphHelpers.ts
    ├── eventParsers.ts
    └── formatters.ts
```

## Steps

### Step 1: UI Specifications Design
**Owner:** UX Eng  
**Duration:** 6 hours  
**Deliverables:**
- All UI specifications designed and documented
- Component architecture and interactions
- State management patterns
- User experience flows

**Documents to create:**
- `/docs/ui/matrix_dashboard_spec.md` - Five-axis dashboard with KPIs and controls
- `/docs/ui/graph_view_spec.md` - Real-time graph visualization with node inspection
- `/docs/ui/budget_panel_spec.md` - TTC policy management interface
- `/docs/ui/verifier_panel_spec.md` - Verification assertion and threshold management
- `/docs/ui/tool_catalog_spec.md` - Tool registration and MVR preflight interface

### Step 2: State Management Setup
**Owner:** UX Eng  
**Duration:** 3 hours  
**Deliverables:**
- Zustand stores for matrix state
- Graph state management
- Settings persistence
- Real-time state synchronization

**Files to create:**
- `apps/ui/src/stores/matrixStore.ts` - Matrix dashboard state
- `apps/ui/src/stores/graphStore.ts` - Graph visualization state
- `apps/ui/src/stores/settingsStore.ts` - User settings and preferences

### Step 3: Matrix Dashboard Implementation
**Owner:** UX Eng  
**Duration:** 4 hours  
**Deliverables:**
- Five-axis dashboard layout
- KPI cards and metrics display
- Axis toggles and controls
- Real-time updates

**Files to create:**
- `apps/ui/src/features/matrix/MatrixDashboard.tsx` - Main dashboard component
- `apps/ui/src/features/matrix/KPICard.tsx` - KPI display component
- `apps/ui/src/features/matrix/AxisToggle.tsx` - Axis control component
- `apps/ui/src/features/matrix/types.ts` - Matrix types

### Step 4: Graph View Implementation
**Owner:** UX Eng  
**Duration:** 6 hours  
**Deliverables:**
- Real-time graph visualization
- Node inspection and details
- Edge rendering and styling
- Interactive graph controls

**Files to create:**
- `apps/ui/src/features/graph/GraphView.tsx` - Main graph component
- `apps/ui/src/features/graph/NodeInspector.tsx` - Node detail panel
- `apps/ui/src/features/graph/EdgeRenderer.tsx` - Edge visualization
- `apps/ui/src/features/graph/types.ts` - Graph types

### Step 5: Budget Panel Implementation
**Owner:** UX Eng  
**Duration:** 3 hours  
**Deliverables:**
- TTC policy controls
- Budget allocation sliders
- Policy selector interface
- Real-time budget monitoring

**Files to create:**
- `apps/ui/src/features/budget/BudgetPanel.tsx` - Budget management panel
- `apps/ui/src/features/budget/TTCControls.tsx` - TTC control components
- `apps/ui/src/features/budget/PolicySelector.tsx` - Policy selection interface
- `apps/ui/src/features/budget/types.ts` - Budget types

### Step 6: Verifier Panel Implementation
**Owner:** UX Eng  
**Duration:** 3 hours  
**Deliverables:**
- Verification assertion editor
- Threshold sliders and controls
- Verification status display
- Real-time verification feedback

**Files to create:**
- `apps/ui/src/features/verifier/VerifierPanel.tsx` - Verifier management panel
- `apps/ui/src/features/verifier/AssertionEditor.tsx` - Assertion editing interface
- `apps/ui/src/features/verifier/ThresholdSlider.tsx` - Threshold control components
- `apps/ui/src/features/verifier/types.ts` - Verifier types

### Step 7: Tool Catalog Implementation
**Owner:** UX Eng  
**Duration:** 4 hours  
**Deliverables:**
- Tool registration interface
- MVR preflight interface
- Trust level management
- Tool status and monitoring

**Files to create:**
- `apps/ui/src/features/tools/ToolCatalog.tsx` - Tool catalog main component
- `apps/ui/src/features/tools/MVRPreflight.tsx` - MVR preflight interface
- `apps/ui/src/features/tools/TrustLevelEditor.tsx` - Trust level management
- `apps/ui/src/features/tools/types.ts` - Tool catalog types

### Step 8: Enhanced Console Implementation
**Owner:** UX Eng  
**Duration:** 2 hours  
**Deliverables:**
- Enhanced run console
- Event stream visualization
- Receipt viewer integration
- Real-time event parsing

**Files to create:**
- `apps/ui/src/features/console/RunConsole.tsx` - Enhanced console component
- `apps/ui/src/features/console/EventStream.tsx` - Event stream visualization
- `apps/ui/src/features/console/ReceiptViewer.tsx` - Receipt viewing interface
- `apps/ui/src/features/console/types.ts` - Console types

### Step 9: Integration and Testing
**Owner:** UX Eng  
**Duration:** 3 hours  
**Deliverables:**
- Component integration
- Real-time event handling
- User experience testing
- Performance optimization

**Test scenarios:**
- Operator changes policies live and impacts runs
- Receipts accessible from graph nodes
- Real-time updates work across all panels
- UI is responsive and user-friendly

## Acceptance Criteria

### Matrix Dashboard
- [ ] Five-axis dashboard displays correctly
- [ ] KPI cards show real-time metrics
- [ ] Axis toggles control system behavior
- [ ] Real-time updates work properly

### Graph View
- [ ] Real-time graph visualization functional
- [ ] Node inspection shows details
- [ ] Edge rendering and styling correct
- [ ] Interactive controls work

### Budget Panel
- [ ] TTC policy controls functional
- [ ] Budget allocation sliders work
- [ ] Policy selector interface working
- [ ] Real-time budget monitoring active

### Verifier Panel
- [ ] Verification assertion editor functional
- [ ] Threshold sliders and controls work
- [ ] Verification status display correct
- [ ] Real-time verification feedback working

### Tool Catalog
- [ ] Tool registration interface working
- [ ] MVR preflight interface functional
- [ ] Trust level management working
- [ ] Tool status and monitoring active

### Integration
- [ ] All panels integrate correctly
- [ ] Real-time event handling works
- [ ] User experience is smooth
- [ ] Performance meets requirements

## KPIs
- **UI Responsiveness:** < 100ms for user interactions
- **Real-time Updates:** < 200ms for event propagation
- **User Experience:** > 90% user satisfaction score
- **Performance:** < 2s initial load time

## Risks & Mitigations

### Risk: UI Complexity
- **Mitigation:** Modular component architecture
- **Fallback:** Simplified interface with core functionality

### Risk: Real-time Performance
- **Mitigation:** Efficient state management and event handling
- **Fallback:** Polling-based updates if streaming fails

### Risk: User Experience Issues
- **Mitigation:** User testing and iterative design
- **Fallback:** Basic interface with essential features

### Risk: Integration Complexity
- **Mitigation:** Clear interfaces and contracts
- **Fallback:** Manual coordination if automation fails

## Rollback Plan
If issues arise:
1. Revert to basic console interface
2. Disable problematic UI features
3. Document issues in ADR
4. Simplify approach and retry

## Links
- [DOC-PHASE-03](/docs/phases/phase-03_controllers_v2_sota.md) - Previous phase
- [DOC-UI-MATRIX-DASH](/docs/ui/matrix_dashboard_spec.md) - Matrix dashboard specification
- [DOC-API-EVENT-MODEL](/docs/api/event_model.md) - Event streaming model
- [Phase 05](/docs/phases/phase-05_eval_governance.md) - Next phase

---

## Acceptance & Traceability
- **Acceptance:** All acceptance criteria met, UI functional, user experience smooth
- **Traceability:** Phase 05 depends on this phase completion