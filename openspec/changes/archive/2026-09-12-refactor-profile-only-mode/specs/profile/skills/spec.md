## REMOVED Requirements

### Requirement: User can manage skills on dashboard
**Reason**: Skill and UserSkill models removed entirely; skills system will be rebuilt later as a tag/filter system independent of profiles
**Migration**: Remove skills grid from sidebar, remove skills edit modal, remove skills API endpoints.

#### Scenario: View skills on dashboard (REMOVED)
- **WHEN** user views sidebar skills section
- **THEN** no skills section is displayed

#### Scenario: Edit skills via modal (REMOVED)
- **WHEN** user clicks edit skills button
- **THEN** no skills modal exists

### Requirement: Skills displayed on talent wall cards
**Reason**: Skill/UserSkill models removed; wall displays sector_name instead
**Migration**: Wall cards show sector_name; skills to be reimplemented later

#### Scenario: Wall card shows skills (REMOVED)
- **WHEN** visitor views wall card
- **THEN** no skill tags displayed; sector_name shown instead

### Requirement: Skills system placeholder
El sistema SHALL reservar la capacidad `profile/skills` para future reimplementación como sistema de tags/filtros. No hay requisitos funcionales en este cambio.

#### Scenario: Future skills implementation
- **WHEN** skills system is reimplemented
- **THEN** it will be a new capability with independent tag/filter architecture
