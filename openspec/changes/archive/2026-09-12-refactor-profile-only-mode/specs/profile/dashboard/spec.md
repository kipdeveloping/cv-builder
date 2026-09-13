## MODIFIED Requirements

### Requirement: Dashboard layout with sidebar and main area
El dashboard SHALL mostrar un layout de 2 columnas con sidebar y área principal. La barra lateral SHALL contener controles de perfil y visibilidad.

#### Scenario: Desktop layout
- **WHEN** user accesses dashboard on desktop viewport (>= 1024px)
- **THEN** sidebar displays on the left (4/12 width) and main area on the right (8/12 width)

#### Scenario: Mobile layout
- **WHEN** user accesses dashboard on mobile viewport (< 1024px)
- **THEN** sidebar stacks above main area, both full width

### Requirement: Sidebar displays profile identity
La barra lateral SHALL mostrar la foto del perfil, nombre completo, titular y bio del usuario. Cada campo editable SHALL tener un botón de edición visible.

#### Scenario: Photo display and edit
- **WHEN** user views sidebar
- **THEN** profile photo is displayed in a circular format with an edit button overlay
- **AND** clicking edit button opens a modal for photo upload

#### Scenario: Headline display and edit
- **WHEN** user views sidebar
- **THEN** headline text is displayed below the name
- **AND** clicking the headline or edit icon opens an inline edit modal

#### Scenario: Bio display and edit
- **WHEN** user views sidebar
- **THEN** bio text is displayed
- **AND** clicking edit button opens an inline edit modal

#### Scenario: Title and sector display
- **WHEN** user views sidebar
- **THEN** professional title and sector_name are displayed
- **AND** editable via profile fields modal

### Requirement: Profile visibility toggle in sidebar
La barra lateral SHALL mostrar un toggle de visibilidad (público/privado) que controla si el perfil aparece en el tablón de talentos.

#### Scenario: View visibility toggle
- **WHEN** user views sidebar
- **THEN** a toggle switch shows current visibility state (Public/Private)
- **AND** label indicates "Visible en Tablón" when public, "Privado" when private

#### Scenario: Toggle visibility
- **WHEN** user clicks the visibility toggle
- **THEN** system POSTs to /accounts/toggle-visibility/
- **AND** toggle updates to reflect new state

#### Scenario: Toggle to public requires photo
- **WHEN** user toggles to public without a profile photo
- **THEN** system blocks the toggle and shows error prompting photo upload

### Requirement: Experience/project carousel in main area
El área principal SHALL mostrar un carrusel horizontal de tarjetas de experiencia y proyectos.

#### Scenario: View carousel
- **WHEN** user views main area
- **THEN** experience and project cards are displayed in a horizontal scrollable carousel

#### Scenario: Add new experience/project
- **WHEN** user clicks "+ Agregar experiencia" button
- **THEN** a modal opens showing a preview card with editable fields

#### Scenario: Edit existing card
- **WHEN** user clicks edit button on a carousel card
- **THEN** the same modal opens pre-populated with the card's data
- **AND** user can modify fields and click Save to update

#### Scenario: Delete card
- **WHEN** user clicks delete button on a carousel card
- **THEN** a confirmation dialog appears
- **AND** on confirmation, the card is removed from the carousel and UserProfile JSON fields

### Requirement: Social links section in main area
El área principal SHALL mostrar iconos de enlaces sociales para plataformas que tengan URLs configuradas.

#### Scenario: View social links
- **WHEN** user views main area
- **THEN** social link icons are displayed for platforms with configured URLs

#### Scenario: Add/edit social links
- **WHEN** user clicks add/edit button on social links section
- **THEN** a modal opens with input fields for LinkedIn, GitHub, Twitter/X, Portfolio, and custom URLs
