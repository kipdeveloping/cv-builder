## MODIFIED Requirements

### Requirement: Registro captura título profesional y sector
El formulario de registro SHALL capturar el campo title (cargo/título profesional) y un dropdown de sector (sector profesional) durante el wizard de registro. El sector SHALL seleccionarse de un dropdown con las opciones del diccionario global SectorTag.

#### Scenario: Registro exitoso con título y sector
- **WHEN** un usuario completa el wizard de 3 pasos con email, contraseña, nombre, apellido, título y sector
- **THEN** el sistema crea la cuenta, el UserProfile, y guarda title y sector FK en el perfil

#### Scenario: Registro con título y sector opcionales
- **WHEN** un usuario omite los campos título y/o sector en el paso 3
- **THEN** el sistema crea la cuenta normalmente con title vacío y sector FK null
- **AND** el usuario puede completarlos después desde el dashboard

#### Scenario: Sector se selecciona de dropdown
- **WHEN** el usuario llega al paso 3 del wizard de registro
- **THEN** el sistema muestra un dropdown con las opciones de SectorTag del diccionario global
- **AND** no se permite entrada de texto libre para sector
