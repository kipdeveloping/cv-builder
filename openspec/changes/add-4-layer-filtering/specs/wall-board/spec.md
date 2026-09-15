## MODIFIED Requirements

### Requirement: AJAX sector filtering
The system SHALL replace simple sector buttons with hierarchical dropdown filters for Sector, Role, Specialty, and Tags, plus global attribute filters (Seniority, Languages). Filters are independent and can be combined freely.

#### Scenario: Filter dropdowns displayed
- **WHEN** talent wall loads
- **THEN** system displays dropdown filters for Sector, Role, Specialty, plus collapsible tag selector and global filters

#### Scenario: Filter by sector dropdown
- **WHEN** user selects "Tecnología" from Sector dropdown
- **THEN** system updates results to show only Tecnología profiles and updates Role dropdown options

#### Scenario: Filter by role only
- **WHEN** user selects "Dev Web" from Role dropdown without selecting Sector
- **THEN** system updates results to show all Dev Web profiles regardless of sector

#### Scenario: Clear all filters
- **WHEN** user clicks "Limpiar filtros" button
- **THEN** system clears all selections and shows all profiles

### Requirement: API endpoint for filtered CVs
The system SHALL provide a GET endpoint at /api/wall/profiles/ that accepts multiple filter parameters (sector, rol, especialidad, tags_must, tags_nice, seniority, languages) and returns filtered profiles with relevance scores as JSON.

#### Scenario: API returns filtered results with scores
- **WHEN** GET request is sent with sector=tecnologia&tags_must=django
- **THEN** system returns JSON array of profiles matching criteria, each with a score field (0-100)

#### Scenario: API excludes profiles missing must tags
- **WHEN** GET request is sent with tags_must=django,typescript
- **AND** profile has django but not typescript
- **THEN** profile is excluded from results

#### Scenario: API ranks by nice tag matches
- **WHEN** GET request is sent with tags_nice=react,aws
- **AND** profile has react but not aws
- **THEN** profile receives partial score bonus for react match

#### Scenario: API returns all when no filter
- **WHEN** GET request is sent without any parameters
- **THEN** system returns all published profiles with score=0

### Requirement: Tag hierarchy API endpoint
The system SHALL provide a GET endpoint at /api/tags/hierarchy/ that returns the complete tag hierarchy (sectors > roles > specialties > tags) as nested JSON.

#### Scenario: API returns full hierarchy
- **WHEN** GET request is sent to /api/tags/hierarchy/
- **THEN** system returns JSON with sectors array, each containing roles array, each containing specialties array, each containing tags array

#### Scenario: API returns filtered hierarchy
- **WHEN** GET request is sent with sector=tecnologia
- **THEN** system returns only Tecnología sector with its roles, specialties, and tags

### Requirement: Real-time search with scoring display
Search results SHALL update instantly when any filter changes. Each profile card SHALL display its relevance score as a percentage badge.

#### Scenario: Instant results update
- **WHEN** user changes any filter
- **THEN** results update within 500ms without page reload

#### Scenario: Score displayed on card
- **WHEN** profile has score 85%
- **THEN** card displays score badge showing "85%"

#### Scenario: Results sorted by score
- **WHEN** results contain multiple profiles
- **THEN** profiles are ordered by score descending (highest first)
