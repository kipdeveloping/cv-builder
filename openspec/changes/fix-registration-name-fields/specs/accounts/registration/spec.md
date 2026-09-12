## Purpose

Requerir nombre y apellido durante el registro de usuarios para garantizar que todos los perfiles tengan información básica completa desde el inicio.

## ADDED Requirements

### Requirement: Nombre y apellido obligatorios en registro
El formulario de registro SHALL requerir los campos `first_name` (nombre) y `last_name` (apellido) como obligatorios. El registro NO SHALL completarse si alguno de estos campos está vacío.

#### Scenario: Registro exitoso con nombre y apellido
- **WHEN** un usuario envía el formulario de registro con email, contraseña, nombre y apellido
- **THEN** el sistema crea la cuenta y redirige al dashboard

#### Scenario: Registro fallido sin nombre
- **WHEN** un usuario envía el formulario de registro sin completar el campo nombre
- **THEN** el sistema muestra un error de validación indicando que el nombre es requerido

#### Scenario: Registro fallido sin apellido
- **WHEN** un usuario envía el formulario de registro sin completar el campo apellido
- **THEN** el sistema muestra un error de validación indicando que el apellido es requerido

### Requirement: Eliminación de la página complete-profile
El sistema NO SHALL redirigir a los usuarios a una página de "completar perfil" después del registro. La ruta `/accounts/complete-profile/` NO SHALL existir.

#### Scenario: Acceso a ruta eliminada
- **WHEN** un usuario intenta acceder a `/accounts/complete-profile/`
- **THEN** el sistema retorna un error 404

### Requirement: Middleware actualizado
El middleware `EnsureProfileMiddleware` NO SHALL redirigir a `complete_profile`. El middleware solo verificará que el usuario esté autenticado para proteger rutas requiriendo login.

#### Scenario: Usuario autenticated accede al dashboard
- **WHEN** un usuario autenticado accede al dashboard
- **THEN** el sistema muestra el dashboard sin redirecciones adicionales

### Requirement: Banner de onboarding para usuarios legacy
El dashboard SHALL mostrar un banner para usuarios que no tengan nombre o apellido configurado, permitiéndoles actualizar estos campos.

#### Scenario: Usuario sin nombre ve el banner
- **WHEN** un usuario autenticado accede al dashboard y no tiene nombre o apellido
- **THEN** el sistema muestra un banner con campos para nombre y apellido y un botón guardar

#### Scenario: Usuario con nombre no ve el banner
- **WHEN** un usuario autenticado accede al dashboard y tiene nombre y apellido
- **THEN** el sistema no muestra el banner de onboarding
