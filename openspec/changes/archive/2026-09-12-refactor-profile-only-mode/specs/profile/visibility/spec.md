## ADDED Requirements

### Requirement: User can toggle profile visibility
The system SHALL provide a mechanism for authenticated users to toggle their profile visibility between public and private.

#### Scenario: Toggle profile to public
- **WHEN** authenticated user clicks the visibility toggle in the dashboard sidebar
- **THEN** the system sets the user's profile `is_public` field to true
- **AND** the profile becomes visible on the talent wall immediately

#### Scenario: Toggle profile to private
- **WHEN** authenticated user clicks the visibility toggle in the dashboard sidebar
- **THEN** the system sets the user's profile `is_public` field to false
- **AND** the profile is removed from the talent wall immediately

#### Scenario: Default visibility is private
- **WHEN** a new user registers
- **THEN** the system creates their profile with `is_public` set to false
- **AND** the profile does not appear on the talent wall until explicitly made public
