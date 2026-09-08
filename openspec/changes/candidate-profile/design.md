## Context

The CV Builder platform currently has a minimal dashboard (photo upload + bio edit), CV templates (classic, modern, creative), a talent wall with filterable grid, and a CV detail page. The project uses Django with Tailwind CSS, vanilla JavaScript, and JSONField for resume content storage. The `Resume.content` JSONField stores all CV data including experience, education, and skills as arrays/objects.

Key constraints:
- CV templates (classic.html, modern.html, creative.html) MUST NOT be modified
- All new features are profile-page exclusive
- The publish mechanism already exists in the editor (publish button + publish.js)
- Registration collects only email + password (future OAuth compatible)
- Email backend is console for development

## Goals / Non-Goals

**Goals:**
- Redesign dashboard as a 2-column profile management page with inline editing
- Create public profile page at `/candidato/<user_id>/` with read-only view
- Implement structured skill taxonomy with automatic sync from Resume.content
- Enable contact between visitors and candidates via email
- Integrate wall cards with profile navigation
- Support featured resume designation

**Non-Goals:**
- Modifying CV templates (classic, modern, creative)
- Changing the registration flow (email + password only)
- Implementing real email sending (console backend only)
- Adding OAuth or social authentication
- Modifying the CV editor's publish mechanism
- Implementing real-time collaboration or notifications

## Decisions

### Decision 1: Data Storage Strategy (Hybrid Approach)

**Choice**: Structured fields for searchable/filterable data, JSON for display-only data.

**Rationale**:
- `UserProfile` model stores: headline, location_flex, search_status, availability, resume_destacado (FK)
- `Skill`/`UserSkill` models store: structured skill data for filtering
- `Resume.content` JSON stores: experience[], projects[], social_links{} (display-only)

**Alternatives considered**:
- All data in JSON: Rejected because skills need relational queries for filtering/search
- All data in relational models: Rejected because experience/projects are complex nested structures that are simpler to manage as JSON

### Decision 2: Skills Sync Strategy

**Choice**: Automatic sync on resume save via `save_resume_api` modification.

**Rationale**:
- When `save_resume_api` is called, extract `skills[]` from content JSON
- For each skill name, ensure `Skill` record exists (create if not)
- Ensure `UserSkill` record exists (create if not)
- Remove `UserSkill` records for skills no longer in any resume
- Preserve `is_primary` flag on existing `UserSkill` records

**Alternatives considered**:
- Manual sync from dashboard: Rejected because it adds user friction
- Background task sync: Rejected because it adds complexity without clear benefit
- Sync on profile view: Rejected because it creates read-time latency

### Decision 3: Featured Resume Strategy

**Choice**: `UserProfile.resume_destacado` FK with fallback to most recent published resume.

**Rationale**:
- Single `resume_destacado` FK on UserProfile
- If FK is NULL or resume is unpublished, fall back to `Resume.objects.filter(user=profile.user, status='published').order_by('-updated_at').first()`
- Star icon toggle in CV list modal sets the featured resume

**Alternatives considered**:
- Multiple featured resumes: Rejected because it complicates the profile display
- No featured resume (always use most recent): Rejected because users want control over which resume is displayed

### Decision 4: Carousel Implementation

**Choice**: Vanilla JavaScript with horizontal scroll and navigation arrows.

**Rationale**:
- No external dependencies (no Swiper.js)
- Simple prev/next arrows with smooth scroll behavior
- Card counter shows current position
- Each card has edit/delete buttons (owner only)

**Alternatives considered**:
- Swiper.js: Rejected because it adds a dependency for a simple use case
- CSS-only scroll snap: Rejected because it lacks navigation controls
- Multi-row grid: Rejected because the requirement specifies horizontal carousel

### Decision 5: Modal Strategy for Card Creation/Editing

**Choice**: Center-of-screen modal with live preview card that matches carousel card styling.

**Rationale**:
- Modal shows exact preview of how the card will look in the carousel
- All fields are contenteditable within the modal
- Save/Cancel buttons at bottom
- Same modal template used for both create and edit (pre-populated for edit)

**Alternatives considered**:
- Separate create/edit pages: Rejected because it breaks the single-page experience
- Inline editing in carousel: Rejected because it's cramped and error-prone
- Form-based modal: Rejected because the preview card approach gives better WYSIWYG experience

### Decision 6: Contact System

**Choice**: Django console email backend with rate limiting.

**Rationale**:
- Contact form sends email via `django.core.mail.send_mail()`
- Console backend prints to terminal in development
- Rate limit: 5 submissions per IP per hour
- Email includes visitor name, email, and message

**Alternatives considered**:
- Database-stored messages: Rejected because it adds complexity without clear benefit
- Real SMTP: Deferred to production deployment
- Third-party contact form service: Rejected because it adds external dependency

## Risks / Trade-offs

### Risk 1: Skills Sync Complexity
**Risk**: Automatic sync from multiple resumes could lead to unexpected skill removal if a user has skills in only one resume and deletes it.
**Mitigation**: Union all skills from all resumes before removing any UserSkill records. Only remove a skill if it appears in NO resume.

### Risk 2: Profile Data Consistency
**Risk**: Dashboard shows data from featured resume, but experience/projects are stored in Resume.content. If user changes resume, profile display changes.
**Mitigation**: This is by design. The featured resume determines what's displayed. Users can change featured resume at any time.

### Risk 3: Carousel Performance
**Risk**: Large number of experience/project cards could slow down carousel rendering.
**Mitigation**: Limit to 20 cards maximum. If exceeded, show warning and suggest removing older entries.

### Risk 4: Contact Form Abuse
**Risk**: Contact form could be used for spam or harassment.
**Mitigation**: Rate limiting (5/hour/IP), CAPTCHA could be added later, and email includes sender info for accountability.

### Risk 5: Mobile Layout Complexity
**Risk**: 2-column layout on desktop needs careful handling for mobile.
**Mitigation**: Use Tailwind's responsive prefixes (md:, lg:) for breakpoints. Test on common mobile viewports.

## Migration Plan

1. **Phase 1 - Models**: Create migration for UserProfile extension + Skill + UserSkill models
2. **Phase 2 - Backend**: Update views and URLs (backward compatible - existing URLs still work)
3. **Phase 3 - Dashboard**: Replace dashboard template (breaking change for dashboard layout)
4. **Phase 4 - Profile**: Add new profile page (additive - no breaking changes)
5. **Phase 5 - Wall Integration**: Update wall.js and cv_detail.html (breaking change for card navigation)

**Rollback strategy**: Git revert to previous commit. No data migration required since all changes are additive or template-level.

## Open Questions

None. All technical decisions have been resolved based on user requirements.
