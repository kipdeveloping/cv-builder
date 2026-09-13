## MODIFIED Requirements

### Requirement: Wall API includes user ID in response
The wall API endpoint SHALL include the user_id in each profile entry response to enable navigation to candidate profiles.

#### Scenario: API response includes user_id
- **WHEN** client fetches profiles from /api/wall/cvs/
- **THEN** each profile object includes a `user_id` field (user ID)
- **AND** the user_id can be used to construct a profile URL at `/candidato/<user_id>/`

### Requirement: Profile cards navigate to profile page
Wall profile cards SHALL link to the candidate's profile page at `/candidato/<user_id>/`.

#### Scenario: Click profile card on wall
- **WHEN** visitor clicks on a profile card in the wall grid
- **THEN** the browser navigates to `/candidato/<user_id>/`
- **AND** NOT to `/cv/<resume_id>/`

### Requirement: Wall displays public profiles only
The wall SHALL only display profiles with `is_public=true`.

#### Scenario: Wall API filters by visibility
- **WHEN** client fetches profiles from /api/wall/cvs/
- **THEN** only profiles with `is_public=true` are returned
- **AND** profiles with `is_public=false` are excluded

#### Scenario: Wall displays profile data
- **WHEN** visitor views a profile card on the wall
- **THEN** card displays: photo, full name, headline/bio preview, sector_name
- **AND** photo uses fallback SVG if no photo uploaded

### Requirement: Wall filtering by sector
The wall SHALL support filtering profiles by sector using the `sector_name` field.

#### Scenario: Filter by sector
- **WHEN** client fetches profiles with sector parameter /api/wall/cvs/?sector=<slug>
- **THEN** only public profiles with matching sector_name are returned
- **AND** sector filter matches case-insensitively

#### Scenario: Sector filter chips in UI
- **WHEN** visitor views the wall page
- **THEN** sector filter chips are rendered from SectorTag model (for future filtering)
- **AND** "Todos" chip shows all public profiles

### Requirement: Tags API returns SectorTag from accounts
The tags API SHALL return SectorTag objects from the accounts app for use in wall filtering UI.

#### Scenario: Fetch tags
- **WHEN** client fetches /api/tags/
- **THEN** response includes SectorTag objects with id, slug, name
- **AND** tags sourced from accounts.SectorTag model

### REMOVED Requirements

### Requirement: CV detail page includes Ver Perfil button
**Reason**: CV detail page removed; wall cards navigate directly to profile
**Migration**: Direct navigation to `/candidato/<user_id>/`

### Requirement: Wall displays skill tags from profile
**Reason**: Skill/UserSkill models removed; skills system will be rebuilt later
**Migration**: Wall displays sector_name instead; skills to be reimplemented

### Requirement: CV cards link to CV detail
**Reason**: CV detail page removed
**Migration**: Cards link to profile page