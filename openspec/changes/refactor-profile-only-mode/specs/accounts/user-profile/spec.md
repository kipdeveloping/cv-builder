## MODIFIED Requirements

### Requirement: UserProfile model with photo and bio
The system SHALL maintain a UserProfile linked one-to-one with each User, containing a photo field and a bio text field. **The profile no longer references Resume or SectorTag via foreign keys. Instead, it stores sector as free text (sector_name) and professional title directly.**

#### Scenario: Profile created on user registration
- **WHEN** a new user registers
- **THEN** a UserProfile is automatically created with empty photo and bio fields
- **AND** `is_public` defaults to false
- **AND** `sector_name` and `title` are populated from registration wizard

#### Scenario: Profile stores sector as text
- **WHEN** user completes registration with sector field
- **THEN** the sector value is stored in `UserProfile.sector_name` (CharField)
- **AND** no SectorTag foreign key is created or referenced

#### Scenario: Profile stores professional title
- **WHEN** user completes registration with title field
- **THEN** the title value is stored in `UserProfile.title` (CharField)

### Requirement: Photo upload from dashboard
The system SHALL allow users to upload or change their profile photo from the dashboard interface.

#### Scenario: Successful photo upload
- **WHEN** user selects a valid image file (jpg, png, webp) under 5MB
- **THEN** system saves the photo and displays it in the dashboard and on the public profile page

#### Scenario: Photo upload with invalid file type
- **WHEN** user attempts to upload a file that is not jpg, png, or webp
- **THEN** system rejects the upload with an error message indicating allowed formats

#### Scenario: Photo upload exceeds size limit
- **WHEN** user attempts to upload a file larger than 5MB
- **THEN** system rejects the upload with an error message indicating the size limit

### Requirement: Bio field for talent wall display
The system SHALL store a bio text in the UserProfile that is displayed on the talent wall cards.

#### Scenario: User edits bio
- **WHEN** user updates their bio text in the dashboard
- **THEN** system saves the bio and it appears on their talent wall card (if profile is public)

### Requirement: Photo required for public profile visibility
The system SHALL prevent users from making their profile public unless they have uploaded a profile photo.

#### Scenario: Toggle public without photo
- **WHEN** user attempts to set `is_public=true` without a profile photo
- **THEN** system blocks the toggle and prompts user to upload a photo first

### Requirement: Profile visibility toggle
The system SHALL provide an API endpoint for toggling the `is_public` field on UserProfile.

#### Scenario: Toggle visibility via API
- **WHEN** authenticated user POSTs to /accounts/toggle-visibility/
- **THEN** system toggles the `is_public` field on the user's profile
- **AND** returns the new visibility state

### REMOVED Requirements

### Requirement: Photo required before publishing
**Reason**: CV publishing removed; replaced by profile visibility toggle which requires photo
**Migration**: Use new visibility toggle requirement

### Requirement: Photo displayed on all CVs
**Reason**: CV templates and resume editor removed
**Migration**: Photo displayed on public profile page instead

### Requirement: UserProfile linked to Resume via resume_destacado
**Reason**: Resume model and featured resume concept removed
**Migration**: Public profile displays profile data directly (experience, projects from profile JSON fields)

### Requirement: UserProfile linked to SectorTag via sector FK
**Reason**: SectorTag moved to accounts for filtering; profile stores sector as free text
**Migration**: Use `sector_name` CharField on UserProfile