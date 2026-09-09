# User Profile Specification

## Purpose

Manages user profile data including photo upload and bio field, displayed on the public talent wall and used across all CVs.

## Requirements

### Requirement: UserProfile model with photo and bio
The system SHALL maintain a UserProfile linked one-to-one with each User, containing a photo field and a bio text field.

#### Scenario: Profile created on user registration
- **WHEN** a new user registers
- **THEN** a UserProfile is automatically created with empty photo and bio fields

### Requirement: Photo upload from dashboard
The system SHALL allow users to upload or change their profile photo from the dashboard interface.

#### Scenario: Successful photo upload
- **WHEN** user selects a valid image file (jpg, png, webp) under 5MB
- **THEN** system saves the photo and displays it in the dashboard and on all CVs

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
- **THEN** system saves the bio and it appears on their talent wall card

### Requirement: Photo required before publishing
The system SHALL prevent users from publishing a CV unless they have uploaded a profile photo.

#### Scenario: Publish attempt without photo
- **WHEN** user attempts to publish a CV without a profile photo
- **THEN** system blocks publishing and prompts user to upload a photo first

### Requirement: Photo displayed on all CVs
The system SHALL use the same UserProfile photo across all of the user's CVs, rendered according to each template's layout.

#### Scenario: Photo in Classic template
- **WHEN** user views a CV with Classic template
- **THEN** photo appears in the left sidebar with formal styling

#### Scenario: Photo in Modern template
- **WHEN** user views a CV with Modern template
- **THEN** photo appears at the top with clean minimalist styling

#### Scenario: Photo in Creative template
- **WHEN** user views a CV with Creative template
- **THEN** photo appears with color overlay and artistic styling
