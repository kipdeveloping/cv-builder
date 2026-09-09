## Why

The current login page only supports email/password authentication. Users expect to log in with their existing Google, GitHub, or LinkedIn accounts for convenience. This change adds OAuth-based login with account linking, allowing users to connect their existing accounts with third-party providers.

## What Changes

- Redesign the login page layout: large app name centered at top, "Iniciar Sesion" title, login form, and OAuth buttons
- Add OAuth integration for Google, GitHub, and LinkedIn using `python-social-auth`
- Implement account linking logic: if a user authenticates via OAuth and an existing account matches by email, link the OAuth provider to that account
- Reject new user creation via OAuth (future task) - show error message if no matching account exists
- Add custom pipeline step to handle the "no matching account" case with user-friendly error display

## Capabilities

### New Capabilities

- `accounts/oauth-login`: OAuth-based login flow with Google, GitHub, and LinkedIn providers, including account linking for existing users and error handling for unmatched accounts

### Modified Capabilities

- `profile/public-profile`: Minor - the login page is part of the public-facing authentication flow, but requirements don't change, only the entry point

## Impact

- **Dependencies**: New dependency `social-auth-app-django` (Python package)
- **Settings**: `crud_cvs/settings.py` - add `social_django` to INSTALLED_APPS, configure AUTHENTICATION_BACKENDS, provider keys, custom pipeline
- **URLs**: `crud_cvs/urls.py` - add `social_django.urls`
- **Templates**: `templates/accounts/login.html` - full redesign with OAuth buttons
- **New files**: `apps/accounts/pipeline.py` - custom pipeline function
- **External**: Requires OAuth app registration on Google Cloud Console, GitHub Developer Settings, and LinkedIn Developer Portal
