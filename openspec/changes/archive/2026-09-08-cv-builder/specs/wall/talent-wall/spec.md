## Purpose

Provides a public talent wall where visitors can browse published CVs in a grid layout with real-time filtering by sector tags.

## ADDED Requirements

### Requirement: Public access to talent wall
The system SHALL allow both authenticated users and anonymous visitors to access the talent wall without login.

#### Scenario: Visitor accesses talent wall
- **WHEN** unauthenticated user navigates to /tablon/
- **THEN** system displays the talent wall with published CV cards

#### Scenario: Authenticated user accesses talent wall
- **WHEN** logged-in user navigates to /tablon/
- **THEN** system displays the talent wall with published CV cards

### Requirement: CV card display with photo, name, and bio
The system SHALL display each published CV as a card showing the user's profile photo, full name, and truncated bio text.

#### Scenario: Card rendered with all fields
- **WHEN** talent wall loads with published CVs
- **THEN** each card shows photo at top, name below photo, and bio text truncated to approximately 80 characters

#### Scenario: Card with long bio
- **WHEN** user's bio exceeds 80 characters
- **THEN** system truncates bio with ellipsis (...) on the card

### Requirement: Grid layout for CV cards
The system SHALL display CV cards in a responsive grid layout that adapts to different screen sizes.

#### Scenario: Desktop grid display
- **WHEN** talent wall is viewed on desktop
- **THEN** cards display in a multi-column grid (3-4 columns)

#### Scenario: Mobile grid display
- **WHEN** talent wall is viewed on mobile
- **THEN** cards display in a single column layout

### Requirement: AJAX sector filtering
The system SHALL provide filter buttons for sector tags that update the displayed CVs in real-time without page reload.

#### Scenario: Filter buttons displayed
- **WHEN** talent wall loads
- **THEN** system displays filter buttons for all available sector tags plus an "All" option

#### Scenario: Filter by sector tag
- **WHEN** user clicks a sector filter button
- **THEN** system sends AJAX request and updates grid to show only CVs with that sector tag

#### Scenario: Filter shows all
- **WHEN** user clicks "All" filter button
- **THEN** system displays all published CVs regardless of sector

### Requirement: API endpoint for filtered CVs
The system SHALL provide a GET endpoint at /api/wall/cvs/ that accepts a sector parameter and returns filtered CV cards as JSON.

#### Scenario: API returns filtered results
- **WHEN** GET request is sent with sector=desarrollo-web
- **THEN** system returns JSON array of CV cards matching that sector

#### Scenario: API returns all when no filter
- **WHEN** GET request is sent without sector parameter
- **THEN** system returns all published CV cards

### Requirement: CV detail view
The system SHALL allow users to view a full CV by clicking on a card in the talent wall.

#### Scenario: Click on CV card
- **WHEN** user clicks on a CV card in the talent wall
- **THEN** system navigates to a detail view showing the complete CV with all sections
