# CV Builder

Plataforma para crear currículums interactivos basados en plantillas y publicarlos en un tablón de talento público.

## Características

- **3 Plantillas profesionales**: Clásico, Moderno y Creativo
- **Editor visual**: Edición directa en la plantilla con autoguardado
- **Tablón de talentos**: Explora CVs publicados por sector
- **Bilingüe**: Interfaz en español e inglés
- **Validación robusta**: Contraseña segura, validación de archivos
- **Login OAuth**: Autenticación con Google, GitHub y LinkedIn

## Requisitos

- Python 3.10+
- Node.js 18+
- pip
- npm

## Instalación

### 1. Clonar el repositorio

`ash
git clone <url-del-repositorio>
cd crud-cvs
`

### 2. Crear entorno virtual

`ash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
`

### 3. Instalar dependencias de Python

`ash
pip install -r requirements.txt
`

### 4. Instalar dependencias de Node.js

`ash
npm install
`

### 5. Configurar variables de entorno

Copia el archivo de ejemplo y configura tus credenciales:

`ash
cp .env.example .env
`

Edita el archivo .env con tus credenciales:

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

**Nota**: Si no configuras las credenciales OAuth, los botones de redes sociales se mostrarán pero no funcionarán. Puedes usar el login con email y contraseña normal.

### 6. Configurar la base de datos

`ash
python manage.py migrate
`

### 7. Cargar datos iniciales

`ash
python manage.py loaddata fixtures/templates.json fixtures/sectors.json
`

### 8. Crear usuario administrador (opcional)

`ash
python manage.py createsuperuser
`

### 9. Compilar traducciones (requiere gettext)

`ash
python manage.py compilemessages
`

### 10. Compilar CSS con Tailwind

`ash
npm run build:prod
`

### 11. Ejecutar el servidor de desarrollo

`ash
python manage.py runserver
`

Visita http://127.0.0.1:8000/ para ver la aplicación.

## Configuración de OAuth (Opcional)

Para habilitar el login con redes sociales, necesitas crear aplicaciones OAuth en cada proveedor:

### Google OAuth

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Ve a "APIs & Services" > "Credentials"
4. Crea un "OAuth 2.0 Client ID"
5. Configura el "Authorized redirect URIs": http://localhost:8000/complete/google-oauth2/
6. Copia el Client ID y Client Secret en tu .env

### GitHub OAuth

1. Ve a [GitHub Developer Settings](https://github.com/settings/developers)
2. Crea un "New OAuth App"
3. Configura el "Authorization callback URL": http://localhost:8000/complete/github/
4. Copia el Client ID y Client Secret en tu .env

### LinkedIn OAuth

1. Ve a [LinkedIn Developer Portal](https://www.linkedin.com/developers/)
2. Crea una nueva aplicación
3. Ve a "Auth" y agrega el "Authorized redirect URL": http://localhost:8000/complete/linkedin-oauth2/
4. Copia el Client ID y Client Secret en tu .env

## Estructura del proyecto

`
crud-cvs/
├── manage.py
├── requirements.txt
├── package.json
├── crud_cvs/                 # Configuración del proyecto
├── apps/
│   ├── accounts/             # Autenticación y perfil
│   ├── resumes/              # Lógica de CVs
│   └── wall/                 # Tablón público
├── templates/                # Plantillas HTML
├── static/
│   ├── src/input.css         # Fuente de Tailwind
│   ├── css/output.css        # CSS compilado
│   ├── css/templates/        # Estilos por plantilla
│   └── js/                   # JavaScript
├── media/photos/             # Fotos de usuario
├── locale/                   # Traducciones
├── fixtures/                 # Datos iniciales
└── .env.example              # Plantilla de variables de entorno
`

## Uso

### Crear una cuenta

1. Haz clic en "Registrarse"
2. Ingresa tu email y contraseña
3. La contraseña debe tener: 8+ caracteres, 1 mayúscula, 1 número, 1 carácter especial

### Crear un CV

1. Ve al Dashboard
2. Haz clic en "Crear nuevo CV"
3. Selecciona una plantilla
4. Edita los campos directamente en la plantilla
5. Los cambios se guardan automáticamente

### Publicar un CV

1. En el editor, haz clic en "Publicar"
2. Selecciona los sectores correspondientes
3. Elige el sector principal
4. Confirma la publicación

### Explorar el tablón

1. Ve a "Tablón de Tecnologías"
2. Usa los filtros por sector
3. Haz clic en una tarjeta para ver el CV completo

## Tecnologías utilizadas

- **Backend**: Django 4.2
- **Frontend**: HTML, Tailwind CSS v4, JavaScript vanilla
- **Base de datos**: SQLite
- **Autenticación**: Django built-in + python-social-auth
- **i18n**: Django gettext

## Licencia

Este proyecto es para uso educativo.
