# Resume Editor Specification

## Purpose

Provides a visual CV editor using contenteditable regions with auto-save functionality, allowing users to create and edit their resumes interactively.

## Requirements

### Requirement: Visual editor with contenteditable regions
The system SHALL provide a visual editor where users click directly on template regions to edit content, using HTML contenteditable attributes.

#### Scenario: User clicks editable region
- **WHEN** user clicks on an editable region in the template
- **THEN** region becomes focused and user can type directly into it

#### Scenario: User edits text content
- **WHEN** user types in an editable region
- **THEN** text updates in real-time within the template layout

### Requirement: Auto-save with debounce
The system SHALL automatically save CV content to the server after 2 seconds of inactivity, without requiring manual save action.

#### Scenario: Auto-save triggered after inactivity
- **WHEN** user stops typing for 2 seconds
- **THEN** system sends a POST request to save the current content

#### Scenario: Auto-save on blur
- **WHEN** user clicks outside an editable field
- **THEN** system immediately saves the content without waiting for debounce

#### Scenario: Save feedback displayed
- **WHEN** content is successfully saved
- **THEN** system displays a timestamp indicator showing when the save occurred

### Requirement: JSON content storage
The system SHALL store all CV content as a JSON object in the Resume model, with fields corresponding to the editable regions.

#### Scenario: Content saved as JSON
- **WHEN** auto-save occurs
- **THEN** system serializes all editable field values into a JSON structure and saves to the database

#### Scenario: Content loaded from JSON
- **WHEN** user opens an existing CV in the editor
- **THEN** system loads the JSON content and populates the editable regions accordingly

### Requirement: Template selection before editing
The system SHALL require users to select a template before entering the editor, and display the template structure with editable regions.

#### Scenario: First-time CV creation
- **WHEN** user clicks "Create new CV"
- **THEN** system displays template selection gallery with 3 options

#### Scenario: Template selected
- **WHEN** user selects a template from the gallery
- **THEN** system loads the editor with that template's HTML structure and editable regions

### Requirement: Editable fields definition
The system SHALL support the following editable fields: name, email, phone, city, bio, experience (title, company, period, description), education (degree, school, year), and skills (list of strings).

#### Scenario: User edits experience entry
- **WHEN** user clicks on an experience item and modifies the title
- **THEN** system updates the experience array in the JSON content

#### Scenario: User adds new skill
- **WHEN** user clicks "Add skill" and types a new skill name
- **THEN** system adds the skill to the skills array in JSON content

### Requirement: Resume model with status tracking
The system SHALL maintain each Resume with a status field that can be 'draft' or 'published', defaulting to 'draft' on creation.

#### Scenario: New resume created
- **WHEN** user selects a template and enters the editor
- **THEN** system creates a Resume with status 'draft'

#### Scenario: Resume content updated
- **WHEN** auto-save occurs on a draft resume
- **THEN** system updates the content while maintaining 'draft' status
