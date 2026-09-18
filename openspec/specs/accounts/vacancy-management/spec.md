# accounts/vacancy-management Specification

## Purpose

Manages job vacancies posted by recruiters, including vacancy creation, status management, and applicant tracking.

## Requirements

### Requirement: Vacancy model stores job posting details
The system SHALL maintain a Vacancy model linked to RecruiterProfile via ForeignKey. The model SHALL store title, description, requirements (JSONField), location, modality, salary_range, employment_type, status, applications_count, created_at, and updated_at.

#### Scenario: Vacancy created by recruiter
- **WHEN** a recruiter creates a new vacancy
- **THEN** the system creates a Vacancy linked to their RecruiterProfile
- **AND** status defaults to "draft"
- **AND** applications_count defaults to 0
- **AND** created_at and updated_at are set automatically

#### Scenario: Vacancy status values
- **WHEN** a Vacancy is created
- **THEN** status accepts values "active", "closed", or "draft"

#### Scenario: Vacancy employment type values
- **WHEN** a Vacancy is created
- **THEN** employment_type accepts values "full_time", "part_time", "contract", or "freelance"

#### Scenario: Vacancy modality values
- **WHEN** a Vacancy is created
- **THEN** modality accepts values "remote", "hybrid", or "onsite"

### Requirement: Recruiter can view vacancies in dashboard
The recruiter dashboard SHALL display a list of vacancies associated with the recruiter's profile. Each vacancy SHALL show title, modality, employment_type, and applications_count.

#### Scenario: View vacancy list
- **WHEN** a recruiter accesses their dashboard
- **THEN** the system displays all vacancies linked to their RecruiterProfile
- **AND** each vacancy shows title, modality, employment_type, and applications_count

#### Scenario: No vacancies
- **WHEN** a recruiter has no vacancies
- **THEN** the system displays an empty state message

### Requirement: Visual-only create vacancy form
The system SHALL provide a "Create Vacancy" button in the recruiter dashboard. Clicking this button SHALL navigate to a form page. The form SHALL be visual-only with no backend functionality in this change.

#### Scenario: Create vacancy button visible
- **WHEN** a recruiter views their dashboard
- **THEN** a "+ Crear Vacante" button is visible in the vacancies section

#### Scenario: Create vacancy form page
- **WHEN** a recruiter clicks "+ Crear Vacante"
- **THEN** the system navigates to a form page with fields for title, description, requirements, location, modality, salary_range, and employment_type
- **AND** the form is visual-only (no backend submission)
