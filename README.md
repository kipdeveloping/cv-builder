# TalentStack

Plataforma web para crear perfiles profesionales interactivos y conectar talento con empresas. Permite a los candidatos crear y publicar sus perfiles, y a los reclutadores discover talento y publicar vacantes.

## Características principales

### Para candidatos (trabajadores)

- **Dashboard personalizado**: Panel de control con acceso rápido a todas las funciones del perfil
- **Perfil profesional público**: Página de perfil en /candidato/<id>/ con foto, bio, experiencia, proyectos y habilidades
- **Control de visibilidad**: Decide si tu perfil es público o privado
- **Tags de habilidades**: Etiqueta tu perfil con tecnologías y skills (obligatorios y deseables)
- **Información laboral**: Estado de búsqueda, disponibilidad, tipo de empleo, disponibilidad para mudarse/viajar
- **Seniority y sector**: Clasifica tu nivel (Junior, Semi-Senior, Senior, Lead) y sector profesional
- **Idiomas**: Registra los idiomas que hablas y su nivel
- **Links sociales**: LinkedIn, GitHub, Twitter, Portfolio
- **Contacto directo**: Formulario de contacto para que reclutadores se comuniquen contigo

### Para reclutadores (empresas)

- **Dashboard de reclutador**: Panel especializado para gestión de vacantes
- **Perfil de empresa público**: Página de perfil en /empresa/<id>/ con logo, descripción y vacantes activas
- **Gestión de vacantes**: Crear, editar y publicar ofertas laborales
- **Información de empresa**: Nombre, logo, sector, tipo (Empresa Directa o Reclutador Independiente), modalidad de trabajo
- **Control de visibilidad**: Decide si el perfil de empresa es público o privado
- **Links sociales**: LinkedIn, Twitter de la empresa

### Tablón de talentos (para candidatos)

- **Exploración de perfiles**: Grid de tarjetas con perfiles de candidatos públicos
- **Filtros avanzados**:
  - Sector (jerarquía: Sector > Rol > Especialidad)
  - Tags obligatorios (AND) y deseables (OR)
  - Seniority (Junior, Semi-Senior, Senior, Lead)
  - Modalidad (Remoto, Híbrido, Presencial)
- **Scoring de relevancia**: Los perfiles se ordenan por relevancia según los filtros aplicados
- **Navegación rápida**: Click en tarjeta para ver perfil completo

### Tablón de empresas (para reclutadores)

- **Exploración de empresas**: Grid de tarjetas con perfiles de empresas públicas
- **Filtros facetados**:
  - Sector (multi-select con búsqueda)
  - Modalidad (checkboxes OR: Remoto, Híbrido, Presencial)
  - Tipo de reclutador (radio: Todos, Empresa Directa, Reclutador Independiente)
- **Navegación rápida**: Click en tarjeta para ver perfil de empresa y vacantes

### Autenticación y seguridad

- **Registro con wizard**: Formulario paso a paso con selección de rol (Candidato o Reclutador)
- **Login OAuth**: Autenticación con Google, GitHub y LinkedIn
- **Restricciones OAuth**: Solo Google y LinkedIn disponibles para reclutadores (correos corporativos)
- **Validación de contraseña**: Mínimo 8 caracteres, 1 mayúscula, 1 número, 1 carácter especial
- **Recuperación de contraseña**: Flujo completo de reset por email
- **Cambio de contraseña**: Desde la configuración de cuenta

### Internacionalización

- **Bilingüe**: Interfaz completa en español e inglés
- **Cambio de idioma**: Selector de idioma en el navbar
- **Contenido bilingüe**: Sectores, roles, especialidades y tags en ambos idiomas

### Diseño y UX

- **Dark mode**: Toggle de tema claro/oscuro con persistencia en localStorage
- **Responsive**: Diseño adaptable a desktop, tablet y móvil
- **Tailwind CSS v4**: Estilos modernos con utility-first CSS
- **Iconos SVG**: Iconos inline para mejor rendimiento

## Rutas principales

| Ruta | Descripción |
|------|-------------|
| / | Landing page |
| /tablon/ | Tablón de talentos (candidatos) |
| /tablon-empresas/ | Tablón de empresas (reclutadores) |
| /candidato/<id>/ | Perfil público de candidato |
| /empresa/<id>/ | Perfil público de empresa |
| /accounts/login/ | Inicio de sesión |
| /accounts/register/ | Registro de usuario |
| /accounts/dashboard/ | Dashboard (candidato o reclutador) |
| /accounts/settings/ | Configuración de cuenta |
| /admin/ | Panel de administración Django |

## API Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| /api/wall/profiles/ | GET | Perfiles de candidatos con filtros |
| /api/wall/recruiters/ | GET | Perfiles de empresas con filtros facetados |
| /api/tags/ | GET | Lista de sectores |
| /api/tags/hierarchy/ | GET | Jerarquía completa Sector > Rol > Especialidad > Tags |
| /api/tags/all/ | GET | Todos los tags con búsqueda |
| /accounts/api/profile/tags/ | GET | Tags del perfil del usuario actual |
| /accounts/api/profile/tags/save/ | POST | Guardar tags del perfil |

## Estructura del proyecto

`
crud-cvs/
+-- manage.py
+-- requirements.txt
+-- package.json
+-- crud_cvs/                    # Configuración del proyecto Django
¦   +-- settings.py
¦   +-- urls.py
¦   +-- wsgi.py
+-- apps/
¦   +-- accounts/                # Autenticación, perfiles y gestión de usuarios
¦   ¦   +-- models.py           # UserProfile, RecruiterProfile, Vacancy, SectorTag, Tag
¦   ¦   +-- views.py            # Vistas de auth, dashboard, perfiles
¦   ¦   +-- urls.py             # Rutas de cuentas
¦   ¦   +-- forms.py            # Formularios de registro y login
¦   ¦   +-- pipeline.py         # Pipeline de OAuth
¦   ¦   +-- signals.py          # Señales de Django
¦   +-- wall/                    # Tablón público
¦       +-- views.py            # Vistas del tablón y APIs
¦       +-- urls.py             # Rutas del tablón
+-- templates/                   # Plantillas HTML
¦   +-- base.html               # Template base con navbar
¦   +-- landing.html            # Página de inicio
¦   +-- accounts/
¦   ¦   +-- dashboard.html      # Dashboard de candidato
¦   ¦   +-- recruiter_dashboard.html  # Dashboard de reclutador
¦   ¦   +-- profile.html        # Perfil público de candidato
¦   ¦   +-- recruiter_profile.html    # Perfil público de empresa
¦   ¦   +-- login.html
¦   ¦   +-- register.html
¦   ¦   +-- account_settings.html
¦   +-- wall/
¦       +-- wall.html           # Tablón de talentos
¦       +-- recruiter_wall.html # Tablón de empresas
+-- static/
¦   +-- src/input.css           # Fuente de Tailwind CSS
¦   +-- css/output.css          # CSS compilado
¦   +-- js/
¦       +-- wall.js             # Lógica del tablón de talentos
¦       +-- recruiter_wall.js   # Lógica del tablón de empresas
¦       +-- profile.js          # Lógica de perfil
¦       +-- darkmode.js         # Toggle de tema
¦       +-- language.js         # Selector de idioma
+-- media/                       # Archivos subidos por usuarios
¦   +-- photos/                 # Fotos de perfil
¦   +-- company_logos/          # Logos de empresa
+-- locale/                      # Traducciones
+-- fixtures/                    # Datos iniciales
¦   +-- templates.json
¦   +-- sectors.json
+-- openspec/                    # Documentación de especificaciones
    +-- specs/                  # Specs del proyecto
    +-- changes/                # Historial de cambios
`

## Modelos de datos

### UserProfile (Candidatos)
- user - Relación OneToOne con User de Django
- photo - Foto de perfil
- io, headline - Biografía y titular
- is_public - Visibilidad del perfil
- sector, 
ol, especialidad - Clasificación profesional
- seniority - Nivel (Junior, Semi-Senior, Senior, Lead)
- location_flex - Modalidad preferida (Remoto, Híbrido, Presencial)
- search_status - Estado de búsqueda
- vailability - Disponibilidad
- employment_type - Tipo de empleo deseado
- experience, projects - Experiencia y proyectos (JSON)
- social_links - Redes sociales (JSON)
- languages - Idiomas (JSON)

### RecruiterProfile (Empresas)
- user - Relación OneToOne con User de Django
- company_name - Nombre de la empresa
- company_logo - Logo de la empresa
- company_sector - Sector de la empresa
- company_type - Tipo (Empresa Directa o Particular)
- work_modality - Modalidad de trabajo
- company_description - Descripción de la empresa
- company_website - Sitio web
- is_public - Visibilidad del perfil
- social_links - Redes sociales (JSON)

### Vacancy (Vacantes)
- 
ecruiter_profile - Relación con RecruiterProfile
- 	itle, description - Título y descripción
- 
equirements - Requisitos (JSON)
- location, modality - Ubicación y modalidad
- salary_range - Rango salarial
- employment_type - Tipo de empleo
- status - Estado (Activa, Cerrada, Borrador)

### SectorTag, SectorRol, RolEspecialidad, Tag
- Sistema jerárquico de clasificación: Sector > Rol > Especialidad > Tags
- Bilingüe (name_es, name_en)
- Tags con categorías (Lenguaje, Framework, Herramienta, Soft Skill)

## Tecnologías utilizadas

- **Backend**: Django 4.2+
- **Frontend**: HTML5, Tailwind CSS v4, JavaScript vanilla
- **Base de datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Autenticación**: Django built-in + python-social-auth
- **Internacionalización**: Django gettext (i18n)
- **Imágenes**: Pillow
- **Formularios**: django-crispy-forms + crispy-bootstrap5
- **Variables de entorno**: python-decouple

## Requisitos

- Python 3.10+
- Node.js 18+
- pip
- npm
- gettext (para traducciones)

## Instalación

### 1. Clonar el repositorio

`ash
git clone https://github.com/kipdeveloping/cv-builder.git
cd crud-cvs
`

### 2. Crear entorno virtual

`ash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
`

### 3. Instalar dependencias

`ash
pip install -r requirements.txt
npm install
`

### 4. Configurar variables de entorno

`ash
cp .env.example .env
`

Edita .env con tus credenciales:

`env
# Django
SECRET_KEY=tu-secret-key-aqui
DEBUG=True

# Google OAuth (opcional)
GOOGLE_CLIENT_ID=tu_google_client_id
GOOGLE_CLIENT_SECRET=tu_google_client_secret

# GitHub OAuth (opcional)
GITHUB_KEY=tu_github_client_id
GITHUB_SECRET=tu_github_client_secret

# LinkedIn OAuth (opcional)
LINKEDIN_CLIENT_ID=tu_linkedin_client_id
LINKEDIN_CLIENT_SECRET=tu_linkedin_client_secret
`

### 5. Configurar la base de datos

`ash
python manage.py migrate
python manage.py loaddata fixtures/templates.json fixtures/sectors.json
`

### 6. Compilar assets y traducciones

`ash
npm run build:prod
python manage.py compilemessages
`

### 7. Ejecutar el servidor

`ash
python manage.py runserver
`

Visita http://127.0.0.1:8000/

## Configuración de OAuth (Opcional)

### Google OAuth

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un proyecto y habilita "Google+ API"
3. Ve a "APIs & Services" > "Credentials"
4. Crea "OAuth 2.0 Client ID"
5. Authorized redirect URIs: http://localhost:8000/complete/google-oauth2/
6. Copia Client ID y Secret en .env

### GitHub OAuth

1. Ve a [GitHub Developer Settings](https://github.com/settings/developers)
2. Crea "New OAuth App"
3. Authorization callback URL: http://localhost:8000/complete/github/
4. Copia Client ID y Secret en .env

### LinkedIn OAuth

1. Ve a [LinkedIn Developer Portal](https://www.linkedin.com/developers/)
2. Crea una aplicación
3. Auth > Authorized redirect URL: http://localhost:8000/complete/linkedin-oauth2/
4. Copia Client ID y Secret en .env

**Nota**: Si no configuras OAuth, los botones de redes sociales se mostrarán pero no funcionarán. Puedes usar login con email y contraseña.

## Licencia

Este proyecto es para uso educativo.
