## 1. Pre-implementation: Branch Cleanup

- [x] 1.1 Delete local branches except main (fix/clean-dead-code-and-lint, fix/refactor-profile-pending-tasks, refactor/profile-only-mode, test/alfredo) and verify only main remains

## 2. Branch 1: cleanup/resume-references

- [x] 2.1 Delete static/css/editor.css (orphaned #cv-container selectors) and verify file is removed
- [x] 2.2 Delete static/css/templates/classic.css, modern.css, creative.css (orphaned .cv-container) and verify files are removed
- [x] 2.3 Clean static/js/i18n.js: remove "Crear CV" and "crea un CV primero" translation keys from all 12 languages and verify keys are removed
- [x] 2.4 Remove test_no_published_cv_shows_message from apps/accounts/tests.py and verify test file runs without errors
- [x] 2.5 Delete openspec/specs/resumes/ directory (cv-templates, resume-editor, resume-publishing) and verify directory is removed
- [x] 2.6 Run python manage.py check and python manage.py test to verify no errors
- [x] 2.7 Commit changes with message "cleanup: remove orphaned resume/CV references"

## 3. Branch 2: fix/work-preferences-context

- [x] 3.1 Update apps/accounts/views.py dashboard_view to pass EMPLOYMENT_TYPE_CHOICES as employment_types in context and verify template receives the variable
- [x] 3.2 Run python manage.py check and python manage.py test to verify no errors
- [x] 3.3 Commit changes with message "fix: pass employment_types to dashboard template context"

## 4. Branch 3: refactor/data-model-cleanup

- [x] 4.1 Remove sector_name field from UserProfile in apps/accounts/models.py and verify model loads correctly
- [x] 4.2 Run python manage.py makemigrations accounts to generate migration for field removal
- [x] 4.3 Create data migration to set sector=SectorTag(slug='tecnologia') for all profiles where sector IS NULL
- [x] 4.4 Remove title field from UserProfile in apps/accounts/models.py and verify model loads correctly
- [x] 4.5 Run python manage.py makemigrations accounts to generate migration for field removal
- [x] 4.6 Create data migration to copy title to headline where headline is empty
- [x] 4.7 Run python manage.py migrate to apply all migrations and verify database state
- [x] 4.8 Fix save_profile_tags_view in apps/accounts/views.py: change SectorRol.objects.get(slug=data['rol']) to SectorRol.objects.get(slug=data['rol'], sector__slug=data['sector']) and fix RolEspecialidad similarly
- [x] 4.9 Fix wall location filter in apps/wall/views.py: add location parameter handling and filter by location_flex
- [x] 4.10 Remove sector_name fallback from wall API response in apps/wall/views.py line 132
- [x] 4.11 Run python manage.py check and python manage.py test to verify no errors
- [x] 4.12 Commit changes with message "refactor: clean data model - remove sector_name, fix slug uniqueness, fix location filter"

## 5. Branch 4: fix/registration-sector-dropdown

- [x] 5.1 Update WizardRegistrationForm in apps/accounts/forms.py: change sector from CharField(TextInput) to CharField(Select) with SectorTag choices and verify form loads
- [x] 5.2 Update WizardRegistrationForm.save(): change profile.sector_name to profile.sector = SectorTag.objects.get(slug=sector_slug) and remove profile.title assignment
- [x] 5.3 Update register_view in apps/accounts/views.py to pass SectorTag.objects.all() as sectors to template context
- [x] 5.4 Update templates/accounts/register.html step 3: replace sector text input with select dropdown and remove title input
- [x] 5.5 Run python manage.py check and python manage.py test to verify no errors
- [x] 5.6 Commit changes with message "fix: use sector dropdown in registration, remove title from step 3"

## 6. Branch 5: fix/wall-tag-filtering

- [x] 6.1 Update wall_api_view in apps/wall/views.py: change must-tag filter to match profiles that have the tag regardless of tag_type and verify filter works
- [x] 6.2 Update scoring in wall_api_view: match tags regardless of tag_type for relevance calculation and verify scoring works
- [x] 6.3 Run python manage.py check and python manage.py test to verify no errors
- [x] 6.4 Commit changes with message "fix: update wall tag filtering to match regardless of tag_type"

## 7. Branch 6: feat/dashboard-skills-modal

- [x] 7.1 Add API URLs to dashboard.html urls dict: getProfileTags, saveProfileTags, tagHierarchy, allTags
- [x] 7.2 Implement loadHierarchy() in dashboard.js: fetch /api/tags/hierarchy/ and store locally
- [x] 7.3 Implement populateSkillsSectorDropdown(preselectedSlug?) in dashboard.js: fill sector select with hierarchy data
- [x] 7.4 Implement populateSkillsRolDropdown(sectorSlug, preselectedSlug?) in dashboard.js: fill rol select based on sector
- [x] 7.5 Implement populateSkillsEspecialidadDropdown(sectorSlug, rolSlug, preselectedSlug?) in dashboard.js: fill especialidad select
- [x] 7.6 Implement openSkillsModal() in dashboard.js: open modal + fetch /accounts/api/profile/tags/ + populate all fields
- [x] 7.7 Implement loadAllTags() in dashboard.js: fetch /api/tags/all/ for tag search
- [x] 7.8 Implement searchTags(query) in dashboard.js: filter tags by name, show suggestions
- [x] 7.9 Implement addTag(slug, name) and removeTag(slug) in dashboard.js: manage tag chips
- [x] 7.10 Implement addLanguage() and removeLanguage(code) in dashboard.js: manage language chips
- [x] 7.11 Implement saveSkills() in dashboard.js: POST to /accounts/api/profile/tags/save/ with all selections
- [x] 7.12 Add event listeners for cascading dropdowns, tag search, language add/remove in dashboard.js
- [x] 7.13 Update dashboard.html skills modal: remove must/nice tag sections, add single tag section, add title input
- [x] 7.14 Add title and languages display to dashboard.html sidebar
- [x] 7.15 Change dashboard.html skills section "Editar" button onclick to call openSkillsModal()
- [x] 7.16 ~~Add title sync logic to update_profile_fields_view~~ N/A: title field was removed in branch 3
- [x] 7.17 Run python manage.py check and python manage.py test to verify no errors
- [x] 7.18 Commit changes with message "feat: implement dashboard skills modal with hierarchy, tags, languages, title"

## 8. Post-implementation: Final Verification

- [x] 8.1 Run full test suite: python manage.py test and verify all tests pass (6 pre-existing failures remain, unchanged)
- [x] 8.2 Run python manage.py check and verify no system check errors
- [x] 8.3 Verify all 6 branches are merged to main in correct order
- [x] 8.4 Verify no merge conflicts exist
