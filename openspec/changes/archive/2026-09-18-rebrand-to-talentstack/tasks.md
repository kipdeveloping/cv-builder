## 1. Configurar skip_specs en .openspec.yaml

- [x] 1.1 Agregar `skip_specs: true` al archivo `.openspec.yaml` del cambio y verificar con `openspec validate` que el cambio es válido

## 2. Actualizar branding en base.html

- [x] 2.1 Cambiar el título default de "CV Builder" a "TalentStack" en el bloque `{% block title %}` y verificar que el navbar muestra el nuevo nombre
- [x] 2.2 Cambiar la marca en el navbar de "CV Builder" a "TalentStack" (línea 25) y verificar visualmente
- [x] 2.3 Actualizar el copyright en el footer de "CV Builder" a "TalentStack" (línea 104) y verificar el texto mostrado

## 3. Actualizar localStorage key en darkmode.js

- [x] 3.1 Cambiar `cvbuilder_theme` a `talentstack_theme` en las líneas 22 y 26 de `static/js/darkmode.js` y verificar que el toggle de tema funciona correctamente (la preferencia se guarda y restaura)

## 4. Actualizar email en settings.py

- [x] 4.1 Cambiar `DEFAULT_FROM_EMAIL` de `noreply@cvbuilder.com` a `noreply@talentstack.com` en `crud_cvs/settings.py` línea 134 y verificar que el valor es correcto

## 5. Reescribir landing.html

- [x] 5.1 Reemplazar el hero section con: título "Haz visible tu talento. Encuentra el candidato ideal.", subtítulo sobre la plataforma, CTAs "Registrarme como Candidato" y "Registrarme como Reclutador", y link secundario "Explorar tablón público sin registro →"
- [x] 5.2 Reemplazar la sección de features con 3 columnas: "Perfiles Interactivos", "Búsqueda Avanzada y Scoring", "Un espacio doble", cada una con descripción y icono SVG
- [x] 5.3 Reemplazar el hero final con: título "¿Listo para impulsar tu carrera o escalar tu equipo?", subtítulo "Crea tu perfil en minutos o explora nuestro directorio de empresas y talentos.", y CTA "Crear una cuenta gratis"
- [x] 5.4 Verificar que todos los textos usan `{% trans %}` para compatibilidad i18n

## 6. Actualizar README.md

- [x] 6.1 Cambiar "# CV Builder" a "# TalentStack" en la línea 1 del README.md y verificar que el nombre es consistente en todo el documento

## 7. Verificación final

- [x] 7.1 Ejecutar el servidor de desarrollo y verificar que la landing page muestra correctamente el branding "TalentStack" en navbar, hero, features, hero final, y footer
- [x] 7.2 Verificar que el toggle de dark mode funciona y persiste la preferencia con el nuevo localStorage key
- [x] 7.3 Verificar que la función de idioma funciona correctamente en la landing page
