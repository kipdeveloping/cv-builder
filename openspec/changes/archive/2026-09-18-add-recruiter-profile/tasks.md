## 1. Git Setup

- [x] 1.1 Create feature branch `feature/recruiter-profile` from main and verify branch exists with `git branch`

## 2. Models and Database

- [x] 2.1 Add RecruiterProfile model to apps/accounts/models.py with fields: user (OneToOne), company_name, company_logo, company_sector (FK to SectorTag), company_description, company_type, work_modality, company_website, is_public, social_links. Verify model is defined correctly.
- [x] 2.2 Add Vacancy model to apps/accounts/models.py with fields: recruiter_profile (FK), title, description, requirements (JSONField), location, modality, salary_range, employment_type, status, applications_count, created_at, updated_at. Verify model is defined correctly.
- [x] 2.3 Add role field to UserProfile model with choices 'candidate' and 'recruiter', default 'candidate'. Verify field is added.
- [x] 2.4 Add BLOCKED_EMAIL_DOMAINS list to crud_cvs/settings.py with blocked free email domains. Verify list is defined.
- [x] 2.5 Run `python manage.py makemigrations` and verify migration files are created.
- [x] 2.6 Run `python manage.py migrate` and verify migrations apply successfully.

## 3. Admin Registration

- [x] 3.1 Register RecruiterProfile in apps/accounts/admin.py with appropriate list_display, filters, and search fields. Verify registration.
- [x] 3.2 Register Vacancy in apps/accounts/admin.py with appropriate list_display, filters, and search fields. Verify registration.

## 4. Forms

- [x] 4.1 Create RecruiterRegistrationForm in apps/accounts/forms.py with fields: email, password1, password2, first_name, last_name, company_name, company_type, sector, work_modality, company_website, company_description. Verify form definition.
- [x] 4.2 Add corporate email validation to RecruiterRegistrationForm.clean_email that checks against BLOCKED_EMAIL_DOMAINS. Verify validation logic.
- [x] 4.3 Modify WizardRegistrationForm to handle role parameter and conditionally show fields based on role. Verify form handles both roles.

## 5. Registration Template and JavaScript

- [x] 5.1 Modify templates/accounts/register.html to add Step 1 with role selection buttons ("Busco Trabajo" / "Busco Talento"). Verify step 1 renders.
- [x] 5.2 Add Step 3 fields for recruiters: contact name, last name, company name, company type. Verify recruiter fields render.
- [x] 5.3 Add Step 4 fields for recruiters: sector dropdown, work modality, optional website/logo/description. Verify recruiter step 4 renders.
- [x] 5.4 Modify static/js/register.js to handle 4-step wizard with role-dependent step content. Verify wizard navigation works for both roles.
- [x] 5.5 Add role parameter to form submission and pass it to backend. Verify role is sent.

## 6. Views and URLs

- [x] 6.1 Modify register_view in apps/accounts/views.py to handle role-based registration flow. Verify both candidate and recruiter registration work.
- [x] 6.2 Add recruiter_dashboard_view in apps/accounts/views.py that queries RecruiterProfile and renders recruiter dashboard. Verify view returns correct template.
- [x] 6.3 Add create_vacancy_view in apps/accounts/views.py (visual only, renders form). Verify view returns form template.
- [x] 6.4 Add URL patterns for recruiter-dashboard and create-vacancy in apps/accounts/urls.py. Verify URLs are accessible.
- [x] 6.5 Modify dashboard_view to check user role and render appropriate template (candidate or recruiter). Verify role-based routing works.

## 7. OAuth Pipeline

- [x] 7.1 Modify apps/accounts/pipeline.py to handle recruiter OAuth flow. Verify pipeline creates RecruiterProfile for recruiter OAuth users.
- [x] 7.2 Add session variable handling for role during OAuth initiation. Verify role persists through OAuth flow.

## 8. Recruiter Dashboard Template

- [x] 8.1 Create templates/accounts/recruiter_dashboard.html with sidebar layout: company logo, name, sector, description, company data card. Verify sidebar renders.
- [x] 8.2 Add main area with vacancies section, "+ Crear Vacante" button, and vacancy list. Verify vacancies section renders.
- [x] 8.3 Add social links section with LinkedIn, Twitter, website. Verify social links render.
- [x] 8.4 Add public profile toggle. Verify toggle renders.
- [x] 8.5 Add edit modals for company description and social links. Verify modals open and close.

## 9. Recruiter Dashboard JavaScript

- [x] 9.1 Create static/js/recruiter_dashboard.js with modal functions (openModal, closeModal). Verify modals work.
- [x] 9.2 Add save functions for company description and social links (AJAX to update endpoint). Verify save functions are defined.
- [x] 9.3 Add public profile toggle functionality. Verify toggle sends POST request.

## 10. Create Vacancy Template (Visual Only)

- [x] 10.1 Create templates/accounts/create_vacancy.html with form fields: title, description, requirements, location, modality, salary_range, employment_type. Verify form renders.
- [x] 10.2 Style form with Tailwind CSS matching existing form patterns. Verify styling is consistent.
- [x] 10.3 Add back button to return to dashboard. Verify navigation works.

## 11. Login Template Modifications
- [x] 11.1 Modify templates/accounts/login.html to show role 
selection before OAuth buttons. Verify role selection appears.
- [x] 11.2 Conditionally show OAuth buttons based on selected role 
(Google+LinkedIn for recruiters, all for candidates). Verify conditional display works.
## 12. Verification

- [x] 12.1 Run `python manage.py test` and verify all tests pass.
- [x] 12.2 Run linting/typecheck commands if configured. Verify no errors.
- [x] 12.3 Manual test: complete candidate registration flow end-to-end. Verify candidate dashboard loads.
- [x] 12.4 Manual test: complete recruiter registration flow end-to-end. Verify recruiter dashboard loads.
- [x] 12.5 Manual test: verify corporate email validation blocks gmail.com for recruiters. Verify error message appears.
- [x] 12.6 Manual test: verify OAuth buttons are restricted for recruiters. Verify only Google and LinkedIn appear.
