## MODIFIED Requirements

### Requirement: Public profile page accessible by user ID
The system SHALL provide a public profile page at `/candidato/<user_id>/` that displays the candidate's professional information. **The profile SHALL only be accessible if the target user's profile has `is_public=true`.**

#### Scenario: Access public profile
- **WHEN** visitor navigates to `/candidato/<user_id>/` AND target profile has `is_public=true`
- **THEN** the system displays the candidate's profile with sidebar and main area layout
- **AND** the page uses the same visual design as the dashboard

#### Scenario: Access private profile returns 404
- **WHEN** visitor navigates to `/candidato/<user_id>/` AND target profile has `is_public=false`
- **THEN** the system returns a 404 page
- **AND** no profile information is leaked

#### Scenario: Non-existent user
- **WHEN** visitor navigates to `/candidato/<nonexistent_id>/`
- **THEN** the system returns a 404 page

### Requirement: Profile displays profile data directly (no resume fallback)
The profile SHALL display data directly from the UserProfile model and its JSON fields (experience, projects, social_links, etc.). **There is no fallback to Resume data since the Resume model is removed.**

#### Scenario: Profile displays profile data
- **WHEN** visitor views a public profile
- **THEN** sidebar displays photo, name, headline, bio, title, sector_name, status badges
- **AND** main area displays experience/project carousel from UserProfile JSON fields
- **AND** social links from UserProfile JSON fields

#### Scenario: No experience/projects
- **WHEN** visitor views a public profile with no experience or projects
- **THEN** carousel is empty with appropriate empty state message
- **AND** no error is displayed

### Requirement: Sidebar displays read-only profile information
The sidebar SHALL display the candidate's photo, name, headline, bio, title, sector_name, and status badges without any edit controls.

#### Scenario: View sidebar as visitor
- **WHEN** visitor views the profile sidebar
- **THEN** photo, name, headline, title, sector_name, bio, and status badges are displayed
- **AND** no edit buttons or modals are present

### Requirement: Main area displays experience/project carousel
The main area SHALL display the candidate's experience and project cards in a carousel format, without edit or delete buttons.

#### Scenario: View carousel as visitor
- **WHEN** visitor views the main area
- **THEN** experience and project cards are displayed in a horizontal carousel
- **AND** navigation arrows allow scrolling
- **AND** no edit or delete buttons are visible on cards

### Requirement: Main area displays social links
The main area SHALL display social link icons that link to the candidate's configured URLs.

#### Scenario: View social links as visitor
- **WHEN** visitor views the main area
- **THEN** social link icons are displayed for platforms with configured URLs
- **AND** clicking an icon opens the URL in a new tab

### Requirement: Contact form for visitors
The profile page SHALL include a "Contactar" button that opens a modal with a contact form. The form SHALL collect visitor's name, email, and message, then send it to the candidate's registered email.

#### Scenario: Open contact form
- **WHEN** visitor clicks "Contactar" button
- **THEN** a modal opens with fields for name, email, and message
- **AND** the modal displays the candidate's name as the recipient

#### Scenario: Submit contact form
- **WHEN** visitor fills in name, email, and message AND clicks Send
- **THEN** a POST request is sent to /contact/<user_id>/
- **AND** the system sends an email to the candidate's registered email address
- **AND** the visitor sees a success message

#### Scenario: Invalid contact form
- **WHEN** visitor submits contact form with missing required fields
- **THEN** the form displays validation errors
- **AND** no email is sent

### Requirement: Owner detection and indicator
If the logged-in user is viewing their own profile, the page SHALL display an indicator and a link back to the dashboard.

#### Scenario: Owner views own profile
- **WHEN** authenticated user views their own profile page
- **THEN** a banner or indicator shows "Este es tu perfil publico"
- **AND** a link to the dashboard is displayed

#### Scenario: Visitor views other profile
- **WHEN** visitor views another user's profile
- **THEN** no owner indicator is displayed
- **AND** the "Contactar" button is visible

### REMOVED Requirements

### Requirement: Profile displays featured or most recent published resume
**Reason**: Resume model removed; profile displays UserProfile data directly
**Migration**: Profile reads from UserProfile and its JSON fields

### Requirement: Photo required before publishing (CV)
**Reason**: CV publishing removed; profile visibility toggle requires photo instead
**Migration**: Handled by profile/visibility capability