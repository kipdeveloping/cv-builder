## Purpose

Enables visitors to contact candidates via email through a form on the public profile page, using Django's console email backend for development.

## ADDED Requirements

### Requirement: Contact form sends email to candidate
The system SHALL accept contact form submissions from visitors and send an email to the candidate's registered email address.

#### Scenario: Successful contact submission
- **WHEN** visitor submits contact form with valid name, email, and message
- **THEN** the system sends an email to the candidate's User.email
- **AND** the email includes the visitor's name, email, and message
- **AND** the visitor sees a success confirmation

#### Scenario: Console email backend
- **WHEN** contact form is submitted in development
- **THEN** the email is printed to the console (Django console email backend)
- **AND** no actual email is sent

### Requirement: Contact form validation
The system SHALL validate contact form submissions and reject invalid data.

#### Scenario: Missing required fields
- **WHEN** visitor submits contact form with empty name, email, or message
- **THEN** the form returns validation errors
- **AND** no email is sent

#### Scenario: Invalid email format
- **WHEN** visitor submits contact form with invalid email format
- **THEN** the form returns an email validation error
- **AND** no email is sent

### Requirement: Contact form rate limiting
The system SHALL limit the number of contact submissions from the same IP address to prevent abuse.

#### Scenario: Rate limit exceeded
- **WHEN** visitor submits more than 5 contact forms within 1 hour
- **THEN** the system returns a rate limit error
- **AND** no email is sent

### Requirement: Contact email includes context
The contact email SHALL include sufficient context for the candidate to identify the sender and respond.

#### Scenario: Email content
- **WHEN** contact form is successfully submitted
- **THEN** the email subject is "Contacto desde CV Builder - [Candidate Name]"
- **AND** the email body includes visitor name, visitor email, and message
- **AND** the email includes a note that it was sent from the CV Builder platform
