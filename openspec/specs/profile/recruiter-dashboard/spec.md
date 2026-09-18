# profile/recruiter-dashboard Specification

## Purpose

Provides a dedicated dashboard interface for recruiters to manage their company profile, view and manage job vacancies, and control public visibility.

## Requirements

### Requirement: Recruiter dashboard layout with sidebar and main area
The recruiter dashboard SHALL use a two-column layout with a sidebar (4 columns) and main area (8 columns) on large screens.

#### Scenario: Sidebar displays company identity
- **WHEN** a recruiter views their dashboard
- **THEN** the sidebar displays company_logo (or placeholder), company_name, and company_sector

#### Scenario: Sidebar displays company description
- **WHEN** a recruiter views their dashboard
- **THEN** the sidebar displays a "Sobre Nosotros" section with company_description
- **AND** an edit button is available to modify the description

#### Scenario: Sidebar displays company data card
- **WHEN** a recruiter views their dashboard
- **THEN** the sidebar displays a "Ficha de Datos" section showing ubicacion, tipo_reclutador, sitio_web, and modalidad

### Requirement: Vacancies section in main area
The main area SHALL display a "Mis Ofertas / Vacantes" section with a "+ Crear Vacante" button and a list of active vacancies.

#### Scenario: Vacancies list displayed
- **WHEN** a recruiter views their dashboard
- **THEN** the main area shows all vacancies linked to their profile
- **AND** each vacancy card shows title, modality, employment_type, and applications_count

#### Scenario: Create vacancy button
- **WHEN** a recruiter views their dashboard
- **THEN** a "+ Crear Vacante" button is visible
- **AND** clicking it navigates to the create vacancy form page

### Requirement: Social links section
The dashboard SHALL display a "Redes y Enlaces" section showing LinkedIn, Twitter, and website links from the recruiter's social_links.

#### Scenario: Social links displayed
- **WHEN** a recruiter has configured social links
- **THEN** the dashboard displays links for LinkedIn, Twitter, and website
- **AND** each link opens in a new tab

#### Scenario: Edit social links
- **WHEN** a recruiter clicks edit on social links
- **THEN** a modal opens with fields for LinkedIn, Twitter, and website URLs

### Requirement: Public profile toggle
The dashboard SHALL include a toggle to control whether the company profile is visible in the public directory.

#### Scenario: Toggle visibility on
- **WHEN** a recruiter enables the public profile toggle
- **THEN** the company profile becomes visible in the directory
- **AND** the toggle state is saved

#### Scenario: Toggle visibility off
- **WHEN** a recruiter disables the public profile toggle
- **THEN** the company profile is hidden from the directory
- **AND** the toggle state is saved
