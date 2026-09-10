## Context

This is a greenfield Django project for building interactive CVs with a public talent wall. The project requires a full-stack architecture with Django backend, Tailwind CSS v4 frontend build, vanilla JavaScript for interactivity, and Django i18n for bilingual support. No existing codebase constraints apply.

## Goals / Non-Goals

**Goals:**
- Establish a clean Django project structure with 3 apps (accounts, resumes, wall)
- Implement a visual CV editor using contenteditable with auto-save
- Provide 3 distinct CV templates with mandatory photo integration
- Create a public talent wall with real-time AJAX filtering
- Support bilingual UI (Spanish/English) via Django i18n
- Use Tailwind CSS v4 with npm build for styling
- Implement robust security (password validation, CSRF, content sanitization)

**Non-Goals:**
- Social authentication (Google/GitHub) - reserved for future scaling
- Multiple CVs per sector - constraint is one CV per sector per user
- Auto-translation of CV content - users write in their preferred language
- Production deployment - this is a local development/GitHub repository project
- Advanced rich text editing - contenteditable with plain text only

## Decisions

### 1. Data Storage: JSONField for CV Content
**Decision**: Store all CV content as a single JSON object in Resume.content using Django's JSONField.

**Rationale**: The CV structure varies by template (different sections, different fields). JSON allows flexible schema without complex relational modeling. SQLite's JSON support is sufficient for this use case.

**Alternatives considered**:
- Separate models for Experience, Education, Skills: Rejected due to complexity and tight coupling to fixed section structure
- PostgreSQL JSONB: Rejected because project uses SQLite for simplicity

### 2. Photo Storage: UserProfile, Not Resume
**Decision**: Store profile photo in UserProfile (one photo per user), not in Resume (one per CV).

**Rationale**: User requested single photo for all CVs. Simpler storage, consistent branding across CVs. Photo is tied to user identity, not individual resume versions.

**Alternatives considered**:
- Photo per Resume: Rejected - user explicitly wanted one photo for all CVs
- External image service: Rejected - overkill for local development project

### 3. Editor Implementation: contenteditable + JavaScript
**Decision**: Use HTML contenteditable attributes with vanilla JavaScript for the visual editor, rather than a form-based approach or rich text library.

**Rationale**: Matches the "visual editor" requirement where users click directly on the CV to edit. No external dependencies. Full control over template rendering.

**Alternatives considered**:
- Form-based editor: Rejected - not visual enough, doesn't match "click to edit" requirement
- Rich text library (TinyMCE, Quill): Rejected - adds complexity, users need plain text editing only
- React/Vue component: Rejected - vanilla JS requirement per user preference

### 4. Auto-Save: Debounced AJAX with 2-Second Delay
**Decision**: Implement auto-save using JavaScript debounce (2 seconds of inactivity) with immediate save on blur events.

**Rationale**: Balances user experience (no lost work) with performance (not saving on every keystroke). Blur save ensures immediate persistence when user leaves a field.

**Alternatives considered**:
- Save on every keystroke: Rejected - too many server requests
- Manual save only: Rejected - risk of data loss, poor UX
- localStorage with periodic sync: Rejected - adds complexity, data not immediately server-persisted

### 5. Template Rendering: Static CSS Files
**Decision**: Maintain separate CSS files for each template (classic.css, modern.css, creative.css) loaded dynamically based on selected template.

**Rationale**: Templates have distinct visual styles that go beyond Tailwind utilities. Separate CSS files allow template-specific styling without bloating the main Tailwind output.

**Alternatives considered**:
- Tailwind-only styling: Rejected - some template effects (gradients, complex layouts) need custom CSS
- Template as Django includes: Rejected - templates need to be dynamically switchable in the editor
- JavaScript-rendered templates: Rejected - adds unnecessary complexity for static layouts

### 6. Bilingual Support: Django i18n with URL Prefixes
**Decision**: Use Django's built-in i18n framework with URL prefixes (/es/, /en/) and locale middleware for language switching.

**Rationale**: Standard Django approach, well-documented, integrates with templates via {% trans %} tags. URL prefixes make language persistent and SEO-friendly.

**Alternatives considered**:
- Query parameters (?lang=es): Rejected - less clean URLs, not standard Django practice
- Session-based language: Rejected - URLs not shareable, harder to debug
- Client-side translation only: Rejected - loses server-side template translation

### 7. Sector Tag Uniqueness: Through Model with is_primary
**Decision**: Use a ResumeTag through model with is_primary field and unique_together constraint on (user, sector_tag) to enforce one CV per sector.

**Rationale**: Allows multiple tags per CV while enforcing the sector uniqueness constraint. is_primary distinguishes the main sector for display purposes.

**Alternatives considered**:
- Simple M2M with unique constraint on (resume, sector): Rejected - doesn't enforce user-level uniqueness
- Separate Sector field on Resume: Rejected - limits to one sector per CV, no tagging flexibility

### 8. Tailwind Build: npm with @tailwindcss/cli
**Decision**: Use npm with @tailwindcss/cli for Tailwind CSS v4 compilation, with a build script in package.json.

**Rationale**: Standard approach for Tailwind v4, allows tree-shaking of unused utilities, produces optimized CSS output. npm is already available on the system.

**Alternatives considered**:
- CDN approach: Rejected as primary - user preferred build local for professional setup
- PostCSS integration: Rejected - @tailwindcss/cli is simpler for this project size

### 9. Authentication: Django Built-in with Email Backend
**Decision**: Use Django's built-in authentication system with email as the primary identifier, customizing the login form to use email instead of username.

**Rationale**: battle-tested, secure, integrates with Django's permission system. Email is more user-friendly than username for this application.

**Alternatives considered**:
- django-allauth: Rejected - overkill for email-only auth, adds dependencies
- Custom auth model: Rejected - unnecessary complexity, Django's auth is sufficient

### 10. Content Sanitization: Strip HTML Tags
**Decision**: Sanitize contenteditable input by stripping all HTML tags, allowing only plain text content.

**Rationale**: Prevents XSS attacks through user-generated content. contenteditable can produce inconsistent HTML; stripping ensures clean data storage.

**Alternatives considered**:
- Allow safe HTML tags: Rejected - adds complexity, users need plain text editing only
- Rich text validation: Rejected - overkill for this use case

## Risks / Trade-offs

**[Risk] contenteditable inconsistencies across browsers** → Mitigation: Test on major browsers (Chrome, Firefox, Safari), normalize input with text sanitization

**[Risk] JSONField query performance for filtering** → Mitigation: Talent wall filtering uses sector tags (indexed M2M), not JSON queries. CV content is loaded whole, not queried.

**[Risk] Tailwind build complexity for beginners** → Mitigation: Provide clear npm scripts, document build process in README, fallback to CDN if build fails

**[Risk] File upload security (photos)** → Mitigation: Validate file types, enforce size limits, use Django's ImageField validation, store outside web root

**[Risk] CSRF protection on AJAX calls** → Mitigation: Include X-CSRFToken header in all fetch requests, use cookie-based CSRF tokens

**[Race condition] Multiple tabs editing same CV** → Mitigation: Last-write-wins strategy, auto-save includes timestamp for conflict detection (future enhancement)

**[Trade-off] One CV per sector limit** → Accepted: User requirement. Simplifies talent wall discovery but limits user flexibility.

**[Trade-off] No rich text editing** → Accepted: Plain text contenteditable is simpler, more secure, and sufficient for CV content.
