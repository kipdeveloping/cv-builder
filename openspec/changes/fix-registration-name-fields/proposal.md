## Why

El formulario de registro permite a los usuarios crear cuentas sin nombre ni apellido (`required=False`). Esto genera una página de redirección `complete-profile` que entra en loop infinito: el middleware redirige a `complete-profile` porque `title`/`sector` están vacíos, pero la vista solo guarda `first_name`/`last_name` sin modificar `title`/`sector`, por lo que el usuario nunca puede avanzar. El botón "Guardar" en el dashboard tampoco funciona para este caso.

## What Changes

- **BREAKING**: Los campos `first_name` y `last_name` en `WizardRegistrationForm` pasan de `required=False` a `required=True`
- Eliminar la página `complete-profile` (vista, template, URL)
- Eliminar el formulario `ProfileOnboardingForm` de `forms.py`
- Eliminar la función `update_name_view` y su ruta `/update-name/`
- Eliminar el banner de onboarding del dashboard (formulario inline de nombre/apellido)
- Actualizar el middleware `EnsureProfileMiddleware` para que ya no redirija a `complete-profile`
- Mantener el banner del dashboard para usuarios legacy que no tengan nombre/apellido

## Capabilities

### New Capabilities
- `accounts/registration`: Requerir nombre y apellido durante el registro de usuarios

### Modified Capabilities
- (ninguna existente se modifica a nivel de spec)

## Impact

- **Archivos Python**: `apps/accounts/forms.py`, `apps/accounts/views.py`, `apps/accounts/urls.py`, `apps/accounts/middleware.py`
- **Templates**: `templates/accounts/register.html`, `templates/accounts/complete_profile.html` (eliminar), `templates/accounts/dashboard.html`
- **JavaScript**: `static/js/dashboard.js` (eliminar handler del onboarding form)
- **Base de datos**: No se requiere migración (campos de `User` ya existen)
- **Usuarios existentes**: No afectados, pueden seguir editando nombre desde el dashboard
