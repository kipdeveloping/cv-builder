## Purpose

Provides a dedicated wall for browsing public recruiter/company profiles with faceted filtering, separate from the candidate talent wall. Allows visitors to discover companies and recruiters by sector, work modality, and company type.

## ADDED Requirements

### Requirement: Recruiter wall page
The system SHALL provide a wall page at `/tablon-empresas/` that displays public `RecruiterProfile` entries in a grid layout.

#### Scenario: Recruiter wall renders
- **WHEN** visitor navigates to `/tablon-empresas/`
- **THEN** the system renders the recruiter wall page with filter controls and a profile grid

#### Scenario: Recruiter wall shows only public profiles
- **WHEN** the recruiter wall loads
- **THEN** only profiles with `is_public=true` are displayed
- **AND** profiles with `is_public=false` are excluded

### Requirement: Recruiter wall API with faceted filtering
The system SHALL provide a GET endpoint at `/api/wall/recruiters/` that returns filtered `RecruiterProfile` data as JSON. Filtering SHALL use faceted strict logic without relevance scoring.

#### Scenario: API returns all public recruiter profiles
- **WHEN** GET request is sent to `/api/wall/recruiters/` without parameters
- **THEN** system returns all public recruiter profiles

#### Scenario: API filters by sector (OR logic)
- **WHEN** GET request is sent with `sector[]=fintech&sector[]=healthtech`
- **THEN** system returns profiles where `company_sector` matches ANY of the provided sector slugs

#### Scenario: API filters by modality (OR logic)
- **WHEN** GET request is sent with `modality[]=remote&modality[]=hybrid`
- **THEN** system returns profiles where `work_modality` matches ANY of the provided modality values

#### Scenario: API filters by company type
- **WHEN** GET request is sent with `company_type=empresa`
- **THEN** system returns only profiles with `company_type='empresa'`

#### Scenario: API combines multiple facets with AND logic
- **WHEN** GET request is sent with `sector[]=fintech&modality[]=remote`
- **THEN** system returns profiles matching BOTH the sector AND the modality criteria

#### Scenario: API response format
- **WHEN** API returns recruiter profiles
- **THEN** each profile object includes: `id`, `user_id`, `company_name`, `company_logo`, `sector`, `company_type`, `work_modality`, `company_description`, `company_website`, `social_links`

### Requirement: Recruiter profile navigation from wall
Wall recruiter profile cards SHALL link to the company's public profile page at `/empresa/<user_id>/`.

#### Scenario: Click recruiter card on wall
- **WHEN** visitor clicks on a recruiter profile card in the wall grid
- **THEN** the browser navigates to `/empresa/<user_id>/`

### Requirement: Recruiter public profile page
The system SHALL provide a public profile page at `/empresa/<user_id>/` that displays company information and active vacancies.

#### Scenario: Recruiter profile page renders
- **WHEN** visitor navigates to `/empresa/<user_id>/`
- **AND** the recruiter profile exists and has `is_public=true`
- **THEN** the system renders the company profile page showing: company logo, company name, sector, company type, work modality, company description, social links, and list of active vacancies

#### Scenario: Recruiter profile not found
- **WHEN** visitor navigates to `/empresa/<user_id>/`
- **AND** no `RecruiterProfile` exists for that user
- **THEN** the system returns a 404 response

#### Scenario: Recruiter profile is private
- **WHEN** visitor navigates to `/empresa/<user_id>/`
- **AND** the recruiter profile has `is_public=false`
- **THEN** the system returns a 404 response

### Requirement: Navbar dropdown for wall navigation
The navbar SHALL display a dropdown menu for wall navigation instead of a single "Tablón" link. The dropdown SHALL contain two options: "Para trabajadores" linking to `/tablon/` and "Para reclutadores" linking to `/tablon-empresas/`.

#### Scenario: Navbar shows dropdown
- **WHEN** visitor views the navbar
- **THEN** a dropdown button labeled "Tablón" is displayed

#### Scenario: Dropdown contains two options
- **WHEN** visitor clicks the "Tablón" dropdown
- **THEN** two options are shown: "Para trabajadores" and "Para reclutadores"

#### Scenario: Dropdown navigation
- **WHEN** visitor clicks "Para trabajadores"
- **THEN** the browser navigates to `/tablon/`
- **WHEN** visitor clicks "Para reclutadores"
- **THEN** the browser navigates to `/tablon-empresas/`
