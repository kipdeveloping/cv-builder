# profile/skills Specification

## Purpose

Manages the tag-based skills system where users select tags from the global dictionary to determine under which filters their profile appears in the wall.

## Requirements

### Requirement: Skills system with simple tag selection
The system SHALL provide a tag-based skills system where users select tags from the global dictionary. These tags determine under which filters the profile appears in the wall. The must/nice distinction is REMOVED from the profile side.

#### Scenario: Profile selects tags
- **WHEN** user configures their skills in the dashboard
- **THEN** they select tags from the global Tag dictionary
- **AND** all tags are saved with a default tag_type='nice'

#### Scenario: Tags determine wall visibility
- **WHEN** a profile has tags [javascript, react, docker]
- **AND** a searcher filters by tags_must=javascript
- **THEN** the profile appears in results

#### Scenario: No must/nice distinction for profiles
- **WHEN** user selects tags in the dashboard
- **THEN** there is no UI distinction between "must" and "nice" tags
- **AND** all selected tags are treated equally for filtering purposes
