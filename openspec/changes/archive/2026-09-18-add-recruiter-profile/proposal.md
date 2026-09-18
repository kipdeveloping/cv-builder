## Why

The platform currently only supports candidate profiles (job seekers). There is no way for companies or recruiters to register, post job vacancies, or manage talent acquisition. Adding a recruiter/empresa profile type enables the platform to serve both sides of the job market: candidates looking for work and companies looking for talent.

## What Changes

- Add role-based registration flow: users choose between "Busco Trabajo" (candidate) and "Busco Talento" (recruiter) during signup
- Create `RecruiterProfile` model (separate from `UserProfile`) with company-specific fields: company name, logo, sector, description, type, work modality, website
- Create `Vacancy` model for job postings with title, description, requirements, location, modality, salary range, employment type, and status
- Add corporate email validation for recruiter registrations (block generic email domains like gmail.com, yahoo.com, etc.)
- Limit OAuth providers for recruiters to Google Workspace and LinkedIn only (no GitHub)
- Create dedicated recruiter dashboard template with company identity, vacancy management, and social links
- Create visual-only "Create Vacancy" form (no backend functionality in this change)
- Add role field to `UserProfile` to distinguish between candidates and recruiters

## Capabilities

### New Capabilities
- `accounts/recruiter-profile`: Recruiter/empresa profile model, registration flow with role selection, corporate email validation, and role-specific OAuth restrictions
- `accounts/vacancy-management`: Vacancy model and recruiter dashboard interface for managing job postings
- `profile/recruiter-dashboard`: Dedicated dashboard layout for recruiters showing company identity, vacancy listings, and social links

### Modified Capabilities
- `accounts/registration`: Registration wizard changes from 3 steps to 4 steps with role selection as step 1, conditional fields based on role, and different OAuth button sets per role

## Impact

- **Models**: New `RecruiterProfile` and `Vacancy` models in `apps/accounts/models.py`
- **Forms**: New `RecruiterRegistrationForm`, modified `WizardRegistrationForm` to handle role selection
- **Views**: Modified `register_view` for role-based flow, new `recruiter_dashboard_view`, new `create_vacancy_view` (visual only)
- **Templates**: Modified `register.html` (4-step wizard), new `recruiter_dashboard.html`, new `create_vacancy.html`
- **JavaScript**: Modified `register.js` (role-dependent step logic), new `recruiter_dashboard.js`
- **Pipeline**: Modified `pipeline.py` to validate corporate email domains for recruiters
- **Admin**: Register new models in `apps/accounts/admin.py`
- **OAuth**: Login template modified to show different OAuth buttons based on selected role
