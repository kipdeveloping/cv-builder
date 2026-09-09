## Why

The current authentication system only supports email+password login. Users expect OAuth options for faster, more convenient sign-in. Adding Google, GitHub, and LinkedIn OAuth reduces registration friction and aligns with modern authentication standards.

## What Changes

- **New OAuth integration** using django-allauth for Google, GitHub, and LinkedIn providers
- **Modified login page** with OAuth buttons alongside existing email+password form
- **Modified registration flow** to handle OAuth profile linking and auto-account creation
- **New social account management** in dashboard for linking/unlinking OAuth providers
- **Updated authentication backend** to support multiple authentication methods

## Capabilities

### New Capabilities

- `accounts/oauth-providers`: OAuth authentication via Google, GitHub, and LinkedIn using django-allauth
- `accounts/social-account-management`: Dashboard UI for managing linked OAuth accounts

### Modified Capabilities

- `accounts/user-auth`: Extended login page with OAuth buttons, modified authentication flow to support OAuth alongside email+password

## Impact

- **Dependencies**: django-allauth package (OAuth library for Django)
- **Settings**: New ALLAUTH settings, provider credentials (Google Client ID, GitHub Client ID, LinkedIn Client ID)
- **Templates**: Modified login.html with OAuth buttons, new social account management template
- **URLs**: New allauth callback URLs for OAuth providers
- **Database**: django-allauth social account tables (auto-migrated)
- **Environment variables**: OAuth provider credentials (GOOGLE_CLIENT_ID, GITHUB_CLIENT_ID, LINKEDIN_CLIENT_ID)
