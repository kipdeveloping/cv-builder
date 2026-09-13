# User Profile Specification

## Purpose

Manages user profile data including photo upload, bio field, and visibility controls, displayed on the public talent wall.

## Requirements

### Requirement: UserProfile model with photo, bio, and visibility
The system SHALL maintain a UserProfile linked one-to-one with each User, containing a photo field, bio text field, is_public boolean, sector_name text, and professional title. The profile SHALL NOT reference Resume or SectorTag via foreign keys.

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
