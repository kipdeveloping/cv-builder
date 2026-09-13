## Why

The `refactor-profile-only-mode` change successfully removed the `apps/resumes` app and migrated to a profile-only model, but left behind orphaned code references. The `dashboard.js` still calls deleted endpoints (`/api/resume/save/`), `profile.html` references `featured_resume.content.*` fields that no longer exist, and `wall.js` references a missing static file. These dead references cause runtime errors when users try to save experience, projects, social links, or skills from the dashboard.

## What Changes

- Remove `fixtures/templates.json` (orphaned resume template fixture)
- Clean `dashboard.js`: remove `currentResumeId`, `saveSkills()`, `setFeatured()`, `saveExperienceData()`, `saveSocialLinks()` logic that calls deleted `/api/resume/save/` endpoint; redirect these functions to use `urls.updateProfile` instead
- Clean `profile.html`: remove all `featured_resume.content.*` template blocks (education, languages, certifications, volunteering, awards, publications, interests, references)
- Clean `wall.js`: replace `/static/img/default-avatar.svg` reference with inline SVG fallback
- Clean `forms.py`: remove dead `_get_or_create_sector()` method
- Skip dashboard.html title change (per user request, "CV Builder" kept as placeholder)

## Capabilities

### New Capabilities

None - this is a pure cleanup refactor.

### Modified Capabilities

None - no behavior changes, only dead code removal.

## Impact

**Files modified:**
- `static/js/dashboard.js` - remove CV-dependent save logic, wire to profile endpoint
- `templates/accounts/profile.html` - remove 18 `featured_resume.content.*` references
- `static/js/wall.js` - fix default avatar fallback
- `apps/accounts/forms.py` - remove dead method
- `fixtures/templates.json` - deleted

**Risk:** Low. All changes remove dead code or fix broken references. No new behavior introduced.
