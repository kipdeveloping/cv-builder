## Why

The project underwent a major refactor that removed the CV/resume feature (`apps/resumes`) but left behind orphaned code references, broken UI components, and inconsistent data model decisions. The dashboard's "Mis Habilidades" (skills) modal is completely non-functional — the `saveSkills()` function doesn't exist, dropdowns are never populated, and API endpoints are orphaned. Additionally, the `sector_name` legacy field creates confusion with the `sector` FK, the `title` field is set during registration but never displayed, and the work preferences modal renders empty because `employment_types` is never passed to the template context.

## What Changes

- **Remove orphaned resume/CV references**: Delete dead CSS files (editor.css, template CSS), clean CV translation keys from i18n.js, remove broken test, delete orphaned openspec specs
- **Fix work preferences**: Pass `EMPLOYMENT_TYPE_CHOICES` to dashboard template context so employment type checkboxes render
- **Clean data model**: Remove `sector_name` field (migrate existing users to "tecnologia" sector), remove `title` field (migrate to `headline`), fix `save_profile_tags_view` slug uniqueness bug, fix wall `location` filter
- **Simplify profile tags**: Replace must/nice tag distinction with simple tag selection — profiles just select tags from the global dictionary, which determine under which filters they appear in the wall
- **Update registration**: Replace free-text sector input with dropdown from hierarchy, remove title from step 3
- **Implement dashboard skills modal**: Full JavaScript implementation — hierarchy loading, cascading dropdowns, tag search/autocomplete, language chips, title editing, save functionality
- **Delete orphaned resume specs**: Remove `openspec/specs/resumes/` directory

## Capabilities

### New Capabilities

None — this is cleanup and fixes to existing functionality.

### Modified Capabilities

- `accounts/user-profile`: Remove `sector_name` field, keep `title` with headline sync, fix slug uniqueness in tag save endpoint
- `accounts/registration`: Replace free-text sector with dropdown, remove title from step 3
- `wall/talent-wall`: Update tag filtering to match profiles regardless of `tag_type`, fix `location` filter
- `profile/dashboard`: Implement skills modal JS, pass `employment_types` to context, add title/languages display
- `profile/skills`: Simplify tag selection from must/nice to single selector

## Impact

**Files modified:**
- `apps/accounts/models.py` — remove `sector_name` field
- `apps/accounts/views.py` — fix `dashboard_view`, `save_profile_tags_view`, `update_profile_fields_view`, `wall_api_view`, `register_view`
- `apps/accounts/forms.py` — update `WizardRegistrationForm`
- `apps/accounts/tests.py` — remove broken test
- `templates/accounts/dashboard.html` — update skills modal, add title/languages
- `templates/accounts/register.html` — sector dropdown, remove title
- `static/js/dashboard.js` — implement skills modal functions
- `static/js/i18n.js` — remove CV translation keys
- `static/js/wall.js` — no changes needed (wall filtering is backend-only)
- `static/css/editor.css` — deleted
- `static/css/templates/classic.css` — deleted
- `static/css/templates/modern.css` — deleted
- `static/css/templates/creative.css` — deleted
- `openspec/specs/resumes/` — deleted

**Database changes:** Migration required to remove `sector_name` field and migrate data.

**API changes:** None — existing endpoints remain, behavior updated.

**Breaking changes:** None — all changes are internal cleanup and fixes.
