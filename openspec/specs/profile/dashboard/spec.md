# profile/dashboard Specification

## Purpose

Provides the user dashboard interface for managing profile information including work preferences, skills, languages, and professional details.

## Requirements

### Requirement: Work preferences section in sidebar
The sidebar SHALL display work preferences (employment type, willingness to relocate, travel availability). An edit button SHALL open a modal for updating these fields. The employment type checkboxes SHALL render correctly with all available options.

#### Scenario: View work preferences
- **WHEN** user views sidebar
- **THEN** work preferences are displayed with current values

#### Scenario: Employment type checkboxes render
- **WHEN** user opens work preferences modal
- **THEN** employment type checkboxes are displayed with all options from EMPLOYMENT_TYPE_CHOICES
- **AND** currently selected types are pre-checked

#### Scenario: Edit work preferences
- **WHEN** user clicks edit button on work preferences section
- **THEN** a modal opens with checkboxes for employment type and dropdowns for relocate/travel
- **AND** changes are saved via POST to /update-profile/

### Requirement: Skills modal with hierarchy dropdowns
The dashboard SHALL provide a skills modal that allows users to select their sector, rol, especialidad, seniority, languages, and tags from the global dictionary. The modal SHALL load hierarchy data from the API and populate cascading dropdowns.

#### Scenario: Open skills modal loads hierarchy
- **WHEN** user clicks "Editar" on the skills section
- **THEN** the skills modal opens
- **AND** sector dropdown is populated from /api/tags/hierarchy/
- **AND** user's current selections are pre-populated

#### Scenario: Cascading dropdown behavior
- **WHEN** user selects a sector in the skills modal
- **THEN** rol dropdown is populated with roles for that sector
- **AND** especialidad dropdown is cleared

#### Scenario: Save skills
- **WHEN** user selects sector, rol, especialidad, seniority, languages, and tags
- **AND** clicks "Guardar"
- **THEN** system POSTs to /accounts/api/profile/tags/save/
- **AND** profile is updated with new selections
- **AND** modal closes and sidebar updates

### Requirement: Simple tag selection for profiles
The skills modal SHALL provide a single tag selector (no must/nice distinction). Users SHALL select tags from the global dictionary. These tags determine under which filters the profile appears in the wall.

#### Scenario: Add tags from global dictionary
- **WHEN** user types in the tag search input
- **THEN** system shows matching tags from /api/tags/all/
- **AND** user can click to add a tag

#### Scenario: Remove tags
- **WHEN** user clicks the X on a tag chip
- **THEN** the tag is removed from the selection

### Requirement: Title field in skills modal
The skills modal SHALL include a title input field that allows users to edit their professional title. The title SHALL sync with headline (if one is empty when the other is saved).

#### Scenario: Edit title in skills modal
- **WHEN** user changes the title field in skills modal
- **AND** clicks "Guardar"
- **THEN** title is saved
- **AND** if headline was empty, headline is set to the title value

### Requirement: Languages display in sidebar
The sidebar SHALL display the user's configured languages with their proficiency levels.

#### Scenario: View languages
- **WHEN** user views sidebar and has configured languages
- **THEN** languages are displayed as "language (level)" format
- **AND** multiple languages are separated by commas

### Requirement: Languages editor in skills modal
The skills modal SHALL allow users to add and remove languages with proficiency levels.

#### Scenario: Add language
- **WHEN** user selects a language and level, then clicks "+"
- **THEN** language chip is added to the display
- **AND** language is included in the save payload

#### Scenario: Remove language
- **WHEN** user clicks the X on a language chip
- **THEN** language is removed from the selection
