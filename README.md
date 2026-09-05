# CV Builder

Plataforma para crear currículums interactivos basados en plantillas y publicarlos en un tablón de talento público.

## Características

- **3 Plantillas profesionales**: Clásico, Moderno y Creativo
- **Editor visual**: Edición directa en la plantilla con autoguardado
- **Tablón de talentos**: Explora CVs publicados por sector
- **Bilingüe**: Interfaz en español e inglés
- **Validación robusta**: Contraseña segura, validación de archivos

## Requisitos

- Python 3.10+
- Node.js 18+
- pip
- npm

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd crud-cvs
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias de Python

```bash
pip install -r requirements.txt
```

### 4. Instalar dependencias de Node.js

```bash
npm install
```

### 5. Configurar la base de datos

```bash
python manage.py migrate
```

### 6. Cargar datos iniciales

```bash
python manage.py loaddata fixtures/templates.json fixtures/sectors.json
```

### 7. Crear usuario administrador (opcional)

```bash
python manage.py createsuperuser
```

### 8. Compilar traducciones (requiere gettext)

```bash
python manage.py compilemessages
```

### 9. Compilar CSS con Tailwind

```bash
npm run build:prod
```

### 10. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Visita http://127.0.0.1:8000/ para ver la aplicación.

## Estructura del proyecto

```
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
└── fixtures/                 # Datos iniciales
```

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
- **Autenticación**: Django built-in
- **i18n**: Django gettext

## Licencia

Este proyecto es para uso educativo.
