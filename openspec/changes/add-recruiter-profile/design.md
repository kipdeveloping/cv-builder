## Context

The project is a Django-based CV/profile platform with Tailwind CSS for styling. It uses a single UserProfile model for all users, a 3-step registration wizard, and a single dashboard template. The system supports OAuth via Google, GitHub, and LinkedIn. See proposal.md for motivation.

Key constraints:
- Django 4+ with SQLite database
- Tailwind CSS for styling (no UI framework)
- Server-rendered templates with vanilla JavaScript
- django-social-auth for OAuth
- i18n support (Spanish/English)

## Goals / Non-Goals

**Goals:**
- Separate recruiter and candidate experiences with distinct profiles and dashboards
- Validate corporate email domains for recruiter registrations
- Restrict OAuth providers for recruiters (Google + LinkedIn only)
- Create visual-only vacancy management interface
- Maintain backward compatibility with existing candidate profiles

**Non-Goals:**
- Functional vacancy creation/submission (visual only in this change)
- Vacancy application tracking or candidate matching
- Payment or subscription features for recruiters
- Multi-language support for new recruiter-specific strings (will use i18n tags)

## Decisions

### Decision 1: Separate RecruiterProfile model (not extending UserProfile)

**Choice:** Create a new RecruiterProfile model with OneToOneField to User, separate from UserProfile.

**Alternatives considered:**
- Add role field to UserProfile with conditional fields: Rejected because it would add nullable fields to UserProfile that only apply to recruiters, creating data sparsity and confusion.
- Single table inheritance: Not natively supported in Django without third-party libraries.

**Rationale:** Clean separation of concerns. RecruiterProfile only contains company-specific fields. UserProfile remains focused on candidate data. The role field on UserProfile determines which model to query.

### Decision 2: Role field on UserProfile (not a separate UserRoles model)

**Choice:** Add a simple CharField `role` to UserProfile with choices 'candidate' and 'recruiter'.

**Alternatives considered:**
- Separate UserRoles model with ForeignKey: Overkill for two roles.
- Using Django groups: More complex than needed, harder to query.

**Rationale:** Simple, direct field on the existing profile. Easy to query and filter. Default value ensures existing users are candidates.

### Decision 3: Corporate email validation via blocked domains list

**Choice:** Maintain a BLOCKED_EMAIL_DOMAINS list in settings.py and validate in the registration form.

**Alternatives considered:**
- Regex-based corporate email detection: Fragile, hard to maintain.
- Third-party email validation service: Adds external dependency.
- Allowed domains list: Requires manual curation, impractical for open registration.

**Rationale:** Simple, maintainable, and effective. Blocking known free email providers catches 99% of personal emails. Can be extended by adding domains to the list.

### Decision 4: Separate recruiter_dashboard.html template

**Choice:** Create a new template `recruiter_dashboard.html` instead of modifying the existing dashboard.html with conditional blocks.

**Alternatives considered:**
- Single template with {% if role == 'recruiter' %} blocks: Would make the template complex and hard to maintain.
- Template inheritance with base dashboard: More complex than needed for two templates.

**Rationale:** Cleaner separation. Each dashboard template is focused on its role. Easier to maintain and modify independently.

### Decision 5: Vacancy model with JSONField for requirements

**Choice:** Use a JSONField for requirements to allow flexible, schema-less requirement lists.

**Alternatives considered:**
- Separate VacancyRequirement model: More normalized but adds complexity for a simple list.
- TextField with structured format: Harder to query and validate.

**Rationale:** JSONField is simple, flexible, and natively supported in Django. Requirements are display-only in this change, so complex querying is not needed.

### Decision 6: JavaScript pattern - global functions for onclick handlers

**Choice:** Follow existing pattern of assigning functions to `window` for inline onclick handlers in templates.

**Alternatives considered:**
- Event delegation with data attributes: More modern but diverges from existing codebase patterns.
- Alpine.js or htmx: Would add new dependencies.

**Rationale:** Consistency with existing codebase. The dashboard.js already uses this pattern extensively.

## Risks / Trade-offs

**Risk:** Existing users without role field may see incorrect dashboard
→ **Mitigation:** Default role value 'candidate' on UserProfile. Migration will set all existing profiles to 'candidate'.

**Risk:** OAuth flow may not pass role selection through the pipeline
→ **Mitigation:** Modify pipeline to check for RecruiterProfile existence and create one if user registered via OAuth with recruiter intent. May need to add a session variable during OAuth initiation.

**Risk:** Template duplication between candidate and recruiter dashboards
→ **Mitigation:** Extract common CSS/JS into shared files. Keep templates focused on their role-specific content.

**Risk:** Corporate email validation may block legitimate business domains
→ **Mitigation:** BLOCKED_EMAIL_DOMAINS list is configurable in settings.py. Can be extended or reduced as needed.
