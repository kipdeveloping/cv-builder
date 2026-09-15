## Purpose

Allows users to select tags from the hierarchical dictionary and associate them with their profiles, marking each as obligatory (MUST) or desirable (NICE TO HAVE), and to set global attributes like seniority and languages.

## ADDED Requirements

### Requirement: Hierarchical tag selection in dashboard
The dashboard SHALL display a "Mis Habilidades" section between Bio and Work Preferences with a modal for editing tags.

#### Scenario: View current tags
- **WHEN** user navigates to dashboard
- **THEN** system displays current sector, role, specialty, and associated tags in the sidebar

#### Scenario: Open edit modal
- **WHEN** user clicks "Editar" on Mis Habilidades section
- **THEN** system opens modal with hierarchical selectors and tag inputs

### Requirement: Cascading dropdown selection
The dashboard modal SHALL provide dropdowns for Sector, Role, and Specialty that filter options based on parent selection.

#### Scenario: Select sector
- **WHEN** user selects sector="Tecnología"
- **THEN** Role dropdown updates to show only Tecnología roles (Dev Web, Data Science, DevOps)

#### Scenario: Select role
- **WHEN** user selects role="Dev Web"
- **THEN** Specialty dropdown updates to show only Dev Web specialties (Backend, Frontend, Fullstack)

#### Scenario: Clear parent selection
- **WHEN** user changes sector from "Tecnología" to "Marketing"
- **THEN** Role and Specialty selections are cleared and dropdowns update

### Requirement: Tag search and selection
Users SHALL be able to search for tags by name and add them to their profile as either MUST or NICE type.

#### Scenario: Search for tag
- **WHEN** user types "Dj" in tag search input
- **THEN** system shows dropdown with tags matching "Dj" (e.g., "Django")

#### Scenario: Add tag as must
- **WHEN** user selects "Django" and clicks "Obligatorio" button
- **THEN** system adds Django to must_tags list with visual indicator

#### Scenario: Add tag as nice
- **WHEN** user selects "React" and clicks "Deseable" button
- **THEN** system adds React to nice_tags list with visual indicator

#### Scenario: Remove tag
- **WHEN** user clicks X on "Django" tag chip
- **THEN** system removes Django from profile tags

### Requirement: Seniority selection
The dashboard modal SHALL provide a dropdown for selecting seniority level (Junior, Semi-Senior, Senior, Lead).

#### Scenario: Set seniority
- **WHEN** user selects seniority="Senior"
- **THEN** system saves seniority to profile

#### Scenario: Clear seniority
- **WHEN** user selects seniority=""
- **THEN** system clears seniority from profile

### Requirement: Language selection
The dashboard SHALL allow users to add multiple languages with proficiency levels.

#### Scenario: Add language
- **WHEN** user adds language="en" with level="B2"
- **THEN** system stores {"en": "B2"} in languages field

#### Scenario: Add multiple languages
- **WHEN** user has {"es": "nativo"} and adds {"en": "B2"}
- **THEN** system stores {"es": "nativo", "en": "B2"}

#### Scenario: Remove language
- **WHEN** user removes "en" from languages
- **THEN** system stores {"es": "nativo"}

### Requirement: Save profile tags
Changes to tags and attributes SHALL be saved via API endpoint and reflected in searches immediately.

#### Scenario: Save successfully
- **WHEN** user clicks "Guardar" in modal
- **AND** all selections are valid
- **THEN** system saves to database and shows success message

#### Scenario: Save with error
- **WHEN** user clicks "Guardar" but API returns error
- **THEN** system shows error message and retains unsaved changes

### Requirement: Adapt to existing dashboard design
The new section SHALL follow the existing dashboard card pattern with consistent styling.

#### Scenario: Display section
- **WHEN** dashboard loads
- **THEN** Mis Habilidades section appears as white card with rounded corners, shadow, and consistent padding

#### Scenario: Display tags
- **WHEN** user has tags assigned
- **THEN** tags display as colored chips consistent with existing badge styling
