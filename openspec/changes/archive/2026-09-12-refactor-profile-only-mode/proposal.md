## Why

The current codebase includes a full CV/resume builder (`apps/resumes`) with template selection, editor, publishing, and talent wall display. The product direction has shifted to a profile-only model where users maintain a professional profile (similar to LinkedIn) instead of creating multiple CVs. The CV functionality is unused and adds significant complexity. Removing it simplifies the codebase, reduces maintenance burden, and aligns with the new product vision.

## What Changes

- **BREAKING**: Delete entire `apps/resumes` (models, views, URLs, templates, fixtures, migrations)
- **BREAKING**: Remove `resumes` from `INSTALLED_APPS` and root URL config
- **BREAKING**: Delete `Skill` and `UserSkill` models from `accounts` (skills system will be rebuilt later as tags/filters)
- **BREAKING**: Remove `sector` FK (`resumes.SectorTag`) and `resume_destacado` FK (`resumes.Resume`) from `UserProfile`
- Add `is_public` BooleanField to `UserProfile` — controls visibility on talent wall
- Add `sector_name` CharField to `UserProfile` — stores sector as free text (from registration wizard)
- Move `SectorTag` model from `resumes` to `accounts` — for future profile filtering
- Update registration wizard to save `title` and `sector_name` directly on `UserProfile`
- Add `toggle_profile_visibility` endpoint in `accounts` — POST toggles `is_public`
- Rewrite `wall_api_view` to query public `UserProfile` objects instead of published `Resume` objects
- Remove `cv_detail_view` from wall (wall cards navigate to `/candidato/<user_id>/` which uses existing `profile_view`)
- Remove CV-related templates: `templates/resumes/` (editor, select_template, 11 partials)
- Remove CV-related static JS: `editor.js`, `publish.js`
- Update `dashboard.html`: remove "Mis CVs" modal; add public/private toggle in sidebar
- Update `dashboard.js`: remove resume-dependent logic (`currentResumeId`, `saveExperienceData`, `saveSkills`, `setFeatured`); add `toggleProfileVisibility()`
- Update `wall.js`: adapt to profile-based API response; remove `default-avatar.svg` reference
- Update `profile.html`: remove `featured_resume.content.*` references; works for public view with `is_owner=False`
- Data migration: delete all `resumes_resume`, `resumes_template`, `resumes_resumetag` records

## Capabilities

### New Capabilities
- `profile/visibility`: User can toggle profile public/private; only public profiles appear on talent wall

### Modified Capabilities
- `accounts/user-profile`: Profile no longer references Resume or SectorTag FK; stores sector_name and title directly; adds is_public flag
- `accounts/registration`: Registration wizard saves sector_name and title to profile (no longer creates SectorTag via resumes app)
- `wall/wall`: Talent wall displays public profiles instead of published CVs; filtering by sector_name
- `profile/dashboard`: Dashboard manages profile only (no CV management); includes visibility toggle
- `profile/public-profile`: Public profile view (`/candidato/<id>/`) shows profile data without edit controls
- `profile/skills`: **REMOVED** — Skill/UserSkill models deleted; will be reimplemented later as tag/filter system

## Impact

**Code removed**: `apps/resumes/` (entire app), `templates/resumes/`, `static/js/editor.js`, `static/js/publish.js`, `fixtures/templates.json`

**Code modified**: 
- `apps/accounts/models.py`, `forms.py`, `pipeline.py`, `views.py`, `urls.py`
- `apps/wall/views.py`, `urls.py`
- `crud_cvs/settings.py`, `urls.py`
- `templates/accounts/dashboard.html`, `templates/accounts/profile.html`
- `templates/wall/wall.html` (minor JS variable changes)
- `static/js/dashboard.js`, `static/js/wall.js`

**Database**: 
- New fields: `UserProfile.is_public`, `UserProfile.sector_name`
- Removed FKs: `UserProfile.sector`, `UserProfile.resume_destacado`
- Removed models: `Skill`, `UserSkill`, `Resume`, `Template`, `ResumeTag`, `SectorTag` (moved to accounts)
- Data cleanup: delete all resume records

**APIs**: 
- Removed: `/api/resume/save/`, `/api/resume/publish/`, `/editor/<id>/`, `/select-template/`, `/create-resume/`
- Added: `POST /accounts/toggle-visibility/`
- Changed: `/api/wall/cvs/` now returns profiles; `/api/tags/` uses accounts.SectorTag