## MODIFIED Requirements

### Requirement: API endpoint for filtered profiles
The system SHALL provide a GET endpoint at /api/wall/profiles/ that accepts sector, rol, especialidad, seniority, location, tags_must, and tags_nice parameters and returns filtered profiles as JSON.

#### Scenario: API returns filtered results by sector
- **WHEN** GET request is sent with sector=tecnologia
- **THEN** system returns JSON array of profiles matching that sector FK

#### Scenario: API filters by location
- **WHEN** GET request is sent with location=remote
- **THEN** system returns only profiles with location_flex='remote'

#### Scenario: API returns all when no filter
- **WHEN** GET request is sent without any parameters
- **THEN** system returns all public profiles

### Requirement: Profile tag matching for wall filtering
The system SHALL match profiles against tag filters regardless of `tag_type`. When a searcher specifies tags_must, profiles that have those tags (regardless of whether saved as 'must' or 'nice') SHALL be included in results.

#### Scenario: Profile with tag matches must-tag filter
- **WHEN** searcher specifies tags_must=javascript
- **AND** a profile has tag 'javascript' saved with tag_type='nice'
- **THEN** the profile IS included in results

#### Scenario: Profile without tag excluded from must-tag filter
- **WHEN** searcher specifies tags_must=javascript
- **AND** a profile does NOT have tag 'javascript'
- **THEN** the profile is excluded from results

### Requirement: Profile tag scoring for relevance
The system SHALL score profiles based on tag matches. Tags matched from the profile SHALL contribute to relevance score regardless of their original `tag_type`.

#### Scenario: Tag match contributes to score
- **WHEN** a profile has tag 'javascript' (any tag_type)
- **AND** searcher includes 'javascript' in tags_must
- **THEN** the profile receives must-tag scoring credit (+15 points)
