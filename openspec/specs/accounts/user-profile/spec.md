# accounts/user-profile Specification

## Purpose

Defines the UserProfile model that extends User with professional information including photo, bio, visibility settings, sector classification, and language proficiency.

## Requirements

### Requirement: UserProfile model with photo, bio, and visibility
The system SHALL maintain a UserProfile linked one-to-one with each User, containing a photo field, bio text field, and is_public boolean. The profile SHALL use SectorTag foreign key for sector classification. The `sector_name` field is REMOVED.

#### Scenario: Profile created on user registration
- **WHEN** a new user registers
- **THEN** a UserProfile is automatically created with empty photo and bio fields
- **AND** `is_public` defaults to false
- **AND** `sector` FK is set from registration dropdown selection

#### Scenario: Profile stores sector via FK
- **WHEN** user completes registration with sector dropdown
- **THEN** the sector value is stored in `UserProfile.sector` (ForeignKey to SectorTag)
- **AND** the `sector_name` field no longer exists

### Requirement: Title syncs with headline
The system SHALL synchronize `title` and `headline` fields. When one is saved and the other is empty, the empty field SHALL be populated with the saved value.

#### Scenario: Title saved when headline is empty
- **WHEN** user saves a title value AND `headline` is empty
- **THEN** `headline` is set to the same value as `title`

#### Scenario: Headline saved when title is empty
- **WHEN** user saves a headline value AND `title` is empty
- **THEN** `title` is set to the same value as `headline`

#### Scenario: Both fields remain independently editable
- **WHEN** user edits either `title` or `headline`
- **THEN** only the edited field changes
- **AND** the other field retains its value
