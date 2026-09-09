# Wall Specification

## Purpose

Provides the talent wall functionality that displays published CVs in a filterable grid, with navigation to candidate profiles.

## Requirements

### Requirement: Wall API includes user ID in response
The wall API endpoint SHALL include the user_id in each CV entry response to enable navigation to candidate profiles.

#### Scenario: API response includes user_id
- **WHEN** client fetches CVs from /api/wall/
- **THEN** each CV object includes an `id` field (resume ID) and a `user_id` field (user ID)
- **AND** the user_id can be used to construct a profile URL

### Requirement: CV cards navigate to profile instead of CV detail
Wall CV cards SHALL link to the candidate's profile page instead of the CV detail page.

#### Scenario: Click CV card on wall
- **WHEN** visitor clicks on a CV card in the wall grid
- **THEN** the browser navigates to `/candidato/<user_id>/`
- **AND** NOT to `/cv/<resume_id>/`

### Requirement: CV detail page includes Ver Perfil button
The CV detail page SHALL include a "Ver Perfil Completo" button that links to the candidate's profile page.

#### Scenario: View CV detail page
- **WHEN** visitor views a CV at `/cv/<resume_id>/`
- **THEN** a "Ver Perfil Completo" button is displayed
- **AND** clicking the button navigates to `/candidato/<user_id>/`

### Requirement: Wall displays skill tags from profile
Wall CV cards SHALL display skill tags from the user's UserSkill model instead of or in addition to resume tags.

#### Scenario: View CV card with skills
- **WHEN** visitor views a CV card on the wall
- **THEN** skill tags from UserSkill.objects.filter(user=cv.user) are displayed
- **AND** up to 3 primary skills are shown
