## Purpose

Provides a structured skill taxonomy that enables skill-based filtering and search, with automatic synchronization from Resume.content JSON data to relational models.

## ADDED Requirements

### Requirement: Skill model with unique names
The system SHALL maintain a Skill model with unique name and slug fields for each skill in the taxonomy.

#### Scenario: Create new skill
- **WHEN** a skill name is encountered that does not exist in the Skill model
- **THEN** a new Skill record is created with the name and a URL-safe slug

#### Scenario: Duplicate skill name
- **WHEN** a skill name already exists in the Skill model
- **THEN** the existing Skill record is reused (no duplicate created)

### Requirement: UserSkill association with primary flag
The system SHALL maintain a UserSkill model that associates users with skills, with a boolean flag to mark one skill as primary.

#### Scenario: Add skill to user
- **WHEN** a skill is added to a user's profile
- **THEN** a UserSkill record is created linking the UserProfile to the Skill
- **AND** if it is the user's first skill, it is automatically marked as primary

#### Scenario: Set primary skill
- **WHEN** user marks a skill as primary
- **THEN** the UserSkill record for that skill has is_primary=True
- **AND** all other UserSkill records for that user have is_primary=False

### Requirement: Automatic skills sync from Resume.content
The system SHALL automatically synchronize skills from Resume.content.skills[] to the UserSkill model whenever a resume is saved.

#### Scenario: Sync skills on resume save
- **WHEN** a resume is saved via POST to /api/resume/save/
- **THEN** the system extracts skills[] from the content JSON
- **AND** for each skill name, ensures a Skill record exists
- **AND** ensures a UserSkill record exists linking the user to the skill
- **AND** removes UserSkill records for skills no longer in the JSON
- **AND** preserves the primary flag on existing UserSkills

#### Scenario: Multiple resumes with different skills
- **WHEN** a user has multiple resumes with different skills
- **THEN** the union of all skills from all resumes is reflected in UserSkill records
- **AND** skills are only removed if they appear in NO resume

### Requirement: Skills displayed in sidebar
The dashboard and profile pages SHALL display skills from the UserSkill model, not directly from Resume.content.

#### Scenario: View skills on dashboard
- **WHEN** user views dashboard sidebar
- **THEN** skills are loaded from UserSkill.objects.filter(user=profile)
- **AND** skills are displayed as a tag grid

#### Scenario: View skills on public profile
- **WHEN** visitor views public profile sidebar
- **THEN** skills are loaded from UserSkill.objects.filter(user=profile)
- **AND** skills are displayed as a tag grid
