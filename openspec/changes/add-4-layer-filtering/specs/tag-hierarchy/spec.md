## Purpose

Provides a hierarchical tag dictionary system with 4 layers (Sector, Role, Specialty, Tags) that allows structured classification of professional skills and enables profile tagging with MUST/NICE_TO_HAVE associations.

## ADDED Requirements

### Requirement: Hierarchical tag structure
The system SHALL maintain a 4-layer hierarchical tag dictionary with the following structure:
- Layer 1: Sector (e.g., Tecnología, Marketing, Salud)
- Layer 2: Role (e.g., Dev Web, Growth Marketer, Enfermero)
- Layer 3: Specialty (e.g., Backend, B2B, UCI)
- Layer 4: Tags (e.g., Django, TypeScript, Meta Ads)

Each layer SHALL belong to its parent layer (Role belongs to Sector, Specialty belongs to Role, Tags may optionally belong to Specialty).

#### Scenario: Create sector
- **WHEN** admin creates a new Sector with name_es="Tecnología", name_en="Technology", slug="tecnologia"
- **THEN** system stores the sector and it becomes available for role assignment

#### Scenario: Create role under sector
- **WHEN** admin creates a new Role with name_es="Dev Web", sector=tecnologia
- **THEN** system stores the role linked to the Tecnología sector

#### Scenario: Create specialty under role
- **WHEN** admin creates a new Specialty with name_es="Backend", sector_rol=dev-web
- **THEN** system stores the specialty linked to the Dev Web role

#### Scenario: Create tag with optional specialty
- **WHEN** admin creates a new Tag with name_es="Django", category="framework", especialidad=backend
- **THEN** system stores the tag linked to the Backend specialty

#### Scenario: Create tag without specialty
- **WHEN** admin creates a new Tag with name_es="Python", category="lenguaje", especialidad=null
- **THEN** system stores the tag as a global tag not tied to any specialty

### Requirement: Tag categories
Tags SHALL have a category field with the following allowed values: lenguaje, framework, herramienta, soft_skill, otro.

#### Scenario: Tag with valid category
- **WHEN** admin creates a tag with category="framework"
- **THEN** system accepts and stores the tag

#### Scenario: Tag with invalid category
- **WHEN** admin creates a tag with category="invalid"
- **THEN** system rejects with validation error

### Requirement: Bilingual support
All tag layers SHALL support bilingual names (name_es and name_en) and a unique slug.

#### Scenario: Get tag name in Spanish
- **WHEN** tag has name_es="Django" and name_en="Django"
- **AND** user language is Spanish
- **THEN** system returns "Django"

#### Scenario: Get tag name in English
- **WHEN** tag has name_es="Django" and name_en="Django"
- **AND** user language is English
- **THEN** system returns "Django"

### Requirement: ProfileTag association
Users SHALL be able to associate tags with their profiles, marking each tag as either "must" (obligatory) or "nice" (desirable).

#### Scenario: Add must tag to profile
- **WHEN** user adds tag "Django" with tag_type="must" to their profile
- **THEN** system stores the association and profile appears in searches requiring Django

#### Scenario: Add nice tag to profile
- **WHEN** user adds tag "React" with tag_type="nice" to their profile
- **THEN** system stores the association and profile receives bonus score in searches including React

#### Scenario: Prevent duplicate tag association
- **WHEN** user tries to add tag "Django" with tag_type="must" but already has "Django" as "nice"
- **THEN** system updates the existing association to "must" instead of creating duplicate

### Requirement: Django Admin management
The tag dictionary SHALL be manageable through Django Admin interface with appropriate list displays, filters, and search fields.

#### Scenario: Admin views sectors
- **WHEN** admin navigates to SectorTag admin page
- **THEN** system displays list with name_es, name_en, slug columns and search by name

#### Scenario: Admin views roles
- **WHEN** admin navigates to SectorRol admin page
- **THEN** system displays list with sector, name_es, name_en, slug columns and filter by sector

#### Scenario: Admin views tags
- **WHEN** admin navigates to Tag admin page
- **THEN** system displays list with name_es, name_en, slug, category, especialidad columns and filter by category
