# Configuración de Login Social (OAuth)

Este proyecto usa [django-allauth](https://docs.allauth.org/) para el acceso con
Google, GitHub, Microsoft y Apple. Las credenciales se leen de **variables de
entorno** (`settings.py` → `SOCIALACCOUNT_PROVIDERS`), por lo que no hace falta
crearlas en la base de datos.

## 1. Variables de entorno

Define las variables según el proveedor que quieras habilitar:

| Variable                     | Proveedor | Dónde obtenerla                                        |
| ---------------------------- | --------- | ------------------------------------------------------ |
| `GOOGLE_OAUTH_CLIENT_ID`     | Google    | Google Cloud Console → OAuth Client ID                 |
| `GOOGLE_OAUTH_CLIENT_SECRET` | Google    | Google Cloud Console → OAuth Client Secret             |
| `GITHUB_CLIENT_ID`           | GitHub    | GitHub → Settings → Developer settings → OAuth Apps    |
| `GITHUB_CLIENT_SECRET`       | GitHub    | GitHub → OAuth Apps (Quick setup)                      |
| `MICROSOFT_CLIENT_ID`        | Microsoft | Azure Portal → App registrations → Application ID      |
| `MICROSOFT_CLIENT_SECRET`    | Microsoft | Azure Portal → Certificates & secrets                  |
| `MICROSOFT_TENANT`           | Microsoft | Azure Portal → Directory (tenant) ID. Default `common` |
| `APPLE_CLIENT_ID`            | Apple     | Apple Developer → Services ID (o Bundle ID)            |
| `APPLE_CLIENT_SECRET`        | Apple     | Solo si usas client secret (o usa Key/Team)            |
| `APPLE_KEY_ID`               | Apple     | Apple Developer → Keys → Key ID                        |
| `APPLE_TEAM_ID`              | Apple     | Apple Developer → Membership → Team ID                 |
| `APPLE_PRIVATE_KEY`          | Apple     | Contenido del `.p8` descargado (con saltos `\n`)       |

En local puedes definirlas en la consola antes de arrancar:

```powershell
$env:GOOGLE_OAUTH_CLIENT_ID = "..."
$env:GOOGLE_OAUTH_CLIENT_SECRET = "..."
python manage.py runserver
```

## 2. Redirect URIs de callback

Debes registrar la URI de callback de cada proveedor. En desarrollo usa
`http://localhost:8000`. Reemplaza `HOST` por tu dominio real en producción.

| Proveedor | Redirect URI                                        |
| --------- | --------------------------------------------------- |
| Google    | `http://HOST/accounts/google/login/callback/`       |
| GitHub    | `http://HOST/accounts/github/login/callback/`       |
| Microsoft | `http://HOST/accounts/microsoft/login/callback/`    |
| Apple     | `http://HOST/accounts/apple/login/callback/`        |

Si usas HTTPS, cambia `http://` por `https://`. Recuerda que el dominio debe
coincidir con el `Host` que envía el navegador y estar en `ALLOWED_HOSTS` en
producción.

## 3. Pasos por proveedor

### Google
1. Consola de Google Cloud → crea/proyecta → *OAuth consent screen*.
2. *Credentials* → *Create credentials* → *OAuth client ID* → tipo *Web application*.
3. Añade la Redirect URI de Google. Copia el Client ID y Secret a las variables.

### GitHub
1. GitHub → Settings → Developer settings → OAuth Apps → *New OAuth App*.
2. Homepage URL: `http://HOST/`, Authorization callback URL: la Redirect URI de GitHub.
3. Copia *Client ID* y genera *Client secret*.

### Microsoft (Entra / Azure AD)
1. Azure Portal → *App registrations* → *New registration* (Supported account types: `common` sirve para cualquier cuenta Microsoft).
2. *Authentication* → *Web* → añade la Redirect URI de Microsoft.
3. *Certificates & secrets* → *New client secret*.
4. Usa el *Application (client) ID* y el *client secret*. Ajusta `MICROSOFT_TENANT` si restringes tu tenant.

### Apple (Sign in with Apple)
1. Apple Developer → Certificates, Identifiers & Profiles.
2. Crea un *Service ID* (client_id) y configura *Sign in with Apple* con el redirect.
3. Crea una *Key* para *Sign in with Apple* y descarga el `.p8` (su contenido va en `APPLE_PRIVATE_KEY`, con los saltos de línea como `\n`).
4. Rellena `APPLE_KEY_ID`, `APPLE_TEAM_ID`, `APPLE_CLIENT_ID` y el private key.

## 4. Notas

- El flujo OAuth requiere las claves configuradas: sin ellas, pulsar un botón
  social devolverá un error de autenticación.
- El primer acceso social crea la cuenta y obliga a completar el perfil
  profesional (título o sector) en `/accounts/complete-profile/` antes de entrar
  al resto de secciones.
- Los usuarios que ya existen por email/password pueden vincular cuentas
  sociales desde el panel de allauth (ver `/admin` → Social applications para
  gestión avanzada si algún día se usan credenciales por DB en vez de entorno).