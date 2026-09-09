## Purpose

Provides candidates with a comprehensive dashboard for managing their professional profile, including inline editing of all profile fields, experience/project carousel management, social links, skills, and CV organization.

## ADDED Requirements

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

### Requirement: Skills section in sidebar
The sidebar SHALL display user skills as a grid of tags. An edit button SHALL open a modal for adding/removing/reordering skills and setting a primary skill.

#### Scenario: View skills
- **WHEN** user views sidebar
- **THEN** skills are displayed as a tag grid with up to 8 visible skills
- **AND** if more than 8 skills exist, a "+N more" indicator shows

#### Scenario: Edit skills
- **WHEN** user clicks edit button on skills section
- **THEN** a modal opens showing all skills with add/remove controls
- **AND** user can mark one skill as primary
- **AND** changes are saved via POST to /update-profile/

### Requirement: Status badges in sidebar
The sidebar SHALL display employment status badges (search status, availability, location preference). An edit button SHALL open a modal for updating these fields.

#### Scenario: View status badges
- **WHEN** user views sidebar
- **THEN** status badges are displayed showing current search_status, availability, and location_flex values

#### Scenario: Edit status
- **WHEN** user clicks edit button on status section
- **THEN** a modal opens with dropdowns for each status field
- **AND** changes are saved via POST to /update-profile/

### Requirement: Mis CVs button opens CV list modal
The sidebar SHALL have a fixed "Mis Curriculums" button at the bottom. Clicking it SHALL open a modal listing all user resumes with actions.

#### Scenario: Open CV list modal
- **WHEN** user clicks "Mis Curriculums" button
- **THEN** a modal opens showing all resumes with name, status, template, and updated date
- **AND** each resume has Edit, View CV, and Set as Featured buttons

#### Scenario: Set featured resume
- **WHEN** user clicks star icon on a resume in the CV list modal
- **THEN** POST request is sent to /set-featured/ with resume_id
- **AND** the star icon toggles to filled state
- **AND** only one resume can be featured at a time

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
- **AND** on confirmation, the card is removed from the carousel and Resume.content

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
- **AND** changes are saved to Resume.content.social_links

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
