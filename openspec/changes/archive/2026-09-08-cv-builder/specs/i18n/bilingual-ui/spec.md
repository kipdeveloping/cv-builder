## Purpose

Provides bilingual UI support using Django i18n with Spanish and English translations, including a language toggle and bilingual sector tags.

## ADDED Requirements

### Requirement: Django i18n integration
The system SHALL use Django's internationalization framework to translate all UI strings between Spanish and English.

#### Scenario: Default language
- **WHEN** user first访问 the application
- **THEN** system displays UI in Spanish (default language)

#### Scenario: Language toggle available
- **WHEN** user views any page
- **THEN** system displays a language toggle button in the navbar showing [ES | EN]

### Requirement: Language switching via URL prefix
The system SHALL support language switching using URL prefixes: /es/... for Spanish and /en/... for English.

#### Scenario: Switch to English
- **WHEN** user clicks EN in the language toggle
- **THEN** system redirects to the English version of the current page with /en/ prefix

#### Scenario: Switch to Spanish
- **WHEN** user clicks ES in the language toggle
- **THEN** system redirects to the Spanish version of the current page with /es/ prefix

### Requirement: Bilingual sector tags
The system SHALL store sector tags with both Spanish and English names, displaying the appropriate version based on current language.

#### Scenario: Tag displayed in Spanish
- **WHEN** UI language is Spanish
- **THEN** sector tags display their name_es value

#### Scenario: Tag displayed in English
- **WHEN** UI language is English
- **THEN** sector tags display their name_en value

### Requirement: Translation files for UI strings
The system SHALL maintain .po translation files in locale/es/LC_MESSAGES/ and locale/en/LC_MESSAGES/ for all user-facing strings.

#### Scenario: Translations compiled
- **WHEN** translation files are updated
- **THEN** system compiles .po files to .mo files for use by Django

### Requirement: Template labels translate
The system SHALL translate CV section labels (Experiencia/Experience, Educacion/Education, etc.) based on current language, while user content remains in the language they wrote.

#### Scenario: Section labels in English
- **WHEN** UI language is English
- **THEN** CV section headers display "Experience", "Education", "Skills" instead of Spanish equivalents

#### Scenario: User content unchanged
- **WHEN** user wrote content in Spanish
- **THEN** switching to English UI does not translate the user's content

### Requirement: JavaScript i18n for dynamic content
The system SHALL provide client-side translation support for dynamically generated UI elements via a JavaScript i18n module.

#### Scenario: Dynamic strings translated
- **WHEN** JavaScript generates new UI text (e.g., "Saved at 14:32")
- **THEN** system uses i18n.js to translate the string based on current language
