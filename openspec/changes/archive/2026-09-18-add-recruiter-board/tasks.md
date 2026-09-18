## 1. Backend Views and API

- [x] 1.1 Add `recruiter_wall_view` to `apps/wall/views.py` that renders `wall/recruiter_wall.html`. Verify: view function exists and returns rendered template.

- [x] 1.2 Add `recruiter_wall_api_view` to `apps/wall/views.py` that returns filtered `RecruiterProfile` data as JSON. Support faceted filtering with `sector[]` (OR), `modality[]` (OR), and `company_type` parameters. Verify: API returns correct JSON structure with `id`, `user_id`, `company_name`, `company_logo`, `sector`, `company_type`, `work_modality`, `company_description`, `company_website`, `social_links`.

- [x] 1.3 Add `recruiter_profile_view` to `apps/accounts/views.py` that renders the public company profile page at `/empresa/<user_id>/`. Return 404 if profile doesn't exist or `is_public=false`. Verify: view returns 404 for non-existent or private profiles, renders template for public profiles.

## 2. URL Routing

- [x] 2.1 Add URL patterns to `apps/wall/urls.py`: `tablon-empresas/` for `recruiter_wall_view` and `api/wall/recruiters/` for `recruiter_wall_api_view`. Verify: `reverse('recruiter_wall')` and `reverse('recruiter_wall_api')` resolve correctly.

- [x] 2.2 Add URL pattern to `apps/accounts/urls.py`: `empresa/<int:user_id>/` for `recruiter_profile_view`. Verify: `reverse('recruiter_profile', args=[1])` resolves correctly.

## 3. Templates

- [x] 3.1 Create `templates/wall/recruiter_wall.html` based on `wall.html` structure. Include filter panel with: sector multi-select, modality checkboxes, company type radio. Include grid container for recruiter profile cards. Load `recruiter_wall.js`. Verify: template renders without errors at `/tablon-empresas/`.

- [x] 3.2 Create `templates/accounts/recruiter_profile.html` that displays: company logo, company name, sector, company type, work modality, company description, social links, and list of active vacancies. Verify: template renders company data correctly at `/empresa/<id>/`.

## 4. JavaScript

- [x] 4.1 Create `static/js/recruiter_wall.js` with: sector dropdown population from API, faceted filtering logic (AND between facets, OR within facets), recruiter profile card rendering (logo, name, sector, type, modality, description), click handler to navigate to `/empresa/<user_id>/`. Verify: wall loads public profiles, filters work correctly, card click navigates to profile.

## 5. Navbar Dropdown

- [x] 5.1 Modify `templates/base.html` to replace the single "Tablón" link with a dropdown containing "Para trabajadores" (`/tablon/`) and "Para reclutadores" (`/tablon-empresas/`). Add dropdown toggle behavior with CSS/JS. Verify: dropdown shows two options, each navigates to correct wall page.
