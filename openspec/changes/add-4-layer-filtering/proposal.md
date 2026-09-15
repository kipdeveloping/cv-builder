## Why

The current talent board only supports filtering by sector using a simple text search (`sector_name__icontains`). This limits recruiters' ability to find specific talent. The project needs a hierarchical, faceted filtering system that allows multi-level search across sectors, roles, specialties, and technical skills, with weighted scoring to rank candidates by relevance.

## What Changes

- **New hierarchical tag dictionary**: 4-layer structure (Sector > Role > Specialty > Tags) with master dictionary managed via Django Admin
- **Profile tagging**: Users can select tags from the dictionary to associate with their profiles, marking them as "obligatory" (MUST) or "desirable" (NICE TO HAVE)
- **Faceted search API**: Independent filters that can be combined freely (no cascading required), with MUST/HAVE exclusion logic and NICE TO HAVE weighted scoring (0-100%)
- **Board UI redesign**: Replace simple sector chips with collapsible dropdown filters for each layer, plus tag selectors with logical operators
- **Dashboard integration**: New "Mis Habilidades" section in user profile for tag selection
- **Global attribute filters**: Seniority and languages added to UserProfile for cross-sector filtering

## Capabilities

### New Capabilities

- `tag-hierarchy`: Hierarchical tag dictionary system with 4 layers (Sector, Role, Specialty, Tags) and ProfileTag association with MUST/NICE types
- `faceted-search`: API and UI for multi-filter search with weighted scoring (MUST exclusion + NICE ranking 0-100%)
- `profile-tagging`: Dashboard UI for users to select tags from the dictionary and associate them with their profiles

### Modified Capabilities

- `wall-board`: Existing board filtering logic will be replaced with faceted search; sector chips will be replaced with hierarchical dropdowns

## Impact

- **Models**: New models (SectorRol, RolEspecialidad, Tag, ProfileTag) and modified UserProfile (add FK relations, seniority, languages)
- **API**: New endpoints for tag hierarchy and faceted search; existing `/api/wall/profiles/` will be significantly modified
- **Frontend**: Major changes to `wall.html` and `wall.js` (filter panel), new section in `dashboard.html` and `dashboard.js`
- **Database**: Migration required for new models and data population from fixture
- **Admin**: New model registrations for tag dictionary management
- **Existing data**: Fixture `sectors.json` needs model path fix (resumes → accounts) and content update
