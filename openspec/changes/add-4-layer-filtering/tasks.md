## 1. Model Setup

- [x] 1.1 Fix fixture app label (resumes → accounts) and verify SectorTag can be loaded
- [x] 1.2 Create SectorRol model with foreign key to SectorTag and verify migration
- [x] 1.3 Create RolEspecialidad model with foreign key to SectorRol and verify migration
- [x] 1.4 Create Tag model with foreign key to RolEspecialidad (nullable) and verify migration
- [x] 1.5 Create ProfileTag model with profile FK, tag FK, and tag_type field and verify migration
- [x] 1.6 Update UserProfile model with sector FK, rol FK, especialidad FK, seniority, languages fields and verify migration

## 2. Admin Setup

- [x] 2.1 Register SectorRol in Django admin with sector filter and verify display
- [x] 2.2 Register RolEspecialidad in Django admin with sector_rol filter and verify display
- [x] 2.3 Register Tag in Django admin with category filter and especialidad filter and verify display
- [x] 2.4 Register ProfileTag in Django admin with profile and tag_type filters and verify display
- [x] 2.5 Update UserProfile admin to show new fields and verify display

## 3. Data Migration

- [x] 3.1 Create migration script to load initial tag dictionary from fixture and verify data
- [x] 3.2 Create migration script to migrate existing sector_name to sector FK on UserProfile and verify data
- [x] 3.3 Verify all existing profiles have valid sector references after migration

## 4. API - Tag Hierarchy

- [x] 4.1 Create GET /api/tags/hierarchy/ endpoint returning nested JSON structure and verify response
- [x] 4.2 Add optional sector parameter to filter hierarchy and verify response

## 5. API - Faceted Search

- [x] 5.1 Update wall_api_view to accept sector, rol, especialidad parameters and verify filtering
- [x] 5.2 Add tags_must parameter with exclusion logic and verify profiles missing tags are excluded
- [x] 5.3 Add tags_nice parameter with scoring logic and verify score calculation
- [x] 5.4 Add seniority parameter and verify filtering
- [x] 5.5 Add languages parameter and verify filtering
- [x] 5.6 Implement weighted scoring calculation (Sector=30, Role=25, Specialty=20, MustTag=15, NiceTag=10) and verify scores
- [x] 5.7 Add score field to API response and verify JSON output
- [x] 5.8 Sort results by score descending and verify ordering

## 6. API - Profile Tags

- [x] 6.1 Create POST /api/profile/tags/ endpoint to save profile tags and verify storage
- [x] 6.2 Create GET /api/profile/tags/ endpoint to retrieve profile tags and verify response
- [x] 6.3 Handle tag_type updates (must ↔ nice) and verify no duplicates

## 7. Frontend - Board Filters

- [x] 7.1 Update wall.html with new filter panel layout (3 dropdowns + collapsible sections) and verify display
- [x] 7.2 Implement Sector dropdown with API fetch and verify options load
- [x] 7.3 Implement Role dropdown that updates based on Sector selection and verify cascading
- [x] 7.4 Implement Specialty dropdown that updates based on Role selection and verify cascading
- [x] 7.5 Implement collapsible tag selector with search input and verify tag suggestions
- [x] 7.6 Implement MUST/NICE tag selection with visual chips and verify add/remove
- [x] 7.7 Implement collapsible advanced filters (Seniority, Languages) and verify display
- [x] 7.8 Implement real-time search with debounced API calls and verify results update
- [x] 7.9 Display score percentage badge on profile cards and verify styling

## 8. Frontend - Profile Tagging

- [x] 8.1 Add "Mis Habilidades" card to dashboard between Bio and Work Preferences and verify placement
- [x] 8.2 Display current sector, role, specialty, tags in the card and verify data loads
- [x] 8.3 Create skills modal with hierarchical selectors matching dashboard design and verify modal opens
- [x] 8.4 Implement Sector dropdown in modal with API fetch and verify options load
- [x] 8.5 Implement Role dropdown that filters by selected Sector and verify cascading
- [x] 8.6 Implement Specialty dropdown that filters by selected Role and verify cascading
- [x] 8.7 Implement Seniority dropdown and verify selection saves
- [x] 8.8 Implement Language selector with add/remove functionality and verify storage
- [x] 8.9 Implement tag search input with autocomplete and verify suggestions appear
- [x] 8.10 Implement MUST/NICE tag assignment buttons and verify chips display
- [x] 8.11 Implement save button with API call and verify data persists
- [x] 8.12 Verify saved tags appear in board search results

## 9. Integration Testing

- [x] 9.1 Verify board filters return correct results with multiple criteria and verify accuracy
- [x] 9.2 Verify MUST tag exclusion works correctly and verify missing tags exclude profiles
- [x] 9.3 Verify NICE tag scoring works correctly and verify score calculation matches spec
- [x] 9.4 Verify profile tagging saves and retrieves correctly and verify data consistency
- [x] 9.5 Verify dashboard displays updated tags after save and verify UI reflects changes
