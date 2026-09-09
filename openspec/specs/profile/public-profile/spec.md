# Public Profile Specification

## Purpose

Provides a public-facing candidate profile page that displays the same content as the owner's dashboard but without edit controls, enabling visitors to view professional information and contact candidates.

## Requirements

### Requirement: Public profile page accessible by user ID
The system SHALL provide a public profile page at `/candidato/<user_id>/` that displays the candidate's professional information.

#### Scenario: Access public profile
- **WHEN** visitor navigates to `/candidato/<user_id>/`
- **THEN** the system displays the candidate's profile with sidebar and main area layout
- **AND** the page uses the same visual design as the dashboard

#### Scenario: Non-existent user
- **WHEN** visitor navigates to `/candidato/<nonexistent_id>/`
- **THEN** the system returns a 404 page

### Requirement: Profile displays featured or most recent published resume
The profile SHALL display data from the user's featured resume (resume_destacado). If no featured resume is set, it SHALL fall back to the most recent published resume.

#### Scenario: Featured resume exists
- **WHEN** user has a resume_destacado set AND that resume is published
- **THEN** profile displays data from the featured resume

#### Scenario: No featured resume
- **WHEN** user has no resume_destacado set
- **THEN** profile displays data from the most recently published resume

#### Scenario: No published resumes
- **WHEN** user has no published resumes
- **THEN** profile displays a message indicating no published CVs

### Requirement: Sidebar displays read-only profile information
The sidebar SHALL display the candidate's photo, name, headline, skills, bio, and status badges without any edit controls.

#### Scenario: View sidebar as visitor
- **WHEN** visitor views the profile sidebar
- **THEN** photo, name, headline, skills grid, bio, and status badges are displayed
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
