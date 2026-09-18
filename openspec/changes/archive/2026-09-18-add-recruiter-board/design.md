## Context

The project is a Django CRUD app with two profile types: `UserProfile` (candidates) and `RecruiterProfile` (companies). Currently, only the candidate talent wall exists at `/tablon/`. The `RecruiterProfile` model already has `is_public`, `company_sector`, `work_modality`, and `company_type` fields. The existing `RecruiterProfile` model and `Vacancy` model provide all data needed for the new wall and public profile page.

## Goals / Non-Goals

**Goals:**
- Add a separate wall page for browsing public recruiter/company profiles
- Provide faceted filtering (sector, modality, company type) without relevance scoring
- Create a public company profile page showing company details and active vacancies
- Convert the navbar "Tablón" button into a dropdown with two navigation options

**Non-Goals:**
- Modifying the existing candidate talent wall behavior
- Adding search functionality beyond faceted filters
- Implementing pagination (can be added later)
- Changing the `RecruiterProfile` or `Vacancy` data models

## Decisions

### 1. Separate API endpoint vs. extending existing wall API
**Decision**: Create a new endpoint `/api/wall/recruiters/` instead of adding a `type` parameter to the existing `/api/wall/profiles/`.

**Rationale**: The existing endpoint returns `UserProfile` data with candidate-specific fields (seniority, tags, experience). Recruiter profiles have fundamentally different fields (company_name, company_type, work_modality). A separate endpoint keeps concerns clean and avoids complex conditional logic in a single endpoint.

### 2. Faceted filtering without scoring
**Decision**: Use strict faceted filtering with AND between facets and OR within facets, returning flat results without relevance scoring.

**Rationale**: The user explicitly requested this architecture. Companies are not ranked by relevance - they are filtered by criteria. This simplifies the API and matches the use case of browsing companies by specific attributes.

### 3. Template approach: reuse vs. new template
**Decision**: Create a new `recruiter_wall.html` template instead of parameterizing the existing `wall.html`.

**Rationale**: The recruiter wall has different filters (no tags, no seniority, different card layout). The existing `wall.html` has complex tag filtering logic that doesn't apply. A separate template is cleaner than conditionally hiding sections.

### 4. JS approach: new file vs. extending wall.js
**Decision**: Create a new `recruiter_wall.js` file instead of extending the existing `wall.js`.

**Rationale**: The existing `wall.js` has tag management, hierarchy cascading, and scoring logic that doesn't apply to the recruiter wall. A new file keeps the codebase maintainable and avoids bloating the existing file with conditional logic.

### 5. Public profile URL structure
**Decision**: Use `/empresa/<user_id>/` as the public profile URL, matching the existing `/candidato/<user_id>/` pattern.

**Rationale**: Consistent URL pattern with the existing candidate profile. Uses `user_id` as the identifier since `RecruiterProfile` has a OneToOneField to User.

## Risks / Trade-offs

- **Risk**: Duplicate code between candidate and recruiter walls (filters, cards, JS patterns)
  - **Mitigation**: Acceptable for now. If a third wall type is added, refactor shared patterns into components.

- **Risk**: No pagination on recruiter wall could be slow with many profiles
  - **Mitigation**: Initial implementation loads all public profiles. Pagination can be added as a follow-up enhancement.

- **Risk**: Faceted filtering may return many OR-combined results for sector filter
  - **Mitigation**: Acceptable. The filtering is strict and the user controls the facets.
