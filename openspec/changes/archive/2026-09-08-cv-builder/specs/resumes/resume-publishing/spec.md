## Purpose

Manages the publishing workflow for CVs, including sector tag selection, validation rules, and status transitions from draft to published.

## ADDED Requirements

### Requirement: Publish button in editor
The system SHALL display a visible "Publish" button within the editor interface for draft resumes.

#### Scenario: Publish button visible for draft
- **WHEN** user is editing a resume with status 'draft'
- **THEN** system displays a "Publish" button

#### Scenario: Publish button hidden for published
- **WHEN** user is editing a resume with status 'published'
- **THEN** system hides the "Publish" button or shows "Unpublish" option

### Requirement: Sector tag selection modal
The system SHALL display a modal dialog before publishing where users can select one or more sector tags for their CV.

#### Scenario: Modal opens on publish click
- **WHEN** user clicks the "Publish" button
- **THEN** system displays a modal with available sector tags as checkboxes

#### Scenario: Primary tag selection
- **WHEN** user selects multiple tags in the modal
- **THEN** system requires one tag to be designated as "primary" via a dropdown or radio button

#### Scenario: No tags selected
- **WHEN** user attempts to confirm publishing without selecting any tags
- **THEN** system displays an error requiring at least one tag selection

### Requirement: Publishing validation
The system SHALL validate the following before allowing publication: resume has content (name and bio not empty), user has a profile photo, and at least one sector tag is selected.

#### Scenario: Validation passes
- **WHEN** user confirms publishing with valid content, photo, and tags
- **THEN** system changes resume status to 'published' and it appears on the talent wall

#### Scenario: Validation fails - missing content
- **WHEN** user attempts to publish without name or bio
- **THEN** system displays error indicating required fields are missing

#### Scenario: Validation fails - no photo
- **WHEN** user attempts to publish without a profile photo
- **THEN** system displays error prompting user to upload a photo first

### Requirement: One CV per sector constraint
The system SHALL enforce that a user can only have one published CV per sector tag. Attempting to publish a second CV for the same sector SHALL replace the previous one.

#### Scenario: First CV for sector
- **WHEN** user publishes a CV with sector tag "Desarrollo Web" and has no other published CV for that sector
- **THEN** system publishes the CV successfully

#### Scenario: Second CV for same sector
- **WHEN** user publishes a CV with sector tag "Desarrollo Web" and already has a published CV for that sector
- **THEN** system unpublishes the previous CV and publishes the new one

### Requirement: Publishing via API endpoint
The system SHALL provide a POST endpoint at /api/resume/publish/ that accepts resume_id, tags array, and primary_tag, returning the updated resume status.

#### Scenario: API publish success
- **WHEN** POST request is sent with valid resume_id, tags, and primary_tag
- **THEN** system returns JSON with status 'published' and updated timestamp

#### Scenario: API publish validation error
- **WHEN** POST request fails validation
- **THEN** system returns JSON error with specific validation failure messages
