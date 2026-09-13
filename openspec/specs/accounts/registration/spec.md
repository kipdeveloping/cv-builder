## Purpose

Requerir nombre y apellido durante el registro de usuarios para garantizar que todos los perfiles tengan informaciÃ³n bÃ¡sica completa desde el inicio.

## Requirements

### Requirement: Nombre y apellido obligatorios en registro
El formulario de registro SHALL requerir los campos `first_name` (nombre) y `last_name` (apellido) como obligatorios. El registro NO SHALL completarse si alguno de estos campos estÃ¡ vacÃ­o.

#### Scenario: Registro exitoso con nombre y apellido
- **WHEN** un usuario envÃ­a el formulario de registro con email, contraseÃ±a, nombre y apellido
- **THEN** el sistema crea la cuenta y redirige al dashboard

#### Scenario: Registro fallido sin nombre
- **WHEN** un usuario envÃ­a el formulario de registro sin completar el campo nombre
- **THEN** el sistema muestra un error de validaciÃ³n indicando que el nombre es requerido

#### Scenario: Registro fallido sin apellido
- **WHEN** un usuario envÃ­a el formulario de registro sin completar el campo apellido
- **THEN** el sistema muestra un error de validaciÃ³n indicando que el apellido es requerido

### Requirement: EliminaciÃ³n de la pÃ¡gina complete-profile
El sistema NO SHALL redirigir a los usuarios a una pÃ¡gina de "completar perfil" despuÃ©s del registro. La ruta `/accounts/complete-profile/` NO SHALL existir.

#### Scenario: Acceso a ruta eliminada
- **WHEN** un usuario intenta acceder a `/accounts/complete-profile/`
- **THEN** el sistema retorna un error 404

### Requirement: Middleware actualizado
El middleware `EnsureProfileMiddleware` NO SHALL redirigir a `complete_profile`. El middleware solo verificarÃ¡ que el usuario estÃ© autenticado para proteger rutas requiriendo login.

#### Scenario: Usuario autenticated accede al dashboard
- **WHEN** un usuario autenticado accede al dashboard
- **THEN** el sistema muestra el dashboard sin redirecciones adicionales

### Requirement: Banner de onboarding para usuarios legacy
El dashboard SHALL mostrar un banner para usuarios que no tengan nombre o apellido configurado, permitiÃ©ndoles actualizar estos campos.

#### Scenario: Usuario sin nombre ve el banner
- **WHEN** un usuario autenticado accede al dashboard y no tiene nombre o apellido
- **THEN** el sistema muestra un banner con campos para nombre y apellido y un botÃ³n guardar

#### Scenario: Usuario con nombre no ve el banner
- **WHEN** un usuario autenticado accede al dashboard y tiene nombre y apellido
- **THEN** el sistema no muestra el banner de onboarding

### Requirement: Registro captura título profesional y sector
El formulario de registro SHALL capturar los campos 	itle (cargo/título profesional) y sector (sector profesional) durante el wizard de registro. Estos valores SHALL guardarse directamente en UserProfile.title y UserProfile.sector_name.

#### Scenario: Registro exitoso con título y sector
- **WHEN** un usuario completa el wizard de 3 pasos con email, contraseña, nombre, apellido, título y sector
- **THEN** el sistema crea la cuenta, el UserProfile, y guarda 	itle y sector_name en el perfil

#### Scenario: Registro con título y sector opcionales
- **WHEN** un usuario omite los campos título y/o sector en el paso 3
- **THEN** el sistema crea la cuenta normalmente con 	itle y sector_name vacíos
- **AND** el usuario puede completarlos después desde el dashboard
