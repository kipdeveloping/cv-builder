document.addEventListener('DOMContentLoaded', function() {
    const cvContainer = document.getElementById('cv-container');
    const saveStatus = document.getElementById('save-status');
    let saveTimeout = null;
    let isSaving = false;

    function getCSRFToken() {
        const cookie = document.cookie.split(';').find(c => c.trim().startsWith('csrftoken='));
        return cookie ? cookie.split('=')[1] : '';
    }

    function collectFormData() {
        const data = {
            name: '',
            email: '',
            phone: '',
            city: '',
            occupation: '',
            bio: '',
            experience: [],
            education: [],
            skills: []
        };

        const experienceEntries = [];
        const educationEntries = [];
        const skills = [];

        cvContainer.querySelectorAll('[contenteditable]').forEach(el => {
            const field = el.dataset.field;
            const section = el.dataset.section;
            const index = parseInt(el.dataset.index) || 0;
            const value = el.innerText.trim();

            if (field === 'skill') {
                if (value) skills[index] = value;
                return;
            }

            if (section === 'experience') {
                if (!experienceEntries[index]) experienceEntries[index] = {};
                experienceEntries[index][field] = value;
            } else if (section === 'education') {
                if (!educationEntries[index]) educationEntries[index] = {};
                educationEntries[index][field] = value;
            } else if (data.hasOwnProperty(field)) {
                data[field] = value;
            }
        });

        data.experience = experienceEntries.filter(e => e && e.title);
        data.education = educationEntries.filter(e => e && e.degree);
        data.skills = skills.filter(s => s);

        return data;
    }

    function sanitizeInput(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    async function saveResume() {
        if (isSaving) return;

        isSaving = true;
        saveStatus.textContent = 'Guardando...';
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
                saveStatus.textContent = `Guardado a las ${result.timestamp}`;
                saveStatus.className = 'text-sm text-green-600';
            } else {
                saveStatus.textContent = 'Error al guardar';
                saveStatus.className = 'text-sm text-red-600';
            }
        } catch (error) {
            console.error('Error saving:', error);
            saveStatus.textContent = 'Error de conexión';
            saveStatus.className = 'text-sm text-red-600';
        } finally {
            isSaving = false;
        }
    }

    function debounceSave() {
        if (saveTimeout) clearTimeout(saveTimeout);
        saveTimeout = setTimeout(saveResume, 2000);
    }

    cvContainer.querySelectorAll('[contenteditable]').forEach(el => {
        el.addEventListener('input', debounceSave);
        el.addEventListener('blur', function() {
            if (saveTimeout) clearTimeout(saveTimeout);
            saveResume();
        });

        el.addEventListener('focus', function() {
            if (this.innerText.trim() === this.getAttribute('data-placeholder')) {
                this.innerText = '';
            }
        });
    });

    document.querySelectorAll('.add-entry-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const section = this.dataset.section;
            const list = document.getElementById(`${section}-list`);
            const index = list.children.length;

            let html = '';
            if (section === 'experience') {
                html = `
                    <div class="entry" data-section="experience" data-index="${index}">
                        <div class="entry-title" contenteditable="true" data-field="title">Título del puesto</div>
                        <div class="entry-subtitle" contenteditable="true" data-field="company">Empresa</div>
                        <div class="entry-period" contenteditable="true" data-field="period">2020 - Presente</div>
                        <div class="entry-description" contenteditable="true" data-field="description">Descripción...</div>
                    </div>
                `;
            } else if (section === 'education') {
                html = `
                    <div class="entry" data-section="education" data-index="${index}">
                        <div class="entry-title" contenteditable="true" data-field="degree">Título</div>
                        <div class="entry-subtitle" contenteditable="true" data-field="school">Institución</div>
                        <div class="entry-period" contenteditable="true" data-field="year">2018</div>
                    </div>
                `;
            }

            list.insertAdjacentHTML('beforeend', html);

            const newEntry = list.lastElementChild;
            newEntry.querySelectorAll('[contenteditable]').forEach(el => {
                el.addEventListener('input', debounceSave);
                el.addEventListener('blur', function() {
                    if (saveTimeout) clearTimeout(saveTimeout);
                    saveResume();
                });
            });

            newEntry.querySelector('[contenteditable]').focus();
        });
    });

    const addSkillBtn = document.getElementById('add-skill-btn');
    if (addSkillBtn) {
        addSkillBtn.addEventListener('click', function() {
            const skillsList = document.getElementById('skills-list');
            const index = skillsList.children.length;

            const newSkill = document.createElement('span');
            newSkill.className = 'skill-tag';
            newSkill.contentEditable = true;
            newSkill.dataset.field = 'skill';
            newSkill.dataset.index = index;
            newSkill.textContent = 'Nueva habilidad';

            skillsList.appendChild(newSkill);

            newSkill.addEventListener('input', debounceSave);
            newSkill.addEventListener('blur', function() {
                if (saveTimeout) clearTimeout(saveTimeout);
                saveResume();
            });

            newSkill.addEventListener('focus', function() {
                this.textContent = '';
            });

            newSkill.focus();
        });
    }
});
