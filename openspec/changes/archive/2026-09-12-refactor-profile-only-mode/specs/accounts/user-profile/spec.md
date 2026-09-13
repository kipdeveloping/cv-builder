## MODIFIED Requirements

### Requirement: UserProfile model with photo, bio, and visibility
El sistema SHALL mantener un UserProfile vinculado uno a uno con cada User, conteniendo campos de foto, bio, is_public, sector_name y título profesional. El perfil NO SHALL referenciar Resume ni SectorTag mediante foreign keys.

#### Scenario: Profile created on user registration
- **WHEN** a new user registers
- **THEN** a UserProfile is automatically created with empty photo and bio fields
- **AND** `is_public` defaults to false

#### Scenario: Profile stores sector as text
- **WHEN** user completes registration with sector field
- **THEN** the sector value is stored in `UserProfile.sector_name` (CharField)
- **AND** no SectorTag foreign key is created or referenced

#### Scenario: Profile stores professional title
- **WHEN** user completes registration with title field
- **THEN** the title value is stored in `UserProfile.title` (CharField)

### Requirement: Photo upload from dashboard
El sistema SHALL permitir a los usuarios subir o cambiar su foto de perfil desde el dashboard.

#### Scenario: Successful photo upload
- **WHEN** user selects a valid image file (jpg, png, webp) under 5MB
- **THEN** system saves the photo and displays it in the dashboard and on the public profile page

#### Scenario: Photo upload with invalid file type
- **WHEN** user attempts to upload a file that is not jpg, png, or webp
- **THEN** system rejects the upload with an error message indicating allowed formats

#### Scenario: Photo upload exceeds size limit
- **WHEN** user attempts to upload a file larger than 5MB
- **THEN** system rejects the upload with an error message indicating the size limit

### Requirement: Bio field for talent wall display
El sistema SHALL almacenar un texto de bio en el UserProfile que se muestra en las tarjetas del tablón de talentos.

#### Scenario: User edits bio
- **WHEN** user updates their bio text in the dashboard
- **THEN** system saves the bio and it appears on their talent wall card (if profile is public)

### Requirement: Photo required for public profile visibility
El sistema SHALL prevenir que los usuarios hagan público su perfil sin haber subido una foto de perfil.

#### Scenario: Toggle public without photo
- **WHEN** user attempts to set `is_public=true` without a profile photo
- **THEN** system blocks the toggle and prompts user to upload a photo first

### Requirement: Profile visibility toggle
El sistema SHALL proveer un endpoint API para alternar el campo `is_public` en UserProfile.

#### Scenario: Toggle visibility via API
- **WHEN** authenticated user POSTs to /accounts/toggle-visibility/
- **THEN** system toggles the `is_public` field on the user's profile
- **AND** returns the new visibility state
