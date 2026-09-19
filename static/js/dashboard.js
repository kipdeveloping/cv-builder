document.addEventListener('DOMContentLoaded', function() {
    if (typeof experienceData === 'undefined') window.experienceData = [];
    if (typeof projectsData === 'undefined') window.projectsData = [];
    if (typeof socialLinksData === 'undefined') window.socialLinksData = {};

    function getCSRFToken() {
        const cookie = document.cookie.split(';').find(c => c.trim().startsWith('csrftoken='));
        return cookie ? cookie.split('=')[1] : '';
    }

    // Modal functions
    window.openModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (!modal) return;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
    };

    window.closeModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (!modal) return;
        modal.classList.add('hidden');
        modal.classList.remove('flex');
    };

    // Generic helper to update profile fields
    async function saveProfileData(payload) {
        try {
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify(payload)
            });
            return response.ok;
        } catch (error) {
            console.error('Error saving profile data:', error);
            return false;
        }
    }

    // Save headline
    window.saveHeadline = async function() {
        const headline = document.getElementById('headline-input').value.trim();
        try {
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({ headline: headline })
            });
            const result = await response.json();
            if (response.ok) {
                const defaultHeadline = (window.i18n && window.i18n.noHeadline) || 'Sin titular';
                document.getElementById('headline-display').innerHTML = (headline || defaultHeadline) + ' <button onclick="openModal(\'headline-modal\')" class="text-indigo-600 hover:text-indigo-700 dark:text-indigo-400 ml-1"><svg class="w-3.5 h-3.5 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg></button>';
                closeModal('headline-modal');
            } else {
                alert('Error al guardar: ' + (result.message || 'Error desconocido'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión: ' + error.message);
        }
    };

    // Save bio
    window.saveBio = async function() {
        const bio = document.getElementById('bio-input').value.trim();
        try {
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({ bio: bio })
            });
            const result = await response.json();
            if (response.ok) {
                const defaultBio = (window.i18n && window.i18n.noBio) || 'Sin biografía';
                document.getElementById('bio-display').textContent = bio || defaultBio;
                closeModal('bio-modal');
            } else {
                alert('Error al guardar: ' + (result.message || 'Error desconocido'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión: ' + error.message);
        }
    };

    // Save status
    window.saveStatus = async function() {
        const searchStatus = document.getElementById('search-status-input').value;
        const availability = document.getElementById('availability-input').value;
        const locationFlex = document.getElementById('location-flex-input').value;

        try {
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    search_status: searchStatus,
                    availability: availability,
                    location_flex: locationFlex
                })
            });
            if (response.ok) {
                location.reload();
            } else {
                const result = await response.json();
                alert('Error al guardar: ' + (result.message || 'Error desconocido'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión: ' + error.message);
        }
    };

    // Save work preferences
    window.saveWorkPrefs = async function() {
        const employmentType = [];
        document.querySelectorAll('#employment-type-input input[type="checkbox"]:checked').forEach(cb => {
            employmentType.push(cb.value);
        });
        const willingToRelocate = document.getElementById('relocate-input').value;
        const travelAvailability = document.getElementById('travel-input').value;

        try {
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    employment_type: employmentType,
                    willing_to_relocate: willingToRelocate,
                    travel_availability: travelAvailability
                })
            });
            if (response.ok) {
                location.reload();
            } else {
                const result = await response.json();
                alert('Error al guardar: ' + (result.message || 'Error desconocido'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión: ' + error.message);
        }
    };

    // ==========================================
    // Media / Image Upload for Items
    // ==========================================
    window.handleImageUpload = async function(fileInputId, urlInputId, previewContainerId, previewImgId) {
        const fileInput = document.getElementById(fileInputId);
        if (!fileInput || !fileInput.files || !fileInput.files[0]) return;

        const file = fileInput.files[0];
        if (file.size > 5 * 1024 * 1024) {
            alert('La imagen no puede superar los 5MB.');
            fileInput.value = '';
            return;
        }

        const formData = new FormData();
        formData.append('image', file);

        const statusEl = document.getElementById(fileInputId + '-status');
        if (statusEl) {
            statusEl.textContent = 'Subiendo imagen...';
            statusEl.classList.remove('hidden');
        }

        try {
            const response = await fetch('/accounts/upload-media/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCSRFToken()
                },
                body: formData
            });
            const data = await response.json();
            if (response.ok && data.url) {
                document.getElementById(urlInputId).value = data.url;
                const previewImg = document.getElementById(previewImgId);
                if (previewImg) previewImg.src = data.url;
                const previewContainer = document.getElementById(previewContainerId);
                if (previewContainer) previewContainer.classList.remove('hidden');
                const dropzone = document.getElementById(fileInputId + '-dropzone');
                if (dropzone) dropzone.classList.add('hidden');
                if (statusEl) statusEl.classList.add('hidden');
            } else {
                alert(data.message || 'Error al subir la imagen');
                if (statusEl) statusEl.classList.add('hidden');
            }
        } catch (e) {
            console.error(e);
            alert('Error de conexión al subir la imagen');
            if (statusEl) statusEl.classList.add('hidden');
        }
    };

    window.removeImage = function(urlInputId, previewContainerId, fileInputId) {
        document.getElementById(urlInputId).value = '';
        const previewContainer = document.getElementById(previewContainerId);
        if (previewContainer) previewContainer.classList.add('hidden');
        if (fileInputId) {
            const fileInput = document.getElementById(fileInputId);
            if (fileInput) fileInput.value = '';
            const dropzone = document.getElementById(fileInputId + '-dropzone');
            if (dropzone) dropzone.classList.remove('hidden');
        }
    };

    // ==========================================
    // Carousel Slide Controls
    // ==========================================
    let currentSlide = 0;
    window.prevSlide = function() {
        const container = document.getElementById('carousel-container');
        if (!container) return;
        const cards = container.querySelectorAll('.carousel-card');
        if (cards.length === 0) return;
        currentSlide = Math.max(0, currentSlide - 1);
        updateCarousel();
    };

    window.nextSlide = function() {
        const container = document.getElementById('carousel-container');
        if (!container) return;
        const cards = container.querySelectorAll('.carousel-card');
        if (cards.length === 0) return;
        currentSlide = Math.min(cards.length - 1, currentSlide + 1);
        updateCarousel();
    };

    function updateCarousel() {
        const container = document.getElementById('carousel-container');
        if (!container) return;
        const cards = container.querySelectorAll('.carousel-card');
        if (cards.length === 0) return;
        const card = cards[currentSlide];
        if (card) {
            card.scrollIntoView({ behavior: 'smooth', inline: 'start', block: 'nearest' });
        }
        const counter = document.getElementById('carousel-counter');
        if (counter) {
            counter.textContent = (currentSlide + 1) + ' / ' + cards.length;
        }
    }

    // ==========================================
    // Experience Management
    // ==========================================
    window.openAddExperienceModal = function() {
        document.getElementById('exp-modal-title').textContent = (window.i18n && window.i18n.addExperience) || 'Agregar experiencia';
        document.getElementById('exp-title-input').value = '';
        document.getElementById('exp-company-input').value = '';
        document.getElementById('exp-period-input').value = '';
        document.getElementById('exp-description-input').value = '';
        document.getElementById('exp-image-url').value = '';
        const previewImg = document.getElementById('exp-image-preview');
        if (previewImg) previewImg.src = '';
        const previewContainer = document.getElementById('exp-image-preview-container');
        if (previewContainer) previewContainer.classList.add('hidden');
        const dropzone = document.getElementById('exp-image-file-dropzone');
        if (dropzone) dropzone.classList.remove('hidden');
        const fileInput = document.getElementById('exp-image-file');
        if (fileInput) fileInput.value = '';
        document.getElementById('exp-edit-index').value = '-1';
        openModal('experience-modal');
    };

    window.editExperience = function(index) {
        const exp = experienceData[index];
        if (!exp) return;

        document.getElementById('exp-modal-title').textContent = (window.i18n && window.i18n.editExperience) || 'Editar experiencia';
        document.getElementById('exp-title-input').value = exp.title || '';
        document.getElementById('exp-company-input').value = exp.company || '';
        document.getElementById('exp-period-input').value = exp.period || '';
        document.getElementById('exp-description-input').value = exp.description || '';
        document.getElementById('exp-image-url').value = exp.image || '';

        const previewImg = document.getElementById('exp-image-preview');
        const previewContainer = document.getElementById('exp-image-preview-container');
        const dropzone = document.getElementById('exp-image-file-dropzone');

        if (exp.image) {
            if (previewImg) previewImg.src = exp.image;
            if (previewContainer) previewContainer.classList.remove('hidden');
            if (dropzone) dropzone.classList.add('hidden');
        } else {
            if (previewImg) previewImg.src = '';
            if (previewContainer) previewContainer.classList.add('hidden');
            if (dropzone) dropzone.classList.remove('hidden');
        }
        const fileInput = document.getElementById('exp-image-file');
        if (fileInput) fileInput.value = '';

        document.getElementById('exp-edit-index').value = index;
        openModal('experience-modal');
    };

    window.deleteExperience = async function(index) {
        const confirmMsg = (window.i18n && window.i18n.deleteExperienceConfirm) || '¿Deseas eliminar esta experiencia laboral?';
        if (!confirm(confirmMsg)) return;
        experienceData.splice(index, 1);
        const ok = await saveProfileData({ experience: experienceData });
        if (ok) {
            location.reload();
        } else {
            alert('Error al eliminar la experiencia.');
        }
    };

    window.saveExperience = async function() {
        const title = document.getElementById('exp-title-input').value.trim();
        const company = document.getElementById('exp-company-input').value.trim();
        const period = document.getElementById('exp-period-input').value.trim();
        const description = document.getElementById('exp-description-input').value.trim();
        const image = document.getElementById('exp-image-url').value.trim();
        const editIndex = parseInt(document.getElementById('exp-edit-index').value, 10);

        if (!title || !company) {
            alert('El cargo y la empresa son campos obligatorios.');
            return;
        }

        const exp = { title, company, period, description, image };

        if (editIndex >= 0) {
            experienceData[editIndex] = exp;
        } else {
            experienceData.push(exp);
        }

        const ok = await saveProfileData({ experience: experienceData });
        if (ok) {
            location.reload();
        } else {
            alert('Error al guardar la experiencia.');
        }
    };

    // ==========================================
    // Projects Management
    // ==========================================
    window.openAddProjectModal = function() {
        document.getElementById('proj-modal-title').textContent = (window.i18n && window.i18n.addProject) || 'Agregar proyecto';
        document.getElementById('proj-title-input').value = '';
        document.getElementById('proj-company-input').value = '';
        document.getElementById('proj-period-input').value = '';
        document.getElementById('proj-url-input').value = '';
        document.getElementById('proj-description-input').value = '';
        document.getElementById('proj-image-url').value = '';
        const previewImg = document.getElementById('proj-image-preview');
        if (previewImg) previewImg.src = '';
        const previewContainer = document.getElementById('proj-image-preview-container');
        if (previewContainer) previewContainer.classList.add('hidden');
        const dropzone = document.getElementById('proj-image-file-dropzone');
        if (dropzone) dropzone.classList.remove('hidden');
        const fileInput = document.getElementById('proj-image-file');
        if (fileInput) fileInput.value = '';
        document.getElementById('proj-edit-index').value = '-1';
        openModal('project-modal');
    };

    window.editProject = function(index) {
        const proj = projectsData[index];
        if (!proj) return;

        document.getElementById('proj-modal-title').textContent = (window.i18n && window.i18n.editProject) || 'Editar proyecto';
        document.getElementById('proj-title-input').value = proj.title || '';
        document.getElementById('proj-company-input').value = proj.company || '';
        document.getElementById('proj-period-input').value = proj.period || '';
        document.getElementById('proj-url-input').value = proj.url || '';
        document.getElementById('proj-description-input').value = proj.description || '';
        document.getElementById('proj-image-url').value = proj.image || '';

        const previewImg = document.getElementById('proj-image-preview');
        const previewContainer = document.getElementById('proj-image-preview-container');
        const dropzone = document.getElementById('proj-image-file-dropzone');

        if (proj.image) {
            if (previewImg) previewImg.src = proj.image;
            if (previewContainer) previewContainer.classList.remove('hidden');
            if (dropzone) dropzone.classList.add('hidden');
        } else {
            if (previewImg) previewImg.src = '';
            if (previewContainer) previewContainer.classList.add('hidden');
            if (dropzone) dropzone.classList.remove('hidden');
        }
        const fileInput = document.getElementById('proj-image-file');
        if (fileInput) fileInput.value = '';

        document.getElementById('proj-edit-index').value = index;
        openModal('project-modal');
    };

    window.deleteProject = async function(index) {
        const confirmMsg = (window.i18n && window.i18n.deleteProjectConfirm) || '¿Deseas eliminar este proyecto?';
        if (!confirm(confirmMsg)) return;
        projectsData.splice(index, 1);
        const ok = await saveProfileData({ projects: projectsData });
        if (ok) {
            location.reload();
        } else {
            alert('Error al eliminar el proyecto.');
        }
    };

    window.saveProject = async function() {
        const title = document.getElementById('proj-title-input').value.trim();
        const company = document.getElementById('proj-company-input').value.trim();
        const period = document.getElementById('proj-period-input').value.trim();
        const url = document.getElementById('proj-url-input').value.trim();
        const description = document.getElementById('proj-description-input').value.trim();
        const image = document.getElementById('proj-image-url').value.trim();
        const editIndex = parseInt(document.getElementById('proj-edit-index').value, 10);

        if (!title) {
            alert('El título del proyecto es obligatorio.');
            return;
        }

        const proj = { title, company, period, url, description, image };

        if (editIndex >= 0) {
            projectsData[editIndex] = proj;
        } else {
            projectsData.push(proj);
        }

        const ok = await saveProfileData({ projects: projectsData });
        if (ok) {
            location.reload();
        } else {
            alert('Error al guardar el proyecto.');
        }
    };

    // ==========================================
    // Social Links
    // ==========================================
    window.saveSocialLinks = async function() {
        const socialLinks = {
            linkedin: document.getElementById('social-linkedin').value.trim(),
            github: document.getElementById('social-github').value.trim(),
            twitter: document.getElementById('social-twitter').value.trim(),
            portfolio: document.getElementById('social-portfolio').value.trim()
        };

        try {
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    social_links: socialLinks
                })
            });

            if (response.ok) {
                location.reload();
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    // ==========================================
    // Profile Visibility Toggle
    // ==========================================
    window.toggleVisibility = async function() {
        const button = document.getElementById('visibility-toggle');
        const dot = document.getElementById('visibility-dot');
        const warning = document.getElementById('visibility-warning');

        const isChecked = button.getAttribute('aria-checked') === 'true';
        const newState = !isChecked;

        button.setAttribute('aria-checked', newState);
        button.classList.toggle('bg-indigo-600', newState);
        button.classList.toggle('bg-gray-300', !newState);
        button.classList.toggle('dark:bg-gray-600', !newState);
        dot.classList.toggle('translate-x-5', newState);
        dot.classList.toggle('translate-x-0', !newState);
        warning.classList.add('hidden');

        try {
            const response = await fetch(urls.toggleVisibility, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                }
            });
            const result = await response.json();

            if (!response.ok || result.status !== 'ok') {
                button.setAttribute('aria-checked', isChecked);
                button.classList.toggle('bg-indigo-600', isChecked);
                button.classList.toggle('bg-gray-300', !isChecked);
                button.classList.toggle('dark:bg-gray-600', !isChecked);
                dot.classList.toggle('translate-x-5', isChecked);
                dot.classList.toggle('translate-x-0', !isChecked);
                warning.textContent = result.message || 'Error al cambiar visibilidad.';
                warning.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error:', error);
            button.setAttribute('aria-checked', isChecked);
            button.classList.toggle('bg-indigo-600', isChecked);
            button.classList.toggle('bg-gray-300', !isChecked);
            button.classList.toggle('dark:bg-gray-600', !isChecked);
            dot.classList.toggle('translate-x-5', isChecked);
            dot.classList.toggle('translate-x-0', !isChecked);
        }
    };

    // ==========================================
    // Skills & Tags Modal
    // ==========================================
    let skillsHierarchy = [];
    let allTags = [];
    let selectedTags = [];
    let selectedLanguages = [];

    window.loadHierarchy = async function() {
        try {
            const response = await fetch(urls.tagHierarchy);
            if (response.ok) {
                const data = await response.json();
                skillsHierarchy = data.hierarchy || [];
            }
        } catch (error) {
            console.error('Error loading hierarchy:', error);
        }
    };

    window.populateSkillsSectorDropdown = function(preselectedSlug) {
        const sectorSelect = document.getElementById('skills-sector-select');
        if (!sectorSelect) return;
        sectorSelect.innerHTML = '<option value="">Seleccionar sector...</option>';
        skillsHierarchy.forEach(sector => {
            const option = document.createElement('option');
            option.value = sector.slug;
            option.textContent = sector.name;
            if (preselectedSlug && sector.slug === preselectedSlug) option.selected = true;
            sectorSelect.appendChild(option);
        });
    };

    window.populateSkillsRolDropdown = function(sectorSlug, preselectedSlug) {
        const rolSelect = document.getElementById('skills-rol-select');
        if (!rolSelect) return;
        rolSelect.innerHTML = '<option value="">Seleccionar rol...</option>';
        const sector = skillsHierarchy.find(s => s.slug === sectorSlug);
        if (sector) {
            sector.roles.forEach(rol => {
                const option = document.createElement('option');
                option.value = rol.slug;
                option.textContent = rol.name;
                if (preselectedSlug && rol.slug === preselectedSlug) option.selected = true;
                rolSelect.appendChild(option);
            });
        }
    };

    window.populateSkillsEspecialidadDropdown = function(sectorSlug, rolSlug, preselectedSlug) {
        const espSelect = document.getElementById('skills-especialidad-select');
        if (!espSelect) return;
        espSelect.innerHTML = '<option value="">Seleccionar especialidad...</option>';
        const sector = skillsHierarchy.find(s => s.slug === sectorSlug);
        if (sector) {
            const rol = sector.roles.find(r => r.slug === rolSlug);
            if (rol) {
                rol.especialidades.forEach(esp => {
                    const option = document.createElement('option');
                    option.value = esp.slug;
                    option.textContent = esp.name;
                    if (preselectedSlug && esp.slug === preselectedSlug) option.selected = true;
                    espSelect.appendChild(option);
                });
            }
        }
    };

    window.openSkillsModal = async function() {
        openModal('skills-modal');
        renderSelectedTags();
        renderSelectedLanguages();

        if (skillsHierarchy.length === 0) {
            await loadHierarchy();
        }

        try {
            const response = await fetch(urls.getProfileTags);
            if (response.ok) {
                const data = await response.json();
                selectedTags = data.tags || [];
                selectedLanguages = data.languages || [];

                populateSkillsSectorDropdown(data.sector || null);
                if (data.sector) {
                    populateSkillsRolDropdown(data.sector, data.rol || null);
                    if (data.rol) {
                        populateSkillsEspecialidadDropdown(data.sector, data.rol, data.especialidad || null);
                    }
                }
                document.getElementById('skills-seniority-select').value = data.seniority || '';

                renderSelectedTags();
                renderSelectedLanguages();
            }
        } catch (error) {
            console.error('Error loading profile tags:', error);
        }
    };

    window.loadAllTags = async function() {
        try {
            const response = await fetch(urls.allTags);
            if (response.ok) {
                const data = await response.json();
                allTags = data.tags || data || [];
            }
        } catch (error) {
            console.error('Error loading tags:', error);
        }
    };

    window.searchTags = async function(query) {
        const suggestions = document.getElementById('tag-suggestions');
        if (!suggestions) return;
        const q = (query || '').trim();
        if (q.length < 1) {
            suggestions.classList.add('hidden');
            suggestions.innerHTML = '';
            return;
        }

        let matches = allTags.filter(tag => 
            (tag.name && tag.name.toLowerCase().includes(q.toLowerCase())) ||
            (tag.slug && tag.slug.toLowerCase().includes(q.toLowerCase()))
        ).slice(0, 10);

        // Fetch from API for broader search
        if (q.length >= 2 && matches.length < 5) {
            try {
                const response = await fetch(urls.allTags + '?search=' + encodeURIComponent(q));
                if (response.ok) {
                    const data = await response.json();
                    const apiTags = data.tags || [];
                    apiTags.forEach(at => {
                        if (!matches.some(m => m.slug === at.slug)) {
                            matches.push(at);
                        }
                    });
                }
            } catch (e) {
                console.error('Error fetching tags search:', e);
            }
        }

        let html = '';
        matches.forEach(tag => {
            const safeName = (tag.name || tag.slug).replace(/'/g, "\\'");
            html += `<div class="px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 cursor-pointer text-sm font-medium text-gray-800 dark:text-gray-200" onclick="addTag('${tag.slug}', '${safeName}')">${tag.name || tag.slug}</div>`;
        });

        const exactMatch = matches.some(m => (m.name && m.name.toLowerCase() === q.toLowerCase()) || (m.slug && m.slug.toLowerCase() === q.toLowerCase()));
        if (!exactMatch && q.length >= 2) {
            const safeQ = q.replace(/'/g, "\\'");
            const slugQ = q.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') || ('tag-' + Date.now());
            const addPrefix = (window.i18n && window.i18n.addTagPrefix) || 'Añadir';
            const newTagLbl = (window.i18n && window.i18n.newTagLabel) || 'Nuevo tag';
            html += `<div class="px-4 py-2.5 hover:bg-indigo-50 dark:hover:bg-indigo-900/40 cursor-pointer text-sm font-bold text-indigo-600 dark:text-indigo-400 border-t border-gray-100 dark:border-gray-600 flex items-center justify-between" onclick="addTag('${slugQ}', '${safeQ}')">
                <span>+ ${addPrefix} "${safeQ}"</span>
                <span class="text-xs font-normal opacity-75">${newTagLbl}</span>
            </div>`;
        }

        if (html) {
            suggestions.innerHTML = html;
            suggestions.classList.remove('hidden');
        } else {
            suggestions.classList.add('hidden');
        }
    };

    window.addTag = function(slug, name) {
        if (!slug) return;
        const tagName = name || slug;
        if (!selectedTags.find(t => t.slug === slug)) {
            selectedTags.push({ slug: slug, name: tagName });
            renderSelectedTags();
        }
        const input = document.getElementById('tag-search-input');
        if (input) input.value = '';
        const suggestions = document.getElementById('tag-suggestions');
        if (suggestions) {
            suggestions.innerHTML = '';
            suggestions.classList.add('hidden');
        }
    };

    window.addCurrentTagInput = function() {
        const input = document.getElementById('tag-search-input');
        if (!input) return;
        const val = input.value.trim();
        if (!val) return;
        const slug = val.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') || ('tag-' + Date.now());
        window.addTag(slug, val);
    };

    window.removeTag = function(slug) {
        selectedTags = selectedTags.filter(t => t.slug !== slug);
        renderSelectedTags();
    };

    function renderSelectedTags() {
        const container = document.getElementById('selected-tags');
        if (!container) return;
        if (selectedTags.length === 0) {
            const noTagsLbl = (window.i18n && window.i18n.noTagsSelected) || 'No hay tags seleccionados';
            container.innerHTML = `<span class="text-xs text-gray-400 dark:text-gray-500 italic py-1">${noTagsLbl}</span>`;
            return;
        }
        container.innerHTML = selectedTags.map(tag => 
            '<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-indigo-100 dark:bg-indigo-900/60 text-indigo-800 dark:text-indigo-200 shadow-2xs">' + 
            (tag.name || tag.slug) + 
            '<button type="button" onclick="removeTag(\'' + tag.slug + '\')" class="ml-1.5 text-indigo-600 dark:text-indigo-400 hover:text-indigo-900 font-bold">&times;</button></span>'
        ).join('');
    }

    window.addLanguage = function() {
        const select = document.getElementById('language-select');
        if (!select) return;
        const code = select.value;
        if (!code) return;
        const name = select.options[select.selectedIndex].text;
        if (!selectedLanguages.find(l => l.code === code)) {
            selectedLanguages.push({ code: code, name: name });
            renderSelectedLanguages();
        }
        select.value = '';
    };

    window.removeLanguage = function(code) {
        selectedLanguages = selectedLanguages.filter(l => l.code !== code);
        renderSelectedLanguages();
    };

    function renderSelectedLanguages() {
        const container = document.getElementById('selected-languages');
        if (!container) return;
        if (selectedLanguages.length === 0) {
            const noLangsLbl = (window.i18n && window.i18n.noLanguagesSelected) || 'No hay idiomas seleccionados';
            container.innerHTML = `<span class="text-xs text-gray-400 dark:text-gray-500 italic py-1">${noLangsLbl}</span>`;
            return;
        }
        container.innerHTML = selectedLanguages.map(lang => 
            '<span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-emerald-100 dark:bg-emerald-900/60 text-emerald-800 dark:text-emerald-200 shadow-2xs">' + 
            lang.name + 
            '<button type="button" onclick="removeLanguage(\'' + lang.code + '\')" class="ml-1.5 text-emerald-600 dark:text-emerald-400 hover:text-emerald-900 font-bold">&times;</button></span>'
        ).join('');
    }

    window.saveSkills = async function() {
        // Auto-add any pending tag typed in the input
        const tagInput = document.getElementById('tag-search-input');
        if (tagInput && tagInput.value.trim()) {
            window.addCurrentTagInput();
        }

        // Auto-add any pending language selected in the dropdown
        const langSelect = document.getElementById('language-select');
        if (langSelect && langSelect.value) {
            window.addLanguage();
        }

        const sector = document.getElementById('skills-sector-select').value;
        const rol = document.getElementById('skills-rol-select').value;
        const especialidad = document.getElementById('skills-especialidad-select').value;
        const seniority = document.getElementById('skills-seniority-select').value;

        try {
            const response = await fetch(urls.saveProfileTags, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    sector: sector,
                    rol: rol,
                    especialidad: especialidad,
                    seniority: seniority,
                    tags: selectedTags.map(t => ({ slug: t.slug, name: t.name || t.slug, tag_type: 'nice' })),
                    languages: selectedLanguages.map(l => ({ code: l.code, level: 'intermediate' }))
                })
            });

            if (response.ok) {
                location.reload();
            } else {
                const result = await response.json();
                alert('Error al guardar: ' + (result.message || 'Error desconocido'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión: ' + error.message);
        }
    };

    // Event Listeners for Skills Modal Dropdowns & Inputs
    const skillsSectorEl = document.getElementById('skills-sector-select');
    if (skillsSectorEl) {
        skillsSectorEl.addEventListener('change', function() {
            const sectorSlug = this.value;
            populateSkillsRolDropdown(sectorSlug);
            const espEl = document.getElementById('skills-especialidad-select');
            if (espEl) espEl.innerHTML = '<option value="">Seleccionar especialidad...</option>';
        });
    }

    const skillsRolEl = document.getElementById('skills-rol-select');
    if (skillsRolEl) {
        skillsRolEl.addEventListener('change', function() {
            const sectorSlug = document.getElementById('skills-sector-select').value;
            const rolSlug = this.value;
            populateSkillsEspecialidadDropdown(sectorSlug, rolSlug);
        });
    }

    const langSelectEl = document.getElementById('language-select');
    if (langSelectEl) {
        langSelectEl.addEventListener('change', function() {
            if (this.value) {
                window.addLanguage();
            }
        });
    }

    const tagInputEl = document.getElementById('tag-search-input');
    if (tagInputEl) {
        tagInputEl.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                window.addCurrentTagInput();
            }
        });
        tagInputEl.addEventListener('input', function() {
            window.searchTags(this.value);
        });
    }

    // Close tag suggestions on outside click
    document.addEventListener('click', function(e) {
        const input = document.getElementById('tag-search-input');
        const suggestions = document.getElementById('tag-suggestions');
        if (suggestions && input && !input.contains(e.target) && !suggestions.contains(e.target)) {
            suggestions.classList.add('hidden');
        }
    });

    // Initialize
    loadHierarchy();
    loadAllTags();
});