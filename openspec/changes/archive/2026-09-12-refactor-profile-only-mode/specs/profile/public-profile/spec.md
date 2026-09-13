## MODIFIED Requirements

### Requirement: Public profile page accessible by user ID
El sistema SHALL proveer una página de perfil público en `/candidato/<user_id>/` que muestre la información profesional del candidato. El perfil SHALL solo ser accesible si el perfil del usuario objetivo tiene `is_public=true`.

#### Scenario: Access public profile
- **WHEN** visitor navigates to `/candidato/<user_id>/` AND target profile has `is_public=true`
- **THEN** the system displays the candidate's profile with sidebar and main area layout

#### Scenario: Access private profile returns 404
- **WHEN** visitor navigates to `/candidato/<user_id>/` AND target profile has `is_public=false`
- **THEN** the system returns a 404 page

#### Scenario: Non-existent user
- **WHEN** visitor navigates to `/candidato/<nonexistent_id>/`
- **THEN** the system returns a 404 page

### Requirement: Profile displays profile data directly
El perfil SHALL mostrar datos directamente del modelo UserProfile y sus campos JSON (experiencia, proyectos, enlaces sociales, etc.). No hay respaldo con datos de Resume ya que el modelo Resume fue eliminado.

#### Scenario: Profile displays profile data
- **WHEN** visitor views a public profile
- **THEN** sidebar displays photo, name, headline, bio, title, sector_name, status badges
- **AND** main area displays experience/project carousel from UserProfile JSON fields

#### Scenario: No experience/projects
- **WHEN** visitor views a public profile with no experience or projects
- **THEN** carousel is empty with appropriate empty state message

### Requirement: Sidebar displays read-only profile information
La barra lateral SHALL mostrar la foto, nombre, titular, bio, sector_name y badges de estado del candidato sin controles de edición.

#### Scenario: View sidebar as visitor
- **WHEN** visitor views the profile sidebar
- **THEN** photo, name, headline, title, sector_name, bio, and status badges are displayed
- **AND** no edit buttons or modals are present
