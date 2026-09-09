## Why

The platform currently lacks a dedicated candidate profile page. Users can create and publish CVs, but there is no structured public-facing profile that showcases their professional identity beyond a single CV template. The dashboard is minimal (only photo and bio editing), and visitors on the wall can only view raw CV templates. We need a unified profile experience that:

1. Gives candidates a professional, structured public page with their identity, experience carousel, skills, and social links
2. Provides a rich dashboard for profile management with inline editing capabilities
3. Enables contact between visitors and candidates via email
4. Creates a discoverable skill taxonomy for filtering and search

## What Changes

- **Dashboard redesign**: Complete rewrite of `/dashboard/` with 2-column layout (sidebar + main area), inline edit modals for all profile fields, experience/project carousel with add/edit functionality, and social links management
- **New public profile page**: `/candidato/<user_id>/` showing the same content as the dashboard but without edit controls, with a contact form instead
- **New models**: `Skill` (reusable skill taxonomy) and `UserSkill` (user-skill association with primary flag) for structured skill data
- **UserProfile extension**: Add `headline`, `location_flex`, `search_status`, `availability`, and `resume_destacado` fields
- **Skills sync**: Automatic synchronization of JSON `skills[]` from Resume.content to relational `Skill`/`UserSkill` models on save
- **Wall integration**: CV cards on the wall link to candidate profiles instead of CV detail pages; CV detail page gains a "Ver Perfil" button
- **Contact system**: Email-based contact form on public profiles using Django's console email backend
- **Featured resume**: Users can designate one resume as their featured/default profile resume

## Capabilities

### New Capabilities

- `profile/dashboard`: Dashboard redesign with 2-column layout, inline edit modals, experience carousel, social links management, skills editing, status badges, and CV list modal
- `profile/public-profile`: Public candidate profile page at `/candidato/<user_id>/` with read-only view, contact form, and owner detection
- `profile/skills`: Skill taxonomy model (Skill) and user-skill association (UserSkill) with automatic sync from Resume.content JSON
- `profile/contact`: Email-based contact system for visitors to message candidates
- `wall/wall`: Wall API response includes `user_id`; CV card clicks navigate to profile; CV detail page includes "Ver Perfil" button

### Modified Capabilities

None.

## Impact

- **Models**: `apps/accounts/models.py` (UserProfile extension + 2 new models), `apps/accounts/admin.py` (register new models)
- **Views**: `apps/accounts/views.py` (6 new/modified views), `apps/wall/views.py` (API response modification)
- **URLs**: `apps/accounts/urls.py` (+5 routes)
- **Templates**: `templates/accounts/dashboard.html` (rewrite), `templates/accounts/profile.html` (new), `templates/wall/cv_detail.html` (add button)
- **JavaScript**: `static/js/dashboard.js` (new), `static/js/profile.js` (new), `static/js/wall.js` (modify), `static/js/editor.js` (extend collectFormData)
- **Settings**: `crud_cvs/settings.py` (EMAIL_BACKEND)
- **Forms**: `apps/accounts/forms.py` (+ProfileOnboardingForm)
- **APIs**: `apps/resumes/views.py` (save_resume_api skills sync)
