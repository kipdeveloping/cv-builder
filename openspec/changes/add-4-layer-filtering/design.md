## Context

The current talent wall uses a simple text-based sector filter with `sector_name__icontains`. The system needs to evolve into a hierarchical, faceted filtering system with weighted scoring. The existing codebase has a `SectorTag` model that was never populated (fixture has wrong app label) and a `UserProfile` with `sector_name` as a CharField.

## Goals / Non-Goals

**Goals:**
- Implement 4-layer hierarchical tag system (Sector > Role > Specialty > Tags)
- Enable profile tagging with MUST/NICE associations
- Provide faceted search with weighted scoring (0-100%)
- Maintain existing dashboard design patterns
- Keep filters independent (no cascading requirement)

**Non-Goals:**
- Salary range filtering (removed per user request)
- Cascading filter dependencies
- Complex scoring algorithms (using simplified weighted approach)
- Breaking existing dashboard layout

## Decisions

### Decision 1: Separate models for each hierarchy level
**Choice**: Create SectorRol, RolEspecialidad, and Tag as separate models with foreign keys.

**Alternatives considered**:
- Single Tag model with parent self-reference: Rejected because it loses type safety and makes queries complex
- Materialized path: Rejected for simplicity; 4 levels don't need graph traversal

**Rationale**: Separate models provide clear relationships, easy querying, and Django admin integration.

### Decision 2: ProfileTag with tag_type field
**Choice**: Single ProfileTag model with `tag_type` field (must/nice) instead of separate must_tags and nice_tags fields.

**Alternatives considered**:
- Two separate ManyToMany fields: Rejected because it complicates queries and doesn't scale
- JSON field with nested structure: Rejected for query complexity

**Rationale**: Single junction table with type field allows flexible queries and easy administration.

### Decision 3: Weighted scoring with fixed weights
**Choice**: Fixed weights (Sector=30, Role=25, Specialty=20, MustTag=15, NiceTag=10) instead of configurable weights.

**Alternatives considered**:
- Configurable weights per tag: Rejected for complexity; fixed weights cover 90% of use cases
- Percentage-based scoring: Rejected because it doesn't account for filter importance

**Rationale**: Fixed weights are simple, predictable, and easy to understand. Can be made configurable later if needed.

### Decision 4: Real-time search with debouncing
**Choice**: Client-side filtering with debounced API calls (300ms delay) instead of instant API calls on each keystroke.

**Alternatives considered**:
- Instant API calls: Rejected because it creates too many requests
- Server-side only filtering: Rejected for latency; client can cache hierarchy

**Rationale**: Debouncing balances responsiveness with server load. Hierarchy data is cached client-side.

### Decision 5: Adapt to existing dashboard patterns
**Choice**: Add "Mis Habilidades" section following existing card patterns with modal editing.

**Alternatives considered**:
- Separate page for tag management: Rejected for UX consistency
- Inline editing: Rejected because it clutters the sidebar

**Rationale**: Consistent with existing dashboard patterns (Bio, Work Preferences all use cards + modals).

## Risks / Trade-offs

**Risk**: Performance with large tag combinations
**Mitigation**: Implement pagination and limit results to 100 profiles per query

**Risk**: Complex scoring calculations on large datasets
**Mitigation**: Use database-level filtering first, then calculate scores only on filtered set

**Risk**: Fixture migration may fail if data is inconsistent
**Mitigation**: Create migration script with validation and rollback capability

**Risk**: Client-side caching may show stale hierarchy
**Mitigation**: Refresh hierarchy on page load and provide manual refresh option

**Trade-off**: Fixed weights vs configurable weights
**Acceptance**: Fixed weights are simpler and cover most cases; can be extended later

**Trade-off**: Independent filters vs cascading filters
**Acceptance**: Independent filters are more flexible; users can组合any criteria

## Migration Plan

1. Fix existing fixture (resumes → accounts app label)
2. Create new models (SectorRol, RolEspecialidad, Tag, ProfileTag)
3. Run migrations
4. Populate hierarchy from fixture data
5. Migrate existing `sector_name` to `sector` FK on UserProfile
6. Update API endpoints
7. Update frontend

**Rollback**: Keep old `sector_name` field during transition; can revert by removing FK and restoring text field.

## Open Questions

None at this time. All major decisions have been resolved through user consultation.
