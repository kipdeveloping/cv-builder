## Purpose

Provides OAuth authentication via Google, GitHub, and LinkedIn, allowing users to sign in or register using their existing social accounts without creating new credentials.

## ADDED Requirements

### Requirement: OAuth login buttons on login page
The system SHALL display OAuth login buttons for Google, GitHub, and LinkedIn on the login page, positioned below the email+password form.

#### Scenario: OAuth buttons displayed
- **WHEN** user navigates to the login page
- **THEN** system displays buttons for Google, GitHub, and LinkedIn with respective brand icons

#### Scenario: OAuth button clicked
- **WHEN** user clicks an OAuth provider button
- **THEN** system redirects to the provider's authorization page

### Requirement: OAuth registration flow
The system SHALL allow new users to register using OAuth without requiring a separate registration form.

#### Scenario: New user OAuth registration
- **WHEN** user authenticates via OAuth for the first time
- **THEN** system creates a new user account with the email from the OAuth provider
- **AND** system creates a UserProfile with the name and photo from the OAuth provider

#### Scenario: Existing email OAuth registration
- **WHEN** user authenticates via OAuth and the email already exists in the system
- **THEN** system links the OAuth account to the existing user
- **AND** system does not create a duplicate account

### Requirement: OAuth callback handling
The system SHALL handle OAuth callbacks from all three providers and complete the authentication process.

#### Scenario: Successful OAuth callback
- **WHEN** OAuth provider redirects back with a valid authorization code
- **THEN** system exchanges the code for an access token
- **AND** system retrieves user profile information
- **AND** system creates or links the user account
- **AND** system redirects to the dashboard

#### Scenario: OAuth callback with error
- **WHEN** OAuth provider redirects back with an error
- **THEN** system displays an error message and redirects to the login page

### Requirement: OAuth provider error handling
The system SHALL handle OAuth errors gracefully and provide user-friendly error messages.

#### Scenario: Provider unavailable
- **WHEN** OAuth provider is unavailable or returns an error
- **THEN** system displays a message indicating the provider is temporarily unavailable

#### Scenario: OAuth permission denied
- **WHEN** user denies permission on the OAuth provider
- **THEN** system redirects to the login page with an informational message

### Requirement: OAuth credentials configuration
The system SHALL support OAuth provider credentials via environment variables for secure configuration.

#### Scenario: Environment variables configured
- **WHEN** OAuth credentials are set in environment variables
- **THEN** system uses those credentials for OAuth authentication

#### Scenario: Missing OAuth credentials
- **WHEN** OAuth credentials are not configured
- **THEN** system hides the corresponding OAuth button from the login page
