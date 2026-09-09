# CV Templates Specification

## Purpose

Defines three visually distinct CV templates (Classic, Modern, Creative) that users can select for their resumes, each with unique styling and mandatory photo integration.

## Requirements

### Requirement: Three available templates
The system SHALL provide exactly 3 templates for user selection: Classic, Modern, and Creative, each with distinct visual styling.

#### Scenario: Template gallery displayed
- **WHEN** user navigates to template selection
- **THEN** system displays 3 template options with thumbnails and descriptions

#### Scenario: Template preview
- **WHEN** user hovers over a template option
- **THEN** system shows a larger preview of the template layout

### Requirement: Classic template design
The system SHALL provide a Classic template with formal serif fonts, conservative colors, left sidebar with photo, and traditional section layout.

#### Scenario: Classic template structure
- **WHEN** user selects Classic template
- **THEN** editor displays left sidebar with photo at top, contact info below, main content area with About, Experience, Education, and Skills sections

#### Scenario: Classic template styling
- **WHEN** Classic template is rendered
- **THEN** system applies serif fonts, muted color palette, and professional formatting

### Requirement: Modern template design
The system SHALL provide a Modern template with clean sans-serif fonts, monochrome with one accent color, minimal layout, and photo integrated at top.

#### Scenario: Modern template structure
- **WHEN** user selects Modern template
- **THEN** editor displays centered header with photo and name, horizontal dividers, About and Contact side-by-side, Experience and Education in clean cards

#### Scenario: Modern template styling
- **WHEN** Modern template is rendered
- **THEN** system applies sans-serif fonts, minimal borders, and single accent color

### Requirement: Creative template design
The system SHALL provide a Creative template with bold colors, gradient accents, artistic photo treatment, and asymmetric layout.

#### Scenario: Creative template structure
- **WHEN** user selects Creative template
- **THEN** editor displays color sidebar with photo overlay, bold typography, and sections with accent borders

#### Scenario: Creative template styling
- **WHEN** Creative template is rendered
- **THEN** system applies bold color palette, gradient backgrounds, and artistic photo cropping

### Requirement: Photo mandatory in all templates
The system SHALL require and display the user's profile photo in all three templates, positioned according to each template's design.

#### Scenario: Photo displayed in Classic
- **WHEN** Classic template is rendered with user photo
- **THEN** photo appears in left sidebar with formal framing

#### Scenario: Photo displayed in Modern
- **WHEN** Modern template is rendered with user photo
- **THEN** photo appears at top center with clean border

#### Scenario: Photo displayed in Creative
- **WHEN** Creative template is rendered with user photo
- **THEN** photo appears with color overlay and artistic treatment

### Requirement: Template-specific CSS files
The system SHALL maintain separate CSS files for each template to handle unique styling beyond Tailwind utilities.

#### Scenario: Template CSS loaded
- **WHEN** user selects a template in the editor
- **THEN** system loads the corresponding CSS file for that template's custom styles

### Requirement: Template thumbnails for gallery
The system SHALL provide thumbnail images for each template to display in the selection gallery.

#### Scenario: Thumbnail displayed
- **WHEN** template selection gallery is rendered
- **THEN** system shows a preview image for each of the 3 templates
