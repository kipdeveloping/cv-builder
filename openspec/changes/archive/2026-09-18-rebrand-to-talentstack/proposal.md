## Why

El proyecto actual se llama "CV Builder" pero la propuesta de valor ha evolucionado: ya no es solo un creador de CVs, sino una plataforma completa de matching entre talento y empresas. El nombre "TalentStack" refleja mejor esta visión: un stack de talento donde candidatos muestran su perfil real y reclutadores filtran por scoring y especialidad. El rebranding alinea la identidad del producto con su funcionalidad real.

## What Changes

- **Renombrar marca**: "CV Builder" → "TalentStack" en navbar, footer, y toda la UI
- **Reescribir landing page**: Nuevo hero section con copy orientado a plataforma de talento, features actualizadas (Perfiles Interactivos, Búsqueda Avanzada y Scoring, Espacio Doble), y CTA final renovado
- **Renombrar localStorage key**: `cvbuilder_theme` → `talentstack_theme` para consistencia
- **Actualizar email**: `noreply@cvbuilder.com` → `noreply@talentstack.com`
- **Actualizar documentación**: README refleja el nuevo nombre

## Capabilities

### New Capabilities

Ninguno. Este cambio es puramente cosmético (textos, branding, contenido estático). No introduce nuevas capacidades ni modifica comportamiento existente.

### Modified Capabilities

Ninguno. El comportamiento del sistema (autenticación, perfiles, tablón, filtros, etc.) no cambia.

## Impact

- **Templates**: `templates/base.html` (navbar, footer, título), `templates/landing.html` (reescribir completo)
- **JavaScript**: `static/js/darkmode.js` (cambiar localStorage key)
- **Configuración**: `crud_cvs/settings.py` (email domain)
- **Documentación**: `README.md`
- **No afecta**: Modelos, URLs, vistas, lógica de negocio, APIs, traducciones (locale)
