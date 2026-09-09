# Social Account Management Specification

## Purpose

Allows users to manage their linked OAuth accounts from the dashboard, including viewing connected providers, linking new accounts, and unlinking existing accounts.

## Requirements

### Requirement: Display linked OAuth accounts
The system SHALL display a list of linked OAuth accounts in the user's dashboard settings.

#### Scenario: View linked accounts
- **WHEN** user navigates to account settings
- **THEN** system displays all linked OAuth providers with their email and connection status

#### Scenario: No linked accounts
- **WHEN** user has no linked OAuth accounts
- **THEN** system displays a message indicating no OAuth accounts are linked

### Requirement: Link new OAuth account
The system SHALL allow users to link additional OAuth accounts from the dashboard.

#### Scenario: Link new provider
- **WHEN** user clicks "Link" button for an unlinked provider
- **THEN** system redirects to the OAuth provider's authorization page

#### Scenario: Link successful
- **WHEN** user successfully authorizes with the OAuth provider
- **THEN** system links the account and displays it in the linked accounts list

#### Scenario: Link with existing email
- **WHEN** user attempts to link an OAuth account with an email already linked to another user
- **THEN** system displays an error message indicating the account is already in use

### Requirement: Unlink OAuth account
The system SHALL allow users to unlink OAuth accounts, with safeguards to prevent account lockout.

#### Scenario: Unlink provider
- **WHEN** user clicks "Unlink" button for a linked provider
- **THEN** system displays a confirmation dialog

#### Scenario: Unlink successful
- **WHEN** user confirms unlinking
- **THEN** system removes the OAuth link and displays a success message

#### Scenario: Prevent unlinking last authentication method
- **WHEN** user attempts to unlink their only authentication method (no password set and only one OAuth account)
- **THEN** system prevents unlinking and displays a message indicating they must set a password first

### Requirement: Account security indicators
The system SHALL display security indicators for each authentication method.

#### Scenario: Show authentication methods
- **WHEN** user views account settings
- **THEN** system displays password status (set/not set) and linked OAuth providers