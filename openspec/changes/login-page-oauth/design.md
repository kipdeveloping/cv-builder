## Context

The project is a Django 4.2 application with email+password authentication. The accounts app has a UserProfile model with OneToOneField to User. The login page currently shows only email+password fields. We need to add OAuth authentication using django-allauth, which is the standard Django library for social authentication.

## Goals / Non-Goals

**Goals:**
- Integrate django-allauth for OAuth authentication
- Support Google, GitHub, and LinkedIn providers
- Maintain existing email+password authentication as fallback
- Allow users to link/unlink OAuth accounts from dashboard
- Handle OAuth profile data (name, email, photo) for auto-registration

**Non-Goals:**
- Social login for admin panel (separate concern)
- OAuth for API authentication (JWT/session-based only)
- Multi-factor authentication (future enhancement)
- Custom OAuth scopes beyond basic profile info

## Decisions

### 1. Library: django-allauth
**Decision**: Use django-allauth for OAuth integration.

**Rationale**: django-allauth is the most mature Django OAuth library. It handles provider integration, callback processing, account linking, and session management. It supports all three required providers (Google, GitHub, LinkedIn) out of the box.

**Alternatives considered**:
- python-social-auth: Rejected - less Django-native, more complex configuration
- django-oauth-toolkit: Rejected - focused on OAuth provider, not consumer
- Custom implementation: Rejected - too much boilerplate, security risk

### 2. Authentication Flow: allauth Default
**Decision**: Use django-allauth's default authentication flow with login redirects.

**Rationale**: allauth handles the complete OAuth flow: redirect to provider → callback → token exchange → user creation/linking → session creation. This minimizes custom code.

**Alternatives considered**:
- AJAX-based OAuth: Rejected - more complex, CSRF concerns, less reliable
- Popup-based OAuth: Rejected - mobile compatibility issues

### 3. Account Linking: Email-Based
**Decision**: Link OAuth accounts to existing users by matching email address.

**Rationale**: User's email from OAuth provider matches their registered email. This is the most intuitive behavior - users expect their OAuth account to link to their existing profile.

**Alternatives considered**:
- Manual linking only: Rejected - poor UX, users expect automatic linking
- No linking: Rejected - creates duplicate accounts

### 4. Profile Data: Auto-Populate
**Decision**: Auto-populate UserProfile with OAuth profile data (name, photo) on first OAuth login.

**Rationale**: Reduces friction for new users. Photo from OAuth provider can be used as profile photo if user hasn't uploaded one.

**Alternatives considered**:
- Skip profile data: Rejected - poor UX, users expect profile to be pre-filled
- Always overwrite: Rejected - would replace user's uploaded photo

### 5. Configuration: Environment Variables
**Decision**: Store OAuth credentials in environment variables, not settings.py.

**Rationale**: Security best practice - credentials should not be in version control. Allows different credentials per environment (dev, staging, production).

**Alternatives considered**:
- Settings.py with local_settings: Rejected - less secure, harder to manage
- .env file with python-decouple: Considered, but environment variables are simpler

## Risks / Trade-offs

**[Risk] Provider API changes** → Mitigation: django-allauth handles most provider changes. Update allauth version if needed.

**[Risk] Account linking conflicts** → Mitigation: Display clear error when OAuth email matches another account. Provide manual linking option.

**[Risk] OAuth provider downtime** → Mitigation: Show appropriate error message, allow fallback to email+password.

**[Trade-off] Additional dependency** → Accepted: django-allauth is well-maintained and widely used.

**[Trade-off] Redirect-based flow** → Accepted: Standard OAuth flow, more reliable than AJAX alternatives.
