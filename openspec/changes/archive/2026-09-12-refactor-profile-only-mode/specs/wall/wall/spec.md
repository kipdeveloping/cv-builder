## MODIFIED Requirements

### Requirement: Wall displays public profiles only
El tablón SHALL mostrar solo perfiles con `is_public=true`.

#### Scenario: Wall API filters by visibility
- **WHEN** client fetches profiles from /api/wall/profiles/
- **THEN** only profiles with `is_public=true` are returned
- **AND** profiles with `is_public=false` are excluded

#### Scenario: Wall displays profile data
- **WHEN** visitor views a profile card on the wall
- **THEN** card displays: photo, full name, headline/bio preview, sector_name
- **AND** photo uses fallback SVG if no photo uploaded

### Requirement: Wall filtering by sector
El tablón SHALL soportar filtrado de perfiles por sector usando el campo `sector_name`.

#### Scenario: Filter by sector
- **WHEN** client fetches profiles with sector parameter /api/wall/profiles/?sector=<slug>
- **THEN** only public profiles with matching sector_name are returned

#### Scenario: Sector filter chips in UI
- **WHEN** visitor views the wall page
- **THEN** sector filter chips are rendered from SectorTag model
- **AND** "Todos" chip shows all public profiles

### Requirement: Wall API includes user ID in response
El endpoint API del tablón SHALL incluir el user_id en cada entrada de perfil para permitir la navegación a perfiles de candidatos.

#### Scenario: API response includes user_id
- **WHEN** client fetches profiles from /api/wall/profiles/
- **THEN** each profile object includes a `user_id` field
- **AND** the user_id can be used to construct a profile URL at `/candidato/<user_id>/`

### Requirement: Profile cards navigate to profile page
Las tarjetas de perfil del tablón SHALL enlazar a la página de perfil del candidato en `/candidato/<user_id>/`.

#### Scenario: Click profile card on wall
- **WHEN** visitor clicks on a profile card in the wall grid
- **THEN** the browser navigates to `/candidato/<user_id>/`

### Requirement: Tags API returns SectorTag from accounts
El API de tags SHALL retornar objetos SectorTag de la app accounts para uso en la UI de filtrado del tablón.

#### Scenario: Fetch tags
- **WHEN** client fetches /api/tags/
- **THEN** response includes SectorTag objects with id, slug, name
