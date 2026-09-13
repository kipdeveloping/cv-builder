## Context

The codebase currently contains a full CV/resume builder in `apps/resumes` with:
- Models: `Resume`, `Template`, `SectorTag`, `ResumeTag`
- Views: Template selection, visual editor (contenteditable), auto-save API, publish API
- Templates: Editor, template gallery, 11 template partials
- Static JS: `editor.js` (319 lines), `publish.js` (131 lines)
- Fixtures: 3 templates, 4 sectors

The `apps/accounts` app has `Skill`/`UserSkill` models for skills management, and `UserProfile` with FKs to `resumes.SectorTag` and `resumes.Resume` (resume_destacado).

The `apps/wall` app displays published CVs via `wall_api_view` querying `Resume.objects.filter(status='published')`.

Product direction: shift to profile-only model (LinkedIn-style). Remove all CV/resume complexity. Keep profile management, add public/private toggle for wall visibility.

## Goals / Non-Goals

**Goals:**
- Remove `apps/resumes` entirely (models, views, URLs, templates, static, fixtures, migrations)
- Remove `Skill`/`UserSkill` models from `accounts`
- Move `SectorTag` to `accounts` for future filtering
- Add `is_public` and `sector_name` to `UserProfile`
- Registration wizard saves `title` + `sector_name` directly to profile
- Talent wall queries public `UserProfile` objects instead of published `Resume` objects
- Dashboard: remove "Mis CVs" modal; add visibility toggle in sidebar
- Public profile (`/candidato/<id>/`) works with `is_owner=False`, reads from profile JSON fields
- Data migration cleans up resume tables

**Non-Goals:**
- Reimplementing skills system (placeholder only, capability reserved)
- Changing auth, registration wizard steps, OAuth flow
- Changing dashboard layout, modals for experience/projects/social/work-prefs
- Changing wall UI beyond API response adaptation
- Internationalization changes

## Decisions

### 1. Sector storage: CharField on UserProfile vs FK to SectorTag

**Decision**: Store `sector_name` as CharField on `UserProfile`. Keep `SectorTag` model in `accounts` for future filtering UI.

**Rationale**: 
- Registration wizard currently uses free-text input for sector (not select)
- Simpler migration: no need to create/link SectorTag on registration
- SectorTag in accounts enables future type-ahead / select without coupling to resumes app
- Free text allows any sector; SectorTag provides canonical list for filters later

**Alternatives considered**:
- FK to SectorTag on registration: requires create-or-get SectorTag, adds complexity, doesn't match current UX (free text)
- JSONField for multiple sectors: overkill for MVP, single sector per profile is current model

### 2. Experience/Projects storage: JSONFields on UserProfile

**Decision**: Add `experience` and `projects` JSONFields to `UserProfile` (default=list). Dashboard modals read/write these fields directly.

**Rationale**:
- Matches existing pattern: `Resume.content` was JSONField with same structure
- Minimal schema change: no new models, no joins
- Dashboard JS already handles JSON serialization for these fields
- Profile view already expects this structure (reads from `featured_resume.content`)

**Alternatives considered**:
- Separate `Experience`/`Project` models with FK to UserProfile: more normalized, but requires new models, migrations, queries; overkill for current array-of-objects usage
- Keep in Resume model: not possible, Resume is being deleted

### 3. Skills system: complete removal with placeholder capability

**Decision**: Drop `Skill` and `UserSkill` tables entirely. Reserve `profile/skills` capability for future tag/filter system.

**Rationale**:
- User explicitly requested "delete it all" for skills
- Current skills tied to resume sync (`sync_skills_from_resume`) which is being removed
- Future system will be tag-based (not profile-skills), so clean break is better than partial migration

**Alternatives considered**:
- Keep models, hide UI: leaves dead code, confusing for future developers
- Migrate skills to profile JSONField: same complexity as new models, not requested

### 4. Visibility toggle: dedicated endpoint vs reusing update-profile

**Decision**: New dedicated endpoint `POST /accounts/toggle-visibility/`

**Rationale**:
- Semantically distinct from profile field updates
- Allows specific validation: "photo required to go public"
- Clearer API contract for frontend
- Avoids overloading `update_profile_fields` with special logic

**Alternatives considered**:
- Add `is_public` to `update_profile_fields` payload: simpler but mixes concerns; photo validation would need special handling

### 5. Wall API response shape: adapt existing or new format

**Decision**: Adapt existing `wall_api_view` to return profile-shaped data with same key names where possible (`user_id`, `name`, `bio`, `photo`, `tags`→`sector_name`)

**Rationale**:
- `wall.js` expects `user_id` for navigation to `/candidato/<user_id>/` (already correct)
- Minimal JS changes: rename `cv.template` → remove, `cv.tags` → `profile.sector_name`
- Backward compatible for wall.js card click behavior

**Alternatives considered**:
- New API endpoint with new response shape: more work, wall.js would need larger rewrite
- Keep CV shape with nulls: confusing, leaks removed concepts

### 6. Data migration strategy: delete resume tables after schema migration

**Decision**: 
1. Schema migrations first (add fields, remove FKs, create SectorTag in accounts, drop Skill/UserSkill)
2. Then data migration: `DELETE FROM resumes_resumetag; DELETE FROM resumes_resume; DELETE FROM resumes_template;`
3. Finally drop `resumes` app migrations

**Rationale**:
- Django requires models to exist for FK removal migrations
- Data cleanup before table drop avoids FK constraint errors
- Order: accounts migrations → resumes migrations → data cleanup → drop app

**Alternatives considered**:
- `RunSQL` in same migration as model deletion: risky if constraints not handled
- Keep data for rollback: not needed, this is a directional product change

### 7. Public profile access control: 404 for private profiles

**Decision**: Return 404 (not 403) when accessing `/candidato/<id>/` for private profile.

**Rationale**:
- Prevents user enumeration (attacker can't distinguish "user exists but private" vs "user doesn't exist")
- Consistent with "profile doesn't exist on wall" mental model
- Simple implementation: `get_object_or_404(UserProfile, user__id=id, is_public=True)`

**Alternatives considered**:
- 403 with "profile is private": leaks existence
- Redirect to wall: confusing UX

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| **Data loss**: Existing resume content deleted | Confirm with stakeholders; this is intentional per requirements. No rollback needed. |
| **Broken links**: External links to `/cv/<id>/` or `/editor/<id>/` will 404 | Acceptable - product pivot. Could add redirect middleware later if needed. |
| **SectorTag migration**: Moving model between apps | Use `SeparateDatabaseAndState` or `RunSQL` to rename table `resumes_sectortag` → `accounts_sectortag` preserving data. Fixtures reload handles initial data. |
| **Skill/UserSkill data loss**: Skills deleted | Confirmed intentional. No migration needed. |
| **Wall API breaking changes**: Frontend expects certain fields | Adapt `wall.js` in same commit; test wall page end-to-end |
| **Registration wizard sector**: Free text vs future select | Current UX is free text; SectorTag in accounts enables future type-ahead without breaking change |
| **Photo requirement for public toggle**: UX edge case | Toggle button disabled/hidden until photo uploaded; clear error message |
| **Dashboard JS refactoring**: Removing resume-dependent code | Incremental: remove `currentResumeId` usage first, then `saveExperienceData`/`saveSkills`/`setFeatured`, add `toggleProfileVisibility` |
| **OAuth pipeline**: `save_user_profile` references SectorTag import | Update import to `accounts.models.SectorTag`; sector not set via OAuth (free text only on registration) |

## Migration Plan

### Phase 1: Schema Migrations (in order)
```bash
# 1. Accounts: add is_public, sector_name; remove sector FK, resume_destacado FK
python manage.py makemigrations accounts --name add_visibility_and_sector_name

# 2. Accounts: create SectorTag model (moved from resumes)
python manage.py makemigrations accounts --name create_sectortag

# 3. Accounts: remove Skill, UserSkill models
python manage.py makemigrations accounts --name remove_skills

# 4. Resumes: delete Resume, Template, ResumeTag, SectorTag (now in accounts)
python manage.py makemigrations resumes --name delete_resumes_models
```

### Phase 2: Apply Migrations
```bash
python manage.py migrate
```

### Phase 3: Data Cleanup
```bash
python manage.py shell -c "
from django.db import connection
with connection.cursor() as c:
    c.execute('DELETE FROM resumes_resumetag;')
    c.execute('DELETE FROM resumes_resume;')
    c.execute('DELETE FROM resumes_template;')
    # SectorTag data preserved in accounts_sectortag via table rename
"
```

### Phase 4: Code Changes (single commit per logical area)
1. Delete `apps/resumes/`, `fixtures/templates.json`, `templates/resumes/`, `static/js/editor.js`, `static/js/publish.js`
2. Update `settings.py`, `urls.py` (remove resumes)
3. Update `accounts/models.py`, `forms.py`, `pipeline.py`, `views.py`, `urls.py`
4. Update `wall/views.py`, `urls.py`
5. Update templates: `dashboard.html`, `profile.html`
6. Update static JS: `dashboard.js`, `wall.js`

### Phase 5: Verify
- Run test suite (if any)
- Manual test: register → dashboard → toggle visibility → wall → profile view
- Check no 500 errors from removed imports

### Rollback Strategy
- Git revert commits
- Database: `python manage.py migrate accounts 0001` (before new fields), `python manage.py migrate resumes 0001` (restore resumes models)
- Data: Not recoverable without backup (intentional)

## Open Questions

1. **Default avatar SVG**: `wall.js` references `/static/img/default-avatar.svg` which doesn't exist. Templates use inline SVG fallback. Decision: Remove the reference in `wall.js` and rely on template fallback? Or create the static file? → Remove reference (templates handle it).

2. **Experience/Projects JSONField defaults**: Should `default=list` use `lambda: []` or `list`? → Use `default=list` (callable) to avoid mutable default bug.

3. **SectorTag table rename**: Use Django's `RenameTable` operation or raw SQL? → `RunSQL` with `ALTER TABLE resumes_sectortag RENAME TO accounts_sectortag` (SQLite compatible) or `SeparateDatabaseAndState`.

4. **Wall sector filtering**: Filter by `sector_name` (free text) or join `SectorTag`? → Start with `sector_name__icontains` on UserProfile; SectorTag in accounts provides canonical list for filter chips UI. Join later when filter UX matures.

5. **Photo validation on toggle**: Check in view or model clean()? → View-level check in `toggle_profile_visibility` for immediate API feedback.