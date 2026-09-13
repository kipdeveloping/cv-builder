## 1. Database Migrations (Schema)

- [x] 1.1 Create accounts migration adding `is_public` (BooleanField, default=False) and `sector_name` (CharField, max_length=100, blank=True, default='') to UserProfile; verify `makemigrations accounts` generates correct operations
- [x] 1.2 Create accounts migration creating SectorTag model (moved from resumes); verify model has name_es, name_en, slug fields matching original
- [x] 1.3 Create accounts migration removing Skill and UserSkill models; verify `makemigrations accounts` generates DeleteModel operations
- [x] 1.4 Create accounts migration removing `sector` FK (to resumes.SectorTag) and `resume_destacado` FK (to resumes.Resume) from UserProfile; verify RemoveField operations
- [x] 1.5 Create resumes migration deleting Resume, Template, ResumeTag, SectorTag models; verify DeleteModel operations
- [x] 1.6 Apply all migrations with `python manage.py migrate`; verify no errors and database schema matches expected state
- [x] 1.7 Run data cleanup SQL to delete resume records: `DELETE FROM resumes_resumetag; DELETE FROM resumes_resume; DELETE FROM resumes_template;`; verify tables are empty
- [x] 1.8 Rename SectorTag table from `resumes_sectortag` to `accounts_sectortag` via RunSQL or SeparateDatabaseAndState; verify SectorTag data preserved and accessible via accounts app

## 2. Code Removal (Resumes App & Related)

- [x] 2.1 Delete `apps/resumes/` directory entirely; verify no import errors in remaining code
- [x] 2.2 Delete `fixtures/templates.json`; verify no fixture loading references
- [x] 2.3 Delete `templates/resumes/` directory (editor.html, select_template.html, 11 partials); verify no template references
- [x] 2.4 Delete `static/js/editor.js` and `static/js/publish.js`; verify no static references in templates
- [x] 2.4 Remove `'apps.resumes'` from `INSTALLED_APPS` in `crud_cvs/settings.py`; verify Django starts without errors
- [x] 2.5 Remove `path('', include('apps.resumes.urls'))` from `crud_cvs/urls.py`; verify URL resolution works
- [x] 2.6 Remove resumes imports from `apps/accounts/views.py` (Resume), `apps/accounts/forms.py` (SectorTag), `apps/wall/views.py` (Resume, SectorTag); verify no import errors

## 3. Accounts App Updates

- [x] 3.1 Update `apps/accounts/models.py`: add `is_public`, `sector_name` fields; remove `sector` FK, `resume_destacado` FK; move SectorTag model here; remove Skill, UserSkill models; verify model validates and migrations match 1.1-1.4
- [x] 3.2 Update `apps/accounts/forms.py` WizardRegistrationForm.save(): save `sector_name` directly to profile; update `_get_or_create_sector()` to use accounts.SectorTag; remove resumes import; verify registration wizard creates profile with title + sector_name
- [x] 3.3 Update `apps/accounts/pipeline.py` save_user_profile(): remove SectorTag import (or update to accounts.SectorTag); sector not set via OAuth; verify OAuth login works
- [x] 3.4 Add `toggle_profile_visibility` view in `apps/accounts/views.py`: POST only, toggles `request.user.profile.is_public`, validates photo exists when enabling, returns JSON with new state; verify endpoint works via curl/test
- [x] 3.5 Update `dashboard_view`: remove `featured_resume` logic, `Resume` queries; pass `profile.is_public` to template; add `experience`, `projects`, `social_links` from profile JSONFields (or empty defaults); verify dashboard loads without resume data
- [x] 3.6 Update `profile_view`: remove `featured_resume` fallback logic; read experience/projects/social_links from profile JSONFields directly; ensure works with `is_owner=False` for public view; verify public profile displays correctly
- [x] 3.7 Add `experience`, `projects`, `social_links` JSONFields to UserProfile model (default=list/dict); generate and apply migration; verify fields exist on profile
- [x] 3.8 Add `path('toggle-visibility/', views.toggle_profile_visibility, name='toggle_profile_visibility')` to `apps/accounts/urls.py`; verify URL resolves

## 4. Wall App Updates

- [x] 4.1 Rewrite `wall_api_view` in `apps/wall/views.py`: query `UserProfile.objects.filter(is_public=True).select_related('user')`; filter by `sector_name__icontains` if sector param; return profile data (id, user_id, name, bio, photo, sector_name, headline, title); verify API returns correct JSON structure
- [x] 4.2 Update `get_tags_api` to use `accounts.models.SectorTag`; verify tags API returns SectorTag data
- [x] 4.3 Remove `cv_detail_view` from `apps/wall/views.py`; verify no references remain
- [x] 4.4 Remove `path('cv/<int:resume_id>/', views.cv_detail_view, name='cv_detail')` from `apps/wall/urls.py`; verify URL config clean

## 5. Template Updates

- [x] 5.1 Update `templates/accounts/dashboard.html`: remove "Mis CVs" modal (lines 496-553); add visibility toggle in sidebar near status badges; remove `currentResumeId`, `featured_resume.content`, `dashboardContent`, `experienceData`, `projectsData`, `socialLinksData` script variables; verify template renders without errors
- [x] 5.2 Update `templates/accounts/profile.html`: remove `featured_resume.content.*` references (education, languages, certifications, volunteering, awards, publications, interests, references); read experience/projects/social_links from profile JSONFields; ensure `is_owner=False` hides edit controls; verify public profile displays correctly
- [x] 5.3 Verify `templates/wall/wall.html` works with adapted API (no changes needed except JS variables updated in wall.js)

## 6. Static JS Updates

- [x] 6.1 Update `static/js/dashboard.js`: remove `currentResumeId`, `saveExperienceData()`, `saveSkills()`, `setFeatured()`, "Mis CVs" modal logic; modify `getFullContent()` to read/write profile JSONFields (experience, projects, social_links); add `toggleProfileVisibility()` calling `/accounts/toggle-visibility/`; update `saveExperience`/`saveProject`/`saveSocialLinks` to POST to profile save endpoint; verify dashboard modals work and persist data
- [x] 6.2 Update `static/js/wall.js`: rename `loadCVs`â†’`loadProfiles`, `renderCVs`â†’`renderProfiles`, `createCVCard`â†’`createProfileCard`; adapt `createProfileCard` to use `profile.sector_name`, `profile.headline`, `profile.title`, `profile.photo`; remove `cv.template`, `cv.tags` references; remove line 160 `/static/img/default-avatar.svg` reference; verify wall loads and cards navigate to `/candidato/<user_id>/`
- [x] 6.3 Verify `static/js/register.js` works unchanged (wizard registration)

## 7. Integration Verification

- [x] 7.1 Test full registration flow: complete 3-step wizard â†’ verify profile created with title + sector_name; verify `is_public=False` by default
- [x] 7.2 Test dashboard: load dashboard â†’ verify sidebar shows profile data, visibility toggle present, experience/project/social modals work, no "Mis CVs" modal
- [x] 7.3 Test visibility toggle: click toggle to public â†’ verify API call succeeds, `is_public=True` in DB, profile appears on wall; click toggle to private â†’ verify removed from wall
- [x] 7.4 Test photo requirement: toggle to public without photo â†’ verify error shown, toggle stays private; upload photo â†’ toggle to public succeeds
- [x] 7.5 Test wall: load `/tablon/` â†’ verify only public profiles shown; filter by sector â†’ verify filtering works; click card â†’ verify navigation to `/candidato/<user_id>/`
- [x] 7.6 Test public profile: visit `/candidato/<public_user_id>/` â†’ verify profile displays with sidebar + main area, no edit controls, contact form works; visit `/candidato/<private_user_id>/` â†’ verify 404
- [x] 7.7 Test owner profile: authenticated user visits own `/candidato/<own_id>/` â†’ verify "Este es tu perfil publico" banner and dashboard link shown
- [x] 7.8 Run Django test suite (if any): `python manage.py test` â†’ verify no regressions
- [x] 7.9 Check for any remaining `resumes` references in codebase: `grep -r "resumes" --include="*.py" .` â†’ verify only in migrations/historical files


