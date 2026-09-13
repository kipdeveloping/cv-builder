## MODIFIED Requirements

### Requirement: Registro captura título profesional y sector
El formulario de registro SHALL capturar los campos `title` (cargo/título profesional) y `sector` (sector profesional) durante el wizard de registro. Estos valores SHALL guardarse directamente en `UserProfile.title` y `UserProfile.sector_name`.

#### Scenario: Registro exitoso con título y sector
- **WHEN** un usuario completa el wizard de 3 pasos con email, contraseña, nombre, apellido, título y sector
- **THEN** el sistema crea la cuenta y el UserProfile, y guarda `title` y `sector_name` en el perfil

#### Scenario: Registro con título y sector opcionales
- **WHEN** un usuario omite los campos título y/o sector en el paso 3
- **THEN** el sistema crea la cuenta normalmente con `title` y `sector_name` vacíos
- **AND** el usuario puede completarlos después desde el dashboard
