## 1. Project Setup

- [x] 1.1 Create Django project structure with manage.py, settings, and wsgi configuration
- [x] 1.2 Create apps directory with accounts, resumes, and wall app stubs
- [x] 1.3 Set up requirements.txt with Django, Pillow, crispy-forms, crispy-bootstrap5
- [x] 1.4 Initialize package.json with tailwindcss and @tailwindcss/cli dependencies
- [x] 1.5 Configure Tailwind CSS v4 build script in package.json
- [x] 1.6 Create static/src/input.css with Tailwind import and static/css/output.css target
- [x] 1.7 Set up base.html template with Tailwind output CSS link and language toggle placeholder
- [x] 1.8 Configure Django settings for static files, media, i18n, and apps
- [x] 1.9 Run npm build to verify Tailwind compilation works

## 2. User Authentication

- [x] 2.1 Create UserProfile model with OneToOneField to User, photo ImageField, and bio TextField
- [x] 2.2 Create RegistrationForm with email field and robust password validation (min 8, uppercase, number, special char)
- [x] 2.3 Create login.html template with email/password form styled with Tailwind
- [x] 2.4 Create register.html template with registration form and password validation feedback
- [x] 2.5 Implement login view with email backend and session management
- [x] 2.6 Implement register view with UserProfile auto-creation on successful registration
- [x] 2.7 Implement logout view with redirect to landing page
- [x] 2.8 Configure authentication URLs and protect private views with login_required
- [x] 2.9 Test registration, login, logout flow end-to-end

## 3. Dashboard and Photo Management

- [x] 3.1 Create dashboard.html template showing user's CVs and profile section
- [x] 3.2 Add photo upload form to dashboard with file validation (jpg/png/webp, max 5MB)
- [x] 3.3 Implement photo upload view with ImageField validation and resize (max 800x800)
- [x] 3.4 Display uploaded photo in dashboard and across the application
- [x] 3.5 Add bio edit field to dashboard with save functionality
- [x] 3.6 Show "Upload photo required before publishing" message when photo is missing
- [x] 3.7 Test photo upload, validation, and display flow

## 4. CV Templates

- [x] 4.1 Create Template model with name, slug, description, and thumbnail fields
- [x] 4.2 Create fixtures/templates.json with 3 pre-built templates (Classic, Modern, Creative)
- [x] 4.3 Create static/css/templates/classic.css with formal serif styling and left sidebar layout
- [x] 4.4 Create static/css/templates/modern.css with clean sans-serif styling and minimal layout
- [x] 4.5 Create static/css/templates/creative.css with bold colors and artistic layout
- [x] 4.6 Create template gallery HTML with 3 template cards showing thumbnails and descriptions
- [x] 4.7 Add template preview functionality on hover
- [x] 4.8 Load fixture data to populate templates in database
- [x] 4.9 Test template selection flow from gallery to editor

## 5. Resume Editor

- [x] 5.1 Create Resume model with user FK, template FK, status field, content JSONField, timestamps
- [x] 5.2 Create editor.html template with contenteditable regions and data-field attributes
- [x] 5.3 Implement JavaScript editor.js to collect form data from contenteditable elements
- [x] 5.4 Implement auto-save with 2-second debounce using setTimeout
- [x] 5.5 Add immediate save on blur events for contenteditable fields
- [x] 5.6 Create API endpoint POST /api/resume/save/ for JSON content storage
- [x] 5.7 Add CSRF token handling for AJAX requests (X-CSRFToken header)
- [x] 5.8 Display save feedback with timestamp ("Guardado a las 14:32")
- [x] 5.9 Implement experience section with add/remove/edit capabilities
- [x] 5.10 Implement education section with add/remove/edit capabilities
- [x] 5.11 Implement skills section with add/remove tag-style input
- [x] 5.12 Load existing CV content from JSON into editor on page load
- [x] 5.13 Test auto-save flow with network inspection and database verification

## 6. Publishing Workflow

- [x] 6.1 Create SectorTag model with name_es, name_en, and slug fields
- [x] 6.2 Create ResumeTag through model with is_primary field and unique constraint
- [x] 6.3 Create fixtures/sectors.json with default sector tags (Desarrollo Web, Diseno Grafico, Marketing, Finanzas)
- [x] 6.4 Create publish modal HTML with tag checkboxes and primary tag dropdown
- [x] 6.5 Implement publish.js to handle modal open, tag selection, and confirmation
- [x] 6.6 Create API endpoint POST /api/resume/publish/ with validation logic
- [x] 6.7 Implement validation: content exists, photo uploaded, at least one tag selected
- [x] 6.8 Implement one-CV-per-sector constraint (unpublish previous CV for same sector)
- [x] 6.9 Add publish button to editor (visible only for draft resumes)
- [x] 6.10 Test complete publishing flow from editor to talent wall appearance

## 7. Talent Wall

- [x] 7.1 Create wall.html template with grid layout for CV cards
- [x] 7.2 Design CV card component showing photo, name, and truncated bio
- [x] 7.3 Implement responsive grid (3-4 columns desktop, 1 column mobile)
- [x] 7.4 Add filter buttons for all sector tags plus "All" option
- [x] 7.5 Create API endpoint GET /api/wall/cvs/ with optional sector filter parameter
- [x] 7.6 Implement wall.js for AJAX filtering without page reload
- [x] 7.7 Add loading indicator during AJAX requests
- [x] 7.8 Implement CV detail view page showing complete resume
- [x] 7.9 Test wall display with multiple published CVs and filtering

## 8. Bilingual Support

- [x] 8.1 Configure Django i18n with LANGUAGES setting for Spanish and English
- [x] 8.2 Add LocaleMiddleware to Django settings
- [x] 8.3 Create locale/es/LC_MESSAGES/django.po with Spanish translations
- [x] 8.4 Create locale/en/LC_MESSAGES/django.po with English translations
- [x] 8.5 Add {% trans %} tags to all templates for translatable strings
- [x] 8.6 Implement language toggle button in navbar with [ES | EN] display
- [x] 8.7 Configure URL prefixes /es/ and /en/ for language routing
- [x] 8.8 Implement i18n.js for client-side dynamic string translation
- [x] 8.9 Update SectorTag display to use name_es/name_en based on current language
- [x] 8.10 Test language switching across all pages and verify CV content remains unchanged

## 9. Landing Page

- [x] 9.1 Create landing.html template with hero section and call-to-action
- [x] 9.2 Add product features section explaining CV builder capabilities
- [x] 9.3 Add CTA buttons for registration/login and talent wall access
- [x] 9.4 Style landing page with Tailwind CSS for professional appearance
- [x] 9.5 Add footer with links and copyright
- [x] 9.6 Test landing page display on different screen sizes

## 10. Security and Polish

- [x] 10.1 Implement content sanitization (strip HTML tags) for contenteditable input
- [x] 10.2 Add CSRF protection verification for all AJAX endpoints
- [x] 10.3 Implement image file type and size validation on upload
- [x] 10.4 Add error handling and user-friendly error messages throughout
- [x] 10.5 Test complete application flow: register, upload photo, create CV, publish, view on wall
- [x] 10.6 Verify bilingual functionality works correctly in both languages
- [x] 10.7 Run Django security checks and fix any issues
- [x] 10.8 Create README.md with setup instructions and project documentation
