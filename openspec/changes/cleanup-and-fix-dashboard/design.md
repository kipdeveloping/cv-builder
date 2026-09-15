## Context

The project is a Django-based talent marketplace with two main apps: `accounts` (user management, profiles) and `wall` (talent discovery). A previous refactor removed the `apps/resumes` app but left orphaned code. The dashboard's skills modal has HTML but no JavaScript implementation. The data model has legacy fields (`sector_name`) that conflict with the newer FK-based taxonomy.

Key constraints:
- SQLite database (no complex migrations)
- Tailwind CSS v4 for styling
- Python Social Auth for OAuth
- i18n support (12 languages)
- Existing API endpoints for hierarchy and tags

## Goals / Non-Goals

**Goals:**
- Remove all orphaned resume/CV references from runtime code
- Fix the non-functional skills modal in the dashboard
- Clean up the data model (remove `sector_name`, sync `title` with `headline`)
- Simplify profile tags (remove must/nice distinction)
- Fix work preferences rendering
- Update registration to use hierarchy dropdowns

**Non-Goals:**
- Renaming the project or changing "CV Builder" branding
- Changing the wall's searcher-side must/nice tag distinction
- Adding new features beyond fixing existing broken functionality
- Modifying the OAuth or authentication system

## Decisions

### Decision 1: Sequential branching strategy
**Choice**: Create branches in dependency order, each building on the previous merged state.

**Rationale**: Ensures no merge conflicts and project works at every step. Each branch is created from the latest main after the previous branch is merged.

**Alternatives considered**:
- Parallel branches: Would require complex conflict resolution and increase risk of broken states.
- Single branch: Less granular history, harder to revert individual changes.

### Decision 2: Remove `sector_name` field entirely
**Choice**: Drop the `sector_name` CharField from UserProfile and migrate all existing users to the "tecnologia" sector FK.

**Rationale**: `sector_name` is a legacy field that creates confusion. The FK-based taxonomy (`sector` -> `rol` -> `especialidad`) is the source of truth. The `migrate_sector_fk` management command already exists to handle migration.

**Alternatives considered**:
- Keep `sector_name` as fallback: Adds complexity without value since the FK is the primary field.
- Auto-sync `sector_name` to FK: Over-engineering for a field that should be removed.

### Decision 3: Keep `title` field, sync with `headline`
**Choice**: Keep `title` on the model but add sync logic: when one is saved and the other is empty, populate the empty field.

**Rationale**: User explicitly requested keeping title as editable. Sync ensures consistency without forcing users to enter the same information twice.

**Alternatives considered**:
- Remove `title` entirely: Simpler but contradicts user preference.
- Make them the same field: Loses the distinction between "professional title" (for classification) and "headline" (for display).

### Decision 4: Simple tag selection for profiles
**Choice**: Remove must/nice distinction from profile side. All tags saved with `tag_type='nice'`. Wall filtering matches regardless of type.

**Rationale**: The must/nice distinction doesn't make sense for a profile that wants to be hired. Profiles just say "I have these skills." The wall's searcher-side distinction still works.

**Alternatives considered**:
- Keep must/nice in UI but ignore in backend: Confusing UX.
- Remove `tag_type` field entirely: Would require migration and break existing data.

### Decision 5: Implement skills modal JS from scratch
**Choice**: Write new JavaScript functions in `dashboard.js` rather than reusing `wall.js` code.

**Rationale**: The dashboard and wall have different requirements (edit vs search, pre-populate vs empty state). Copying would create maintenance overhead.

**Alternatives considered**:
- Shared utility functions: Over-abstracting for two different use cases.
- Reusing wall.js directly: Wrong context (search vs edit).

## Risks / Trade-offs

**[Risk] Data migration failure**: Removing `sector_name` requires running migration. If migration fails, profiles lose sector data.
→ Mitigation: Migration copies data to FK before dropping field. Backup strategy: `python manage.py dumpdata` before migration.

**[Risk] Skills modal complexity**: Full JS implementation is the largest change. Could introduce bugs in cascading dropdowns or tag search.
→ Mitigation: Reference implementation in `wall.js` for hierarchy loading. Test each function independently.

**[Risk] Wall tag filtering behavior change**: Profiles with tags saved as 'nice' will now match must-tag searches. This changes search results.
→ Mitigation: This is the intended behavior per user request. Document in changelog.

**[Risk] Registration form changes**: New users won't have title set. Existing users without sector FK get default "tecnologia".
→ Mitigation: Both fields are optional and editable from dashboard. Default sector ensures visibility in wall.

## Migration Plan

1. **Pre-migration**: Run `python manage.py dumpdata` for backup
2. **Branch 3 (data model)**: 
   - Create migration that copies `sector_name` to `sector` FK (default: "tecnologia")
   - Create migration that copies `title` to `headline` where headline is empty
   - Drop `sector_name` field
3. **Post-migration**: Verify all profiles have sector FK set
4. **Rollback**: Restore from dumpdata if issues arise

## Open Questions

None. All design decisions have been resolved based on user requirements.
