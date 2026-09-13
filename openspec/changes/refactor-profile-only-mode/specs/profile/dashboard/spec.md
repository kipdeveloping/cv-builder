## MODIFIED Requirements

### Requirement: Dashboard layout with sidebar and main area
The dashboard SHALL display a 2-column responsive layout with a sidebar (4/12 width on desktop) and main content area (8/12 width on desktop). On mobile, the layout SHALL stack vertically.

#### Scenario: Desktop layout
- **WHEN** user accesses dashboard on desktop viewport (>= 1024px)
- **THEN** sidebar displays on the left (4/12 width) and main area on the right (8/12 width)

#### Scenario: Mobile layout
- **WHEN** user accesses dashboard on mobile viewport (< 1024px)
- **THEN** sidebar stacks above main area, both full width

### Requirement: Sidebar displays profile identity
The sidebar SHALL display the user's profile photo (circular), full name, headline, and bio. Each editable field SHALL have a visible edit button that opens an inline modal.

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
The sidebar SHALL display a visibility toggle (public/private) that controls whether the profile appears on the talent wall.

#### Scenario: View visibility toggle
- **WHEN** user views sidebar
- **THEN** a toggle switch shows current visibility state (Public/Private)
- **AND** label indicates "Visible en Tablón" when public, "Privado" when private

#### Scenario: Toggle visibility
- **WHEN** user clicks the visibility toggle
- **THEN** system POSTs to /accounts/toggle-visibility/
- **AND** toggle updates to reflect new state
- **AND** profile visibility on wall changes immediately

#### Scenario: Toggle to public requires photo
- **WHEN** user toggles to public without a profile photo
- **THEN** system blocks the toggle and shows error prompting photo upload
- **AND** visibility remains private

### Requirement: Skills section in sidebar - REMOVED
**Reason**: Skill and UserSkill models removed; skills system will be rebuilt later as tag/filter system
**Migration**: Remove skills grid and edit modal from sidebar; no skills displayed on wall

### Requirement: Status badges in sidebar
The sidebar SHALL display employment status badges (search status, availability, location preference). An edit button SHALL open a modal for updating these fields.

#### Scenario: View status badges
- **WHEN** user views sidebar
- **THEN** status badges are displayed showing current search_status, availability, and location_flex values

#### Scenario: Edit status
- **WHEN** user clicks edit button on status section
- **THEN** a modal opens with dropdowns for each status field
- **AND** changes are saved via POST to /update-profile/

### Requirement: Mis CVs button - REMOVED
**Reason**: CV management removed; dashboard is profile-only
**Migration**: Remove "Mis Curriculums" button and modal entirely

### Requirement: Experience/project carousel in main area
The main area SHALL display a horizontal carousel of experience and project cards. Each card SHALL show title, company/project name, period, and description. Owner SHALL see edit and delete buttons on each card.

#### Scenario: View carousel
- **WHEN** user views main area
- **THEN** experience and project cards are displayed in a horizontal scrollable carousel
- **AND** navigation arrows allow scrolling left/right
- **AND** a card counter shows current position (e.g., "2 of 5")

#### Scenario: Add new experience/project
- **WHEN** user clicks "+ Agregar experiencia" button
- **THEN** a modal opens showing a preview card with editable fields (title, company, period, description)
- **AND** the preview card matches the exact styling of cards in the carousel
- **AND** user can fill in fields and click Save to add the card
- **AND** or click Cancel to discard

#### Scenario: Edit existing card
- **WHEN** user clicks edit button on a carousel card
- **THEN** the same modal opens pre-populated with the card's data
- **AND** user can modify fields and click Save to update
- **AND** or click Cancel to discard changes

#### Scenario: Delete card
- **WHEN** user clicks delete button on a carousel card
- **THEN** a confirmation dialog appears
- **AND** on confirmation, the card is removed from the carousel and UserProfile JSON fields

### Requirement: Social links section in main area
The main area SHALL display social link icons for platforms that have URLs configured. An add/edit button SHALL open a modal for managing social links.

#### Scenario: View social links
- **WHEN** user views main area
- **THEN** social link icons are displayed for platforms with configured URLs
- **AND** each icon links to the configured URL

#### Scenario: Add/edit social links
- **WHEN** user clicks add/edit button on social links section
- **THEN** a modal opens with input fields for LinkedIn, GitHub, Twitter/X, Portfolio, and custom URLs
- **AND** user can add/remove platform URLs
- **AND** changes are saved to UserProfile JSON fields (social_links)

### Requirement: Work preferences section in sidebar
The sidebar SHALL display work preferences (employment type, willingness to relocate, travel availability). An edit button SHALL open a modal for updating these fields.

#### Scenario: View work preferences
- **WHEN** user views sidebar
- **THEN** work preferences are displayed with current values

#### Scenario: Edit work preferences
- **WHEN** user clicks edit button on work preferences section
- **THEN** a modal opens with checkboxes for employment type and dropdowns for relocate/travel
- **AND** changes are saved via POST to /update-profile/

### Requirement: Onboarding banner for incomplete profiles
If the user's first_name or last_name is empty, the dashboard SHALL display an onboarding banner prompting them to complete their name.

#### Scenario: Show onboarding banner
- **WHEN** user accesses dashboard AND (first_name is empty OR last_name is empty)
- **THEN** a yellow banner appears at the top of the dashboard
- **AND** banner contains a form to enter first_name and last_name
- **AND** submitting the form POSTs to /update-name/

#### Scenario: Hide onboarding banner
- **WHEN** user accesses dashboard AND first_name and last_name are both filled
- **THEN** no onboarding banner is displayed

### REMOVED Requirements

### Requirement: Mis CVs button opens CV list modal
**Reason**: CV management removed
**Migration**: Removed entirely; no replacement

### Requirement: Featured resume logic in dashboard
**Reason**: Resume model removed; featured resume concept removed
**Migration**: Public profile displays profile data directly

### Requirement: Social links saved to Resume.content
**Reason**: Resume removed; social links saved to UserProfile JSON fields
**Migration**: Use UserProfile social_links JSONField

### Requirement: Experience/project cards saved to Resume.content
**Reason**: Resume removed; experience/projects saved to UserProfile JSON fields
**Migration**: Use UserProfile experience/projects JSONFields