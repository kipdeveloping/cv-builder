## 1. Setup

- [x] 1.1 Install social-auth-app-django and add to requirements.txt, verify installation with pip install
- [x] 1.2 Configure social-auth in Django settings (INSTALLED_APPS, AUTHENTICATION_BACKENDS, SOCIAL_AUTH_PIPELINE)
- [x] 1.3 Set up social-auth URL patterns in project urls.py
- [x] 1.4 Create database migrations for social-auth and run migrate

## 2. OAuth Provider Configuration

- [x] 2.1 Configure Google OAuth provider in settings (SOCIAL_AUTH_GOOGLE_OAUTH2_KEY/SECRET from env vars)
- [x] 2.2 Configure GitHub OAuth provider in settings (SOCIAL_AUTH_GITHUB_KEY/SECRET from env vars)
- [x] 2.3 Configure LinkedIn OAuth provider in settings (SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY/SECRET from env vars)
- [x] 2.4 Create .env.example file with OAuth credential placeholders

## 3. Login Page Integration

- [x] 3.1 Create login.html template with OAuth buttons below email+password form
- [x] 3.2 Style OAuth buttons with provider brand colors and icons
- [x] 3.3 Add conditional rendering to hide OAuth buttons when credentials not configured
- [x] 3.4 Test OAuth redirect flow for each provider

## 4. OAuth Callback Handling

- [x] 4.1 Configure social-auth callback URLs for each provider
- [x] 4.2 Test OAuth callback and account creation for new users
- [x] 4.3 Test OAuth callback and account linking for existing users with matching email
- [x] 4.4 Handle OAuth errors (provider unavailable, permission denied)

## 5. Profile Auto-Population

- [x] 5.1 Create social-auth pipeline to auto-populate UserProfile on first OAuth login
- [x] 5.2 Extract and save user name from OAuth profile data
- [x] 5.3 Download and save OAuth profile photo as UserProfile photo
- [x] 5.4 Test profile auto-population for each provider

## 6. Social Account Management

- [x] 6.1 Create account settings template with linked accounts section
- [x] 6.2 Display list of linked OAuth providers with status
- [x] 6.3 Add "Link" button for unlinked providers
- [x] 6.4 Add "Unlink" button with confirmation dialog for linked providers
- [x] 6.5 Prevent unlinking last authentication method (show set password prompt)

## 7. Testing

- [x] 7.1 Test complete OAuth login flow for Google provider
- [x] 7.2 Test complete OAuth login flow for GitHub provider
- [x] 7.3 Test complete OAuth login flow for LinkedIn provider
- [x] 7.4 Test account linking when OAuth email matches existing user
- [x] 7.5 Test error handling for OAuth failures
- [x] 7.6 Test social account management (link/unlink)
