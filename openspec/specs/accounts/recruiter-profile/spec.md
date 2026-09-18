# accounts/recruiter-profile Specification

## Purpose

Manages recruiter/empresa profiles separate from candidate profiles, including company information, corporate email validation, and role-based OAuth restrictions.

## Requirements

### Requirement: RecruiterProfile model stores company information
The system SHALL maintain a separate RecruiterProfile model linked to User via OneToOneField. The model SHALL store company_name, company_logo, company_sector (ForeignKey to SectorTag), company_description, company_type, work_modality, company_website, is_public, and social_links.

#### Scenario: RecruiterProfile created on registration
- **WHEN** a user completes registration with role "recruiter"
- **THEN** the system creates a RecruiterProfile linked to the User
- **AND** the UserProfile is NOT created for this user

#### Scenario: Company information fields
- **WHEN** a RecruiterProfile is created
- **THEN** company_name is required
- **AND** company_sector is a required ForeignKey to SectorTag
- **AND** company_type accepts values "empresa" or "particular"
- **AND** work_modality accepts values "remote", "hybrid", or "onsite"
- **AND** company_logo, company_description, company_website, and social_links are optional

### Requirement: Corporate email validation for recruiters
The system SHALL reject registration attempts from recruiters using generic email domains. The system SHALL maintain a list of blocked domains including gmail.com, yahoo.com, hotmail.com, outlook.com, live.com, aol.com, icloud.com, mail.com, protonmail.com, zoho.com, yandex.com, qq.com, 163.com, 126.com, gmx.com, and fastmail.com.

#### Scenario: Recruiter registration with blocked domain
- **WHEN** a user attempts to register as a recruiter with email "user@gmail.com"
- **THEN** the system rejects the registration
- **AND** displays an error message indicating corporate email is required

#### Scenario: Recruiter registration with valid corporate domain
- **WHEN** a user attempts to register as a recruiter with email "user@empresa.com"
- **THEN** the system accepts the email domain
- **AND** proceeds with registration

#### Scenario: Candidate registration is unaffected
- **WHEN** a user registers as a candidate with any email domain
- **THEN** the system does NOT apply corporate email validation

### Requirement: Role-based OAuth provider restrictions
The system SHALL only display Google and LinkedIn OAuth buttons for recruiter registrations. GitHub OAuth SHALL NOT be available for recruiter registrations.

#### Scenario: Recruiter OAuth buttons
- **WHEN** a user selects "Busco Talento" (recruiter) role in registration
- **THEN** only Google and LinkedIn OAuth buttons are displayed
- **AND** GitHub OAuth button is hidden

#### Scenario: Candidate OAuth buttons
- **WHEN** a user selects "Busco Trabajo" (candidate) role in registration
- **THEN** Google, GitHub, and LinkedIn OAuth buttons are all displayed

### Requirement: Role field on UserProfile
The system SHALL add a role field to UserProfile with values "candidate" (default) and "recruiter". This field determines which dashboard template to render.

#### Scenario: Default role
- **WHEN** a UserProfile is created
- **THEN** the role field defaults to "candidate"

#### Scenario: Role determines dashboard
- **WHEN** a user with role "candidate" accesses /dashboard/
- **THEN** the system renders the candidate dashboard template
- **WHEN** a user with role "recruiter" accesses /dashboard/
- **THEN** the system renders the recruiter dashboard template
