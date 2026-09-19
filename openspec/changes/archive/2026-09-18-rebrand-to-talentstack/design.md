## Context

El proyecto es una aplicación Django con templates Jinja2, Tailwind CSS v4, y JavaScript vanilla. El branding actual "CV Builder" está distribuido en:
- `templates/base.html` (navbar, footer, título)
- `templates/landing.html` (hero section, features, CTA)
- `static/js/darkmode.js` (localStorage key)
- `crud_cvs/settings.py` (email domain)

No hay dependencias externas ni cambios de arquitectura. Es un cambio de contenido estático.

## Goals / Non-Goals

**Goals:**
- Renombrar "CV Builder" a "TalentStack" en toda la UI visible
- Reescribir el landing page con nuevo copy orientado a plataforma de talento
- Mantener consistencia en el naming (localStorage, email)
- Preservar la funcionalidad existente sin regresiones

**Non-Goals:**
- Cambiar comportamiento del sistema (auth, perfiles, tablón, filtros)
- Modificar modelos de datos o esquemas de base de datos
- Actualizar traducciones (locale) - se hará en un cambio futuro
- Cambiar URLs o rutas existentes
- Actualizar OAuth flows o configuración de autenticación

## Decisions

### 1. Modificar `.openspec.yaml` para `skip_specs: true`

**Decisión**: Agregar `skip_specs: true` al archivo `.openspec.yaml` del cambio.

**Razón**: Este es un cambio puramente cosmético (textos, branding). No hay cambios de comportamiento del sistema que requieran specs. Los specs describen comportamiento observable, y nada de eso cambia aquí.

**Alternativas consideradas**:
- Crear specs vacíos: Rechazado porque viola el principio de que specs describen comportamiento
- No agregar `skip_specs`: Rechazado porque `openspec validate` rechaza cambios con cero deltas sin ese marker

### 2. Reescribir `landing.html` completo

**Decisión**: Reemplazar el contenido completo de `landing.html` en lugar de hacer ediciones quirúrgicas.

**Razón**: El cambio de copy es tan extenso (hero, features, CTA final) que las ediciones individuales serían más propensas a errores y más difíciles de revisar.

**Alternativas consideradas**:
- Ediciones quirúrgicas por línea: Más riesgo de inconsistencia
- Crear un nuevo template: innecesario, el path de la URL no cambia

### 3. Renombrar localStorage key

**Decisión**: Cambiar `cvbuilder_theme` a `talentstack_theme` en `darkmode.js`.

**Razón**: Consistencia con el nuevo branding. Los usuarios pierden su preferencia de tema una vez, pero es un impacto menor.

**Alternativas consideradas**:
- Mantener el key viejo: Rompe consistencia del naming
- Migrar el valor: Complejidad innecesaria para un cambio menor

### 4. Usar tag `{% trans %}` para textos traducibles

**Decision**: Envoler los nuevos textos del landing con `{% trans %}` para mantener la compatibilidad con el sistema i18n existente.

**Razón**: El proyecto ya usa `{% load i18n %}` y tiene 8 idiomas configurados. Aunque las traducciones no se actualizarán ahora, los textos deben estar listos para cuando se traduzcan.

## Risks / Trade-offs

**[Risk] Usuarios existentes pierden preferencia de tema** → Mitigación: Impacto menor, solo afecta el toggle dark/light. Los usuarios lo re-configuran en 1 click.

**[Risk] Búsqueda rompe si alguien busca "CV Builder"** → Mitigación: El nombre "CV Builder" solo aparece en la UI, no en datos de usuario ni en URLs. No hay búsqueda de texto completo sobre el nombre de la app.

**[Risk] Email "noreply@talentstack.com" no existe** → Mitigación: El email backend está configurado en modo consola (`console.EmailBackend`). Ningún email real se envía en desarrollo. En producción, se debe configurar el dominio real antes de deploy.
