## Context

El proyecto es un CRUD de CVs construido con Django. El formulario de registro usa un wizard de 3 pasos (`WizardRegistrationForm`) con campos `first_name` y `last_name` opcionales. Un middleware (`EnsureProfileMiddleware`) redirige a una página `complete-profile` cuando detecta `title`/`sector` vacíos, pero esta página solo guarda nombre/apellido sin resolver la condición del middleware, causando un loop infinito.

Archivos clave involucrados:
- `apps/accounts/forms.py` - Formulario de registro y onboarding
- `apps/accounts/views.py` - Vistas de registro, complete_profile, update_name
- `apps/accounts/urls.py` - Rutas URL
- `apps/accounts/middleware.py` - Middleware de verificación de perfil
- `templates/accounts/register.html` - Template de registro (wizard de 3 pasos)
- `templates/accounts/complete_profile.html` - Template a eliminar
- `templates/accounts/dashboard.html` - Dashboard con banner de onboarding
- `static/js/dashboard.js` - JavaScript del dashboard

## Goals / Non-Goals

**Goals:**
- Hacer `first_name` y `first_name` obligatorios en el registro
- Eliminar la página `complete-profile` y su loop infinito
- Eliminar código muerto relacionado (`ProfileOnboardingForm`, `update_name_view`)
- Mantener funcionalidad para usuarios legacy sin nombre/apellido

**Non-Goals:**
- Modificar el modelo `UserProfile` (no se requiere migración)
- Cambiar la estructura del wizard de registro (sigue siendo de 3 pasos)
- Eliminar usuarios existentes sin nombre/apellido
- Modificar campos opcionales como `title`/`sector` en el registro

## Decisions

### Decision 1: Cambiar `required=False` a `required=True` en el formulario
**Alternativa A**: Agregar validación custom en el `save()` del formulario
**Alternativa B**: Usar `required=True` en la definición del campo (elegida)

**Razón**: `required=True` es la forma estándar de Django, más simple y directa. El wizard ya tiene validación por paso, así que el usuario ve el error inmediatamente en el paso 2.

### Decision 2: Eliminar `complete_profile_view` y template
**Alternativa A**: Reparar el loop infinito guardando `title`/`sector` en la vista
**Alternativa B**: Eliminar completamente la página (elegida)

**Razón**: La página existe solo para resolver un problema que no debería existir. Con `first_name`/`last_name` requeridos en registro, la página es innecesaria.

### Decision 3: Eliminar `update_name_view` y su ruta
**Alternativa A**: Mantener `update_name_view` para otros usos
**Alternativa B**: Eliminar la vista y ruta (elegida)

**Razón**: `update_name_view` solo era llamada por el banner de onboarding del dashboard. Con el banner eliminado, no tiene uso.

### Decision 4: Eliminar banner de onboarding del dashboard
**Alternativa A**: Mantener el banner para usuarios legacy
**Alternativa B**: Eliminar el banner completamente (elegida)

**Razón**: Los usuarios existentes pueden actualizar su nombre desde el perfil del dashboard (ya existe esa funcionalidad). El banner de onboarding es una solución temporal que ya no se necesita.

### Decision 5: Simplificar el middleware
**Alternativa A**: Eliminar el middleware completamente
**Alternativa B**: Mantener el middleware pero sin la redirección a `complete_profile` (elegida)

**Razón**: El middleware podría ser útil en el futuro para otras verificaciones de perfil. Solo eliminamos la parte de redirección.

### Decision 6: Mantener el wizard de 3 pasos en el registro
**Alternativa A**: Reducir a 2 pasos (datos de acceso + nombre/apellido)
**Alternativa B**: Mantener 3 pasos como está (elegida)

**Razón**: El paso 3 (cargo/título) ya es opcional y el wizard funciona bien. Cambiarlo añadiría riesgo sin beneficio claro.

## Risks / Trade-offs

- **[Riesgo]** Usuarios existentes sin nombre/apellido podrían no entender cómo actualizar sus datos → **Mitigación**: El perfil ya tiene campos editables, y la interfaz es clara
- **[Riesgo]** Eliminar `complete-profile` rompe bookmarks o links guardados → **Mitigación**: Es una ruta interna, no pública. Los usuarios afectados serían redirigidos al dashboard
- **[Trade-off]** Se pierde la funcionalidad de "completar perfil" como paso separado → **Aceptable**: Los datos se obtienen en el registro, que es el momento correcto

## Migration Plan

1. Aplicar cambios en código
2. Ejecutar `python manage.py test` para verificar que no hay regresiones
3. No se requiere migración de base de datos
4. No se requiere rollback específico (los cambios son en código, no en datos)
