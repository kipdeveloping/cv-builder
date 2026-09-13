## Purpose

Controls profile visibility on the talent wall, allowing users to toggle between public (visible on wall) and private (hidden from wall) profiles.

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

### Requirement: Talent wall only shows public profiles
The talent wall API SHALL only return profiles with `is_public` set to true.

#### Scenario: Wall API filters by visibility
- **WHEN** client fetches profiles from /api/wall/cvs/
- **THEN** only profiles with `is_public=true` are returned
- **AND** profiles with `is_public=false` are excluded

#### Scenario: Sector filter applies only to public profiles
- **WHEN** client fetches profiles with sector filter from /api/wall/cvs/?sector=<slug>
- **THEN** only public profiles matching the sector are returned
- **AND** private profiles are excluded regardless of sector match