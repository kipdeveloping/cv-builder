document.addEventListener('DOMContentLoaded', function() {
    const cvContainer = document.getElementById('cv-container');
    const saveStatus = document.getElementById('save-status');
    let saveTimeout = null;
    let isSaving = false;

    let initialContent = {};
    const contentNode = document.getElementById('resume-content');
    if (contentNode) {
        try { initialContent = JSON.parse(contentNode.textContent); } catch (e) { initialContent = {}; }
    }

    const SECTION_CONFIG = {
        experience: {
            required: 'title',
            fields: [
                { field: 'title', cls: 'entry-title', placeholder: 'Título del puesto' },
                { field: 'company', cls: 'entry-subtitle', placeholder: 'Empresa' },
                { field: 'period', cls: 'entry-period', placeholder: '2020 - Presente' },
                { field: 'description', cls: 'entry-description', placeholder: 'Descripción...' }
            ]
        },
        education: {
            required: 'degree',
            fields: [
                { field: 'degree', cls: 'entry-title', placeholder: 'Título' },
                { field: 'school', cls: 'entry-subtitle', placeholder: 'Institución' },
                { field: 'year', cls: 'entry-period', placeholder: '2018' }
            ]
        },
        projects: {
            required: 'title',
            fields: [
                { field: 'title', cls: 'entry-title', placeholder: 'Nombre del proyecto' },
                { field: 'description', cls: 'entry-description', placeholder: 'Descripción del proyecto...' },
                { field: 'link', cls: 'entry-period', placeholder: 'https://...' }
            ]
        },
        languages: {
            required: 'language',
            fields: [
                { field: 'language', cls: 'entry-title', placeholder: 'Idioma' },
                { field: 'level', cls: 'entry-subtitle', placeholder: 'Nivel' }
            ]
        },
        certifications: {
            required: 'name',
            fields: [
                { field: 'name', cls: 'entry-title', placeholder: 'Nombre de la certificación' },
                { field: 'institution', cls: 'entry-subtitle', placeholder: 'Institución o plataforma' },
                { field: 'year', cls: 'entry-period', placeholder: 'Año' }
            ]
        },
        volunteering: {
            required: 'role',
            fields: [
                { field: 'role', cls: 'entry-title', placeholder: 'Rol / Cargo' },
                { field: 'organization', cls: 'entry-subtitle', placeholder: 'Organización' },
                { field: 'period', cls: 'entry-period', placeholder: '2020 - Presente' },
                { field: 'description', cls: 'entry-description', placeholder: 'Describe tu labor...' }
            ]
        },
        awards: {
            required: 'name',
            fields: [
                { field: 'name', cls: 'entry-title', placeholder: 'Premio o reconocimiento' },
                { field: 'issuer', cls: 'entry-subtitle', placeholder: 'Otorgado por' },
                { field: 'year', cls: 'entry-period', placeholder: 'Año' }
            ]
        },
        publications: {
            required: 'title',
            fields: [
                { field: 'title', cls: 'entry-title', placeholder: 'Título de la publicación' },
                { field: 'venue', cls: 'entry-subtitle', placeholder: 'Medio o revista' },
                { field: 'year', cls: 'entry-period', placeholder: 'Año' },
                { field: 'url', cls: 'entry-description', placeholder: 'https://...' }
            ]
        },
        references: {
            required: 'name',
            fields: [
                { field: 'name', cls: 'entry-title', placeholder: 'Nombre' },
                { field: 'position', cls: 'entry-subtitle', placeholder: 'Cargo' },
                { field: 'company', cls: 'entry-period', placeholder: 'Empresa' },
                { field: 'contact', cls: 'entry-description', placeholder: 'email o teléfono' }
            ]
        }
    };

    function getCSRFToken() {
        const cookie = document.cookie.split(';').find(c => c.trim().startsWith('csrftoken='));
        return cookie ? cookie.split('=')[1] : '';
    }

    function pl(key, fallback) {
        return typeof t === 'function' ? t(key) : fallback;
    }

    function collectFormData() {
        const data = {
            name: '',
            email: '',
            phone: '',
            city: '',
            occupation: '',
            bio: '',
            skills: [],
            interests: [],
            social_links: {}
        };
        const lists = {};
        Object.keys(SECTION_CONFIG).forEach(k => lists[k] = []);

        cvContainer.querySelectorAll('[contenteditable]').forEach(el => {
            const field = el.dataset.field;
            const section = el.dataset.section;
            const index = parseInt(el.dataset.index) || 0;
            const value = el.innerText.trim();

            if (field === 'skill' || field === 'interest') {
                if (value) data[field === 'skill' ? 'skills' : 'interests'][index] = value;
                return;
            }

            if (section && lists[section]) {
                if (!lists[section][index]) lists[section][index] = {};
                lists[section][index][field] = value;
                return;
            }

            if (data.hasOwnProperty(field)) {
                data[field] = value;
            }
        });

        Object.keys(SECTION_CONFIG).forEach(key => {
            const required = SECTION_CONFIG[key].required;
            data[key] = lists[key].filter(e => e && e[required]);
        });
        data.skills = data.skills.filter(s => s);
        data.interests = data.interests.filter(s => s);

        if (initialContent && initialContent.social_links && typeof initialContent.social_links === 'object') {
            data.social_links = initialContent.social_links;
        }

        return data;
    }

    async function saveResume() {
        if (isSaving) return;

        isSaving = true;
        saveStatus.textContent = pl('Guardando...', 'Guardando...');
        saveStatus.className = 'text-sm text-yellow-600';

        try {
            const data = collectFormData();
            const response = await fetch('/api/resume/save/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    resume_id: resumeId,
                    content: data
                })
            });

            const result = await response.json();

            if (result.status === 'ok') {
                saveStatus.textContent = pl('Guardado a las', 'Guardado a las') + ' ' + result.timestamp;
                saveStatus.className = 'text-sm text-green-600';
            } else {
                saveStatus.textContent = pl('Error al guardar', 'Error al guardar');
                saveStatus.className = 'text-sm text-red-600';
            }
        } catch (error) {
            console.error('Error saving:', error);
            saveStatus.textContent = pl('Error de conexión', 'Error de conexión');
            saveStatus.className = 'text-sm text-red-600';
        } finally {
            isSaving = false;
        }
    }

    function debounceSave() {
        if (saveTimeout) clearTimeout(saveTimeout);
        saveTimeout = setTimeout(saveResume, 2000);
    }

    function entryHTML(section, index) {
        const conf = SECTION_CONFIG[section];
        const fieldsHtml = conf.fields.map(f => {
            const ph = pl(f.placeholder, f.placeholder);
            return `<div class="${f.cls}" contenteditable="true" data-field="${f.field}">${ph}</div>`;
        }).join('');
        return `<div class="entry" data-section="${section}" data-index="${index}">${fieldsHtml}` +
            `<button type="button" class="entry-remove" title="${pl('Eliminar', 'Eliminar')}">×</button></div>`;
    }

    function bindEntry(entry) {
        entry.querySelectorAll('[contenteditable]').forEach(el => {
            el.addEventListener('input', debounceSave);
            el.addEventListener('blur', function() {
                if (saveTimeout) clearTimeout(saveTimeout);
                saveResume();
            });
        });

        const removeBtn = entry.querySelector('.entry-remove');
        if (removeBtn) {
            removeBtn.addEventListener('click', function() {
                entry.remove();
                reindexEntries(entry.parentElement);
            });
        }
    }

    function reindexEntries(list) {
        if (!list) return;
        Array.from(list.children).forEach((child, i) => {
            if (child.classList.contains('entry')) {
                child.dataset.index = i;
                child.querySelectorAll('[contenteditable]').forEach(el => {
                    el.dataset.index = i;
                });
            }
        });
        saveResume();
    }

    function bindTag(tag) {
        tag.addEventListener('input', debounceSave);
        tag.addEventListener('blur', function() {
            if (saveTimeout) clearTimeout(saveTimeout);
            saveResume();
        });
        tag.addEventListener('focus', function() {
            if (this.innerText.trim() === this.getAttribute('data-placeholder')) {
                this.innerText = '';
            }
        });
        const removeBtn = tag.querySelector('.tag-remove');
        if (removeBtn) {
            removeBtn.addEventListener('click', function() {
                tag.remove();
                reindexTags(tag.parentElement);
            });
        }
    }

    function reindexTags(list) {
        if (!list) return;
        Array.from(list.children).forEach((child, i) => {
            if (child.classList.contains('skill-tag')) {
                child.dataset.index = i;
            }
        });
        saveResume();
    }

    cvContainer.querySelectorAll('.entry').forEach(bindEntry);
    cvContainer.querySelectorAll('.skill-tag').forEach(bindTag);
    cvContainer.querySelectorAll('[contenteditable]').forEach(el => {
        el.addEventListener('input', debounceSave);
        el.addEventListener('blur', function() {
            if (saveTimeout) clearTimeout(saveTimeout);
            saveResume();
        });
    });

    cvContainer.querySelectorAll('.add-entry-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const section = this.dataset.section;
            if (!SECTION_CONFIG[section]) return;
            const list = document.getElementById(`${section}-list`);
            if (!list) return;
            list.insertAdjacentHTML('beforeend', entryHTML(section, list.children.length));
            const newEntry = list.lastElementChild;
            bindEntry(newEntry);
            const firstEditable = newEntry.querySelector('[contenteditable]');
            if (firstEditable) firstEditable.focus();
        });
    });

    function bindTagButton(btnId, field, fallbackText) {
        const btn = document.getElementById(btnId);
        if (!btn) return;
        btn.addEventListener('click', function() {
            const list = document.getElementById(field === 'skill' ? 'skills-list' : 'interests-list');
            if (!list) return;
            const tag = document.createElement('span');
            tag.className = 'skill-tag';
            tag.contentEditable = true;
            tag.dataset.field = field;
            tag.dataset.index = list.children.length;
            tag.innerHTML = `${pl(fallbackText, fallbackText)}<button type="button" class="tag-remove" title="${pl('Eliminar', 'Eliminar')}">×</button>`;
            list.appendChild(tag);
            bindTag(tag);
            const text = tag.firstChild;
            if (text) {
                const range = document.createRange();
                range.setStart(text, 0);
                range.collapse(true);
                const sel = window.getSelection();
                sel.removeAllRanges();
                sel.addRange(range);
            }
            tag.focus();
        });
    }

    bindTagButton('add-skill-btn', 'skill', 'Nueva habilidad');
    bindTagButton('add-interest-btn', 'interest', 'Nuevo interés');
});