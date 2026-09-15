## Purpose

Enables multi-filter search with independent filters, MUST/HAVE exclusion logic, and NICE TO HAVE weighted scoring to rank candidates by relevance percentage (0-100%).

## ADDED Requirements

### Requirement: Independent filter selection
Filters SHALL be independent and can be combined freely without requiring sequential selection. Users can apply any combination of Sector, Role, Specialty, and Tags.

#### Scenario: Filter by sector only
- **WHEN** user selects sector="Tecnología" without other filters
- **THEN** system returns all profiles in Tecnología sector

#### Scenario: Filter by role only
- **WHEN** user selects role="Dev Web" without sector filter
- **THEN** system returns all profiles with Dev Web role regardless of sector

#### Scenario: Filter by multiple criteria
- **WHEN** user selects sector="Tecnología", role="Dev Web", seniority="Senior"
- **THEN** system returns profiles matching all three criteria

### Requirement: Tag filtering with MUST logic
Profiles that do NOT have ALL tags marked as "must" by the user SHALL be excluded from results.

#### Scenario: Profile has all must tags
- **WHEN** user searches with must_tags=["Django", "TypeScript"]
- **AND** profile has both Django and TypeScript as must tags
- **THEN** profile is included in results

#### Scenario: Profile missing must tag
- **WHEN** user searches with must_tags=["Django", "TypeScript"]
- **AND** profile has Django but not TypeScript
- **THEN** profile is excluded from results

#### Scenario: No must tags specified
- **WHEN** user searches without specifying must_tags
- **THEN** all profiles pass this filter regardless of their tags

### Requirement: Tag filtering with NICE logic
Profiles with tags matching user's "nice" preferences SHALL receive score bonuses but SHALL NOT be excluded.

#### Scenario: Profile has nice tags
- **WHEN** user searches with nice_tags=["React", "AWS"]
- **AND** profile has React as nice tag
- **THEN** profile receives bonus score for React match

#### Scenario: Profile has no nice tags
- **WHEN** user searches with nice_tags=["React", "AWS"]
- **AND** profile has neither React nor AWS
- **THEN** profile is still included with base score

### Requirement: Weighted scoring system
The system SHALL calculate a relevance score from 0% to 100% using weighted points:
- Sector match: +30 points
- Role match: +25 points
- Specialty match: +20 points
- Each must tag match: +15 points
- Each nice tag match: +10 points

Maximum score is the sum of all weights for filters actually applied.

#### Scenario: Calculate score with all filters
- **WHEN** user applies sector(30) + role(25) + specialty(20) + 2 must tags(15+15) + 2 nice tags(10+10)
- **AND** profile matches all criteria
- **THEN** score = 30+25+20+15+15+10+10 = 125 points = 100% (normalized)

#### Scenario: Calculate score with partial match
- **WHEN** user applies sector(30) + role(25) + 1 must tag(15)
- **AND** profile matches sector and role but not must tag
- **THEN** profile is excluded (must tag not matched)

#### Scenario: Calculate score with nice tag variation
- **WHEN** user applies sector(30) + 2 nice tags(10+10)
- **AND** profile matches sector and 1 of 2 nice tags
- **THEN** score = 30+10 = 40 points out of max 50 = 80%

### Requirement: Global attribute filters
The system SHALL support filtering by seniority and languages as cross-sector attributes.

#### Scenario: Filter by seniority
- **WHEN** user selects seniority="Senior"
- **THEN** system returns only profiles with seniority="senior"

#### Scenario: Filter by language
- **WHEN** user selects language="en" with level="B2"
- **THEN** system returns profiles with English B2 or higher

#### Scenario: No global filters
- **WHEN** user does not specify seniority or language filters
- **THEN** all profiles pass these filters

### Requirement: Real-time search
Search results SHALL update instantly when any filter changes without requiring a submit button.

#### Scenario: Change sector filter
- **WHEN** user changes sector from "Tecnología" to "Salud"
- **THEN** results update within 500ms showing Salud profiles

#### Scenario: Add tag filter
- **WHEN** user adds must_tag="Django" to existing filters
- **THEN** results update within 500ms excluding profiles without Django

### Requirement: Score display
Each profile card in results SHALL display its relevance score as a percentage.

#### Scenario: Show score on card
- **WHEN** profile has score 85%
- **THEN** card displays "85%" badge or indicator

#### Scenario: Sort by score
- **WHEN** results contain profiles with scores 100%, 85%, 72%
- **THEN** profiles are ordered 100% → 85% → 72%
