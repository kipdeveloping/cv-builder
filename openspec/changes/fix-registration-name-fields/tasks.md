## 1. Formulario de Registro

- [x] 1.1 Cambiar `required=False` a `required=True` en los campos `first_name` y `last_name` de `WizardRegistrationForm` en `apps/accounts/forms.py` y verificar que el formulario requiere estos campos
- [x] 1.2 Eliminar la clase `ProfileOnboardingForm` de `apps/accounts/forms.py` y verificar que no hay errores de importación

## 2. Vistas y URLs

- [x] 2.1 Eliminar la función `complete_profile_view` de `apps/accounts/views.py` y verificar que no hay errores de sintaxis
- [x] 2.2 Eliminar la función `update_name_view` de `apps/accounts/views.py` y verificar que no hay errores de sintaxis
- [x] 2.3 Eliminar la ruta `path('complete-profile/', ...)` de `apps/accounts/urls.py` y verificar que la URL ya no existe
- [x] 2.4 Eliminar la ruta `path('update-name/', ...)` de `apps/accounts/urls.py` y verificar que la URL ya no existe
- [x] 2.5 Eliminar el import de `ProfileOnboardingForm` de `apps/accounts/views.py` si existe

## 3. Middleware

- [x] 3.1 Eliminar la lógica de redirección a `complete_profile` de `EnsureProfileMiddleware` en `apps/accounts/middleware.py` y verificar que el middleware solo verifica autenticación

## 4. Templates

- [x] 4.1 Eliminar el archivo `templates/accounts/complete_profile.html` y verificar que no hay referencias rotas
- [x] 4.2 Eliminar el banner de onboarding (div amarillo con formulario de nombre/apellido) de `templates/accounts/dashboard.html` y verificar que el dashboard se muestra correctamente

## 5. JavaScript

- [x] 5.1 Eliminar el handler del formulario de onboarding (`onboarding-form`) de `static/js/dashboard.js` y verificar que no hay errores de JavaScript

## 6. Verificación

- [x] 6.1 Ejecutar `python manage.py test` para verificar que no hay regresiones en las pruebas existentes
- [x] 6.2 Verificar manualmente que el registro de usuario nuevo requiere nombre y apellido
- [x] 6.3 Verificar que la ruta `/accounts/complete-profile/` retorna 404
- [x] 6.4 Verificar que el dashboard se carga correctamente para usuarios con y sin nombre/apellido
