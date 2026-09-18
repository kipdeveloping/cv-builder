## MODIFIED Requirements

### Requirement: Registration captures professional title and sector
The registration form SHALL be a 4-step wizard. Step 1 SHALL capture role selection ("Busco Trabajo" or "Busco Talento"). Step 2 SHALL capture account credentials (email, password). Step 3 SHALL capture personal information (first name, last name). For candidates, step 3 also captures sector. For recruiters, step 3 captures company name and company type. Step 4 SHALL capture role-specific information: sector for candidates, or company sector, work modality, and optional company details for recruiters.

#### Scenario: Candidate registration flow
- **WHEN** a user selects "Busco Trabajo" in step 1
- **THEN** the wizard proceeds with 4 steps: role, credentials, personal info, sector
- **AND** step 3 shows first name and last name fields
- **AND** step 4 shows sector dropdown from SectorTag dictionary

#### Scenario: Recruiter registration flow
- **WHEN** a user selects "Busco Talento" in step 1
- **THEN** the wizard proceeds with 4 steps: role, credentials, company info, company details
- **AND** step 3 shows contact name, last name, company name, and company type
- **AND** step 4 shows sector dropdown, work modality, and optional fields (website, logo, description)

#### Scenario: Successful registration with title and sector
- **WHEN** a user completes the 4-step wizard with all required fields
- **THEN** the system creates the account with appropriate profile type (UserProfile or RecruiterProfile)
- **AND** saves all provided information on the respective profile

#### Scenario: Registration with optional fields
- **WHEN** a user omits optional fields (company logo, description, website)
- **THEN** the system creates the account normally with empty optional fields
- **AND** the user can complete them later from the dashboard

#### Scenario: Sector selected from dropdown
- **WHEN** a user reaches the step with sector selection
- **THEN** the system displays a dropdown with SectorTag options from the global dictionary
- **AND** free text input is not allowed for sector
