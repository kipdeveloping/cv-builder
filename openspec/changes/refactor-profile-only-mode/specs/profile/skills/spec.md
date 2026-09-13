## REMOVED Requirements

### Requirement: User can manage skills on dashboard
**Reason**: Skill and UserSkill models removed entirely; skills system will be rebuilt later as a tag/filter system independent of profiles
**Migration**: Remove skills grid from sidebar, remove skills edit modal, remove skills API endpoints. No data migration needed as skills data is ephemeral.

#### Scenario: View skills on dashboard (REMOVED)
- **WHEN** user views sidebar skills section
- **THEN** no skills section is displayed

#### Scenario: Edit skills via modal (REMOVED)
- **WHEN** user clicks edit skills button
- **THEN** no skills modal exists

#### Scenario: Primary skill designation (REMOVED)
- **WHEN** user marks a skill as primary
- **THEN** no primary skill concept exists

### Requirement: Skills displayed on talent wall cards
**Reason**: Skill/UserSkill models removed; wall displays sector_name instead
**Migration**: Wall cards show sector_name; skills to be reimplemented later

#### Scenario: Wall card shows skills (REMOVED)
- **WHEN** visitor views wall card
- **THEN** no skill tags displayed; sector_name shown instead

### Requirement: Skills synced from resume content
**Reason**: Resume model removed; sync function removed
**Migration**: Remove `sync_skills_from_resume` function and all calls to it

### Requirement: Skill model with unique name and slug
**Reason**: Entire skills system removed
**Migration**: Drop Skill and UserSkill tables via migration

### Requirement: UserSkill links UserProfile to Skill
**Reason**: Entire skills system removed
**Migration**: Drop UserSkill table via migration

### ADDED Requirements (for future reimplementation)

### Requirement: Skills system placeholder
The system SHALL reserve the `profile/skills` capability for future reimplementation as a tag/filter system. No functional requirements in this change.

#### Scenario: Future skills implementation
- **WHEN** skills system is reimplemented
- **THEN** it will be a new capability with independent tag/filter architecture
- **AND** will not depend on current Skill/UserSkill models