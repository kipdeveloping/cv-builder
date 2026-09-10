## Why

There is no existing platform in this project. This is a greenfield build of an interactive CV/Resume builder with a public talent wall. The platform allows users to create, customize, and publish professional resumes using visual templates, then discover talent through a filterable public board. This serves as a full-stack learning project combining Django, Tailwind CSS v4, and vanilla JavaScript.

## What Changes

- **New Django project** with 3 apps: accounts, resumes, wall
- **User authentication** with email+password, robust password validation, and profile management
- **UserProfile model** with mandatory photo upload capability from dashboard
- **Resume system** with JSON-based content storage, 3 visual templates (Classic, Modern, Creative), and contenteditable-based editor
- **Auto-save functionality** using AJAX/fetch with 2-second debounce
- **Publishing workflow** with sector tag selection modal and validation (photo required, unique sector per user)
- **Public talent wall** with grid layout, real-time AJAX filtering by sector, and card display showing photo + name + bio
- **Bilingual UI** using Django i18n (Spanish/English toggle), with bilingual sector tags
- **Tailwind CSS v4** build system with npm for styling the UI
- **Custom CSS** for CV template visual differentiation
- **Landing page** for product presentation and user acquisition
- **Dashboard** for CV management and profile photo upload

## Capabilities

### New Capabilities

- ccounts/user-auth: User registration, login, logout with email+password authentication and profile management
- ccounts/user-profile: UserProfile with photo upload, bio field, and dashboard management
- esumes/resume-editor: Visual CV editor with contenteditable, auto-save, template selection, and JSON content storage
- esumes/resume-publishing: Publishing workflow with sector tag selection, validation, and status management
- esumes/cv-templates: Three visual CV templates (Classic, Modern, Creative) with distinct styling and photo integration
- wall/talent-wall: Public talent wall with grid display, AJAX sector filtering, and CV card rendering
- i18n/bilingual-ui: Django i18n integration with ES/EN toggle and bilingual sector tags

### Modified Capabilities

<!-- None - this is a greenfield project -->

## Impact

- **New files**: Complete Django project structure with apps/, templates/, static/, media/, locale/
- **Dependencies**: Django 4.2, Pillow, django-crispy-forms, crispy-bootstrap5, Tailwind CSS v4 (npm)
- **Database**: SQLite with 5 new models (UserProfile, Resume, Template, SectorTag, ResumeTag)
- **Frontend**: Tailwind CSS v4 compiled via npm, vanilla JavaScript for editor/wall/i18n
- **Static assets**: CSS templates, JS modules, images, compiled Tailwind output
- **Media storage**: User photo uploads in media/photos/
- **Translations**: Locale files for Spanish and English UI strings
