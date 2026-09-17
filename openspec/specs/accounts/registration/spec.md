# accounts/registration Specification

## Purpose

Handles new user registration through a 3-step wizard that collects account credentials, personal information, and professional sector classification.

## Requirements

### Requirement: Registration captures professional title and sector
The registration form SHALL capture the title field (professional role/title) and a sector dropdown during the registration wizard. The sector SHALL be selected from a dropdown populated with options from the global SectorTag dictionary.

#### Scenario: Successful registration with title and sector
- **WHEN** a user completes the 3-step wizard with email, password, first name, last name, title, and sector
- **THEN** the system creates the account, UserProfile, and saves title and sector FK on the profile

#### Scenario: Registration with optional title and sector
- **WHEN** a user omits the title and/or sector fields in step 3
- **THEN** the system creates the account normally with empty title and null sector FK
- **AND** the user can complete them later from the dashboard

#### Scenario: Sector selected from dropdown
- **WHEN** the user reaches step 3 of the registration wizard
- **THEN** the system displays a dropdown with SectorTag options from the global dictionary
- **AND** free text input is not allowed for sector
