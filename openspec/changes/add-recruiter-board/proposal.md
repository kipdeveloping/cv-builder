## Why

The talent wall currently only displays candidate (trabajador) profiles. Companies and recruiters also have public profiles via `RecruiterProfile`, but there is no way for visitors to discover them. This change adds a separate wall for recruiter/company profiles, keeping the two profile types differentiated and discoverable.

## What Changes

- **Dropdown in navbar**: The "Tablón" button becomes a dropdown with two options: "Para trabajadores" (existing wall) and "Para reclutadores" (new wall).
- **New recruiter wall page**: A separate wall at `/tablon-empresas/` that displays public `RecruiterProfile` entries with faceted filtering (sector, modality, company type).
- **New recruiter wall API**: A GET endpoint at `/api/wall/recruiters/` returning filtered `RecruiterProfile` data as JSON.
- **New recruiter public profile page**: A public profile view at `/empresa/<user_id>/` showing company details and active vacancies.
- **Recruiter profile view**: A new view in `accounts` to render the public company profile page.

## Capabilities

### New Capabilities
- `wall/recruiter-wall`: The recruiter/company wall functionality including the wall page, faceted filtering API, and public company profile view.

### Modified Capabilities
None. The existing `wall/talent-wall` and `wall/wall` specs remain unchanged. The navbar modification is a minor UI change captured within the new capability.

## Impact

- `templates/base.html` - navbar dropdown modification
- `apps/wall/views.py` - new `recruiter_wall_view` and `recruiter_wall_api_view`
- `apps/wall/urls.py` - new URL patterns
- `templates/wall/recruiter_wall.html` - new template
- `static/js/recruiter_wall.js` - new JS file
- `apps/accounts/views.py` - new `recruiter_profile_view`
- `apps/accounts/urls.py` - new URL pattern
- `templates/accounts/recruiter_profile.html` - new template
