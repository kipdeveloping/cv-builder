## 1. Models & Migration

- [x] 1.1 Extend UserProfile model with headline, location_flex, search_status, availability, resume_destacado fields and verify migration generates correctly
- [x] 1.2 Create Skill model with name and slug fields and verify unique constraint
- [x] 1.3 Create UserSkill model with user FK, skill FK, is_primary fields and verify unique_together constraint
- [x] 1.4 Register new models in admin.py and verify admin site displays them
- [x] 1.5 Run makemigrations and migrate and verify database schema updates

## 2. Backend Views & URLs

- [x] 2.1 Add new URL patterns: candidato/<user_id>/, update-profile/, update-name/, set-featured/, contact/<user_id>/
- [x] 2.2 Rewrite dashboard_view to pass profile, skills, experience, projects, social_links, resumes to template
- [x] 2.3 Create profile_view for public profile page with featured resume fallback logic
- [x] 2.4 Create update_profile_fields view for headline, location_flex, search_status, availability updates
- [x] 2.5 Create update_name_view for first_name, last_name updates
- [x] 2.6 Create set_featured_resume view for resume_destacado assignment
- [x] 2.7 Create contact_email_view for sending contact emails via console backend
- [x] 2.8 Add ProfileOnboardingForm to forms.py for name collection

## 3. Skills Sync

- [x] 3.1 Create sync_skills_from_resume helper function that extracts skills from JSON
- [x] 3.2 Implement Skill record creation for new skill names
- [x] 3.3 Implement UserSkill record creation for new user-skill associations
- [x] 3.4 Implement UserSkill removal for skills no longer in any resume
- [x] 3.5 Preserve is_primary flag during sync operations
- [x] 3.6 Modify save_resume_api to call sync_skills_from_resume after save
- [ ] 3.7 Test sync with multiple resumes having different skills

## 4. Dashboard Template & JavaScript

- [x] 4.1 Create dashboard.html with 2-column responsive layout (sidebar 4/12 + main 8/12)
- [x] 4.2 Implement sidebar: photo with edit button, name, headline with edit button
- [x] 4.3 Implement sidebar: skills grid with edit button that opens modal
- [x] 4.4 Implement sidebar: bio with edit button that opens modal
- [x] 4.5 Implement sidebar: status badges with edit button that opens modal
- [x] 4.6 Implement sidebar: "Mis Curriculums" button that opens CV list modal
- [x] 4.7 Implement main area: experience/project carousel with navigation arrows
- [x] 4.8 Implement main area: "+ Agregar experiencia" button that opens modal with preview card
- [x] 4.9 Implement main area: edit button on each carousel card that opens modal pre-populated
- [x] 4.10 Implement main area: social links section with add/edit button
- [x] 4.11 Implement onboarding banner for users without first_name or last_name
- [x] 4.12 Create dashboard.js with modal open/close functions
- [x] 4.13 Implement saveName, saveHeadline, saveBio, saveStatus functions in dashboard.js
- [x] 4.14 Implement carousel navigation (nextSlide, prevSlide) in dashboard.js
- [x] 4.15 Implement CV list modal with star toggle for featured resume
- [x] 4.16 Implement experience/project card create/edit modal with preview
- [x] 4.17 Implement social links modal with platform URL inputs

## 5. Public Profile Template & JavaScript

- [x] 5.1 Create profile.html with same 2-column layout as dashboard but no edit controls
- [x] 5.2 Implement sidebar: read-only photo, name, headline, skills, bio, status badges
- [x] 5.3 Implement main area: read-only experience/project carousel without edit/delete buttons
- [x] 5.4 Implement main area: social links as clickable icons
- [x] 5.5 Implement "Contactar" button that opens contact form modal
- [x] 5.6 Implement owner detection with "Este es tu perfil publico" indicator
- [x] 5.7 Create profile.js with carousel navigation
- [x] 5.8 Implement contact form submission via fetch POST to /contact/<user_id>/

## 6. Wall Integration

- [x] 6.1 Modify wall_api_view to include user_id in CV response objects
- [x] 6.2 Modify wall.js createCVCard to navigate to /candidato/<user_id>/ instead of /cv/<id>/
- [x] 6.3 Add "Ver Perfil Completo" button to cv_detail.html template
- [x] 6.4 Verify wall cards correctly link to profile pages

## 7. Editor Extension (Optional)

- [x] 7.1 Extend collectFormData() in editor.js to include projects[] array
- [x] 7.2 Extend collectFormData() in editor.js to include social_links{} object
- [x] 7.3 Verify save_resume_api correctly stores projects and social_links in Resume.content

## 8. Settings & Configuration

- [x] 8.1 Add EMAIL_BACKEND = django.core.mail.backends.console.EmailBackend to settings.py
- [x] 8.2 Verify contact emails print to console in development

## 9. Testing & Verification

- [x] 9.1 Test dashboard loads correctly for authenticated user with profile data
- [x] 9.2 Test profile page loads correctly for public visitor
- [x] 9.3 Test skills sync works when saving resume with skills array
- [x] 9.4 Test featured resume toggle updates UserProfile.resume_destacado
- [x] 9.5 Test contact form sends email to console
- [x] 9.6 Test wall cards navigate to profile pages
- [x] 9.7 Test onboarding banner appears for users without name
- [x] 9.8 Test responsive layout on mobile and desktop viewports





















