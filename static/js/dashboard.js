document.addEventListener('DOMContentLoaded', function() {
    let currentSlide = 0;
    const carousel = document.getElementById('carousel-container');
    const cards = carousel ? carousel.querySelectorAll('.carousel-card') : [];
    const counter = document.getElementById('carousel-counter');
    
    if (typeof experienceData === 'undefined') window.experienceData = [];
    if (typeof projectsData === 'undefined') window.projectsData = [];
    if (typeof socialLinksData === 'undefined') window.socialLinksData = {};
    
    function getCSRFToken() {
        const cookie = document.cookie.split(';').find(c => c.trim().startsWith('csrftoken='));
        return cookie ? cookie.split('=')[1] : '';
    }

    // Modal functions
    window.openModal = function(modalId) {
        document.getElementById(modalId).classList.remove('hidden');
        document.getElementById(modalId).classList.add('flex');
    };

    window.closeModal = function(modalId) {
        document.getElementById(modalId).classList.add('hidden');
        document.getElementById(modalId).classList.remove('flex');
    };

    // Save headline
    window.saveHeadline = async function() {
        const headline = document.getElementById('headline-input').value;
        
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
                document.getElementById('headline-display').innerHTML = headline + ' <button onclick="openModal(\'headline-modal\')" class="text-indigo-600 hover:text-indigo-700 ml-1"><svg class="w-3 h-3 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg></button>';
                closeModal('headline-modal');
            } else {
                alert('Error al guardar: ' + (result.message || 'Error desconocido'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexion: ' + error.message);
        }
    };

    // Save bio
    window.saveBio = async function() {
        const bio = document.getElementById('bio-input').value;
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
                document.getElementById('bio-display').textContent = bio || 'Sin biografia';
                closeModal('bio-modal');
            } else {
                alert('Error al guardar: ' + (result.message || 'Error desconocido'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexion: ' + error.message);
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
            
            const result = await response.json();
            
            if (response.ok) {
                location.reload();
            } else {
                alert('Error al guardar: ' + (result.message || 'Error desconocido'));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexion: ' + error.message);
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
            alert('Error de conexion: ' + error.message);
        }
    };

    // Experience/Projects carousel
    window.nextSlide = function() {
        if (currentSlide < cards.length - 1) {
            currentSlide++;
            updateCarousel();
        }
    };

    window.prevSlide = function() {
        if (currentSlide > 0) {
            currentSlide--;
            updateCarousel();
        }
    };

    function updateCarousel() {
        if (cards[currentSlide]) {
            cards[currentSlide].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
        }
        if (counter) {
            counter.textContent = `${currentSlide + 1} of ${cards.length}`;
        }
    }

    // Experience modal
    window.editExperience = function(index) {
        const exp = experienceData[index];
        if (!exp) return;
        
        document.getElementById('exp-modal-title').textContent = 'Editar experiencia';
        document.getElementById('exp-title-input').value = exp.title || '';
        document.getElementById('exp-company-input').value = exp.company || '';
        document.getElementById('exp-period-input').value = exp.period || '';
        document.getElementById('exp-description-input').value = exp.description || '';
        document.getElementById('exp-edit-index').value = index;
        
        openModal('experience-modal');
    };

    window.deleteExperience = async function(index) {
        if (!confirm('Eliminar esta experiencia?')) return;
        
        experienceData.splice(index, 1);
        await saveExperienceData();
        location.reload();
    };

    window.saveExperience = async function() {
        const title = document.getElementById('exp-title-input').value;
        const company = document.getElementById('exp-company-input').value;
        const period = document.getElementById('exp-period-input').value;
        const description = document.getElementById('exp-description-input').value;
        const editIndex = parseInt(document.getElementById('exp-edit-index').value);
        
        const exp = { title, company, period, description };
        
        if (editIndex >= 0) {
            experienceData[editIndex] = exp;
        } else {
            experienceData.push(exp);
        }
        
        await saveExperienceData();
        location.reload();
    };

    window.editProject = function(index) {
        const project = projectsData[index];
        if (!project) return;
        
        document.getElementById('exp-modal-title').textContent = 'Editar proyecto';
        document.getElementById('exp-title-input').value = project.title || '';
        document.getElementById('exp-company-input').value = project.company || '';
        document.getElementById('exp-period-input').value = project.period || '';
        document.getElementById('exp-description-input').value = project.description || '';
        document.getElementById('exp-edit-index').value = 'proj_' + index;
        
        openModal('experience-modal');
    };

    window.deleteProject = async function(index) {
        if (!confirm('Eliminar este proyecto?')) return;
        
        projectsData.splice(index, 1);
        await saveExperienceData();
        location.reload();
    };

    async function saveExperienceData() {
        try {
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    experience: experienceData,
                    projects: projectsData
                })
            });
            
            return response.ok;
        } catch (error) {
            console.error('Error:', error);
            return false;
        }
    }

    // Social links
    window.saveSocialLinks = async function() {
        const socialLinks = {
            linkedin: document.getElementById('social-linkedin').value,
            github: document.getElementById('social-github').value,
            twitter: document.getElementById('social-twitter').value,
            portfolio: document.getElementById('social-portfolio').value
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

    // Profile visibility toggle
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

    // Skills modal
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

    window.searchTags = function(query) {
        const suggestions = document.getElementById('tag-suggestions');
        if (!suggestions) return;
        if (!query || query.length < 2) {
            suggestions.classList.add('hidden');
            return;
        }
        const filtered = allTags.filter(tag => 
            tag.name.toLowerCase().includes(query.toLowerCase()) ||
            tag.slug.includes(query.toLowerCase())
        ).slice(0, 10);
        
        if (filtered.length === 0) {
            suggestions.classList.add('hidden');
            return;
        }
        
        suggestions.innerHTML = filtered.map(tag => 
            '<div class="px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 cursor-pointer" onclick="addTag(\'' + tag.slug + '\', \'' + tag.name + '\')">' + tag.name + '</div>'
        ).join('');
        suggestions.classList.remove('hidden');
    };

    window.addTag = function(slug, name) {
        if (!selectedTags.find(t => t.slug === slug)) {
            selectedTags.push({ slug, name });
            renderSelectedTags();
        }
        document.getElementById('tag-search-input').value = '';
        document.getElementById('tag-suggestions').classList.add('hidden');
    };

    window.removeTag = function(slug) {
        selectedTags = selectedTags.filter(t => t.slug !== slug);
        renderSelectedTags();
    };

    function renderSelectedTags() {
        const container = document.getElementById('selected-tags');
        if (!container) return;
        container.innerHTML = selectedTags.map(tag => 
            '<span class="inline-flex items-center px-3 py-1 rounded-full text-sm bg-indigo-100 dark:bg-indigo-900 text-indigo-800 dark:text-indigo-200">' + 
            tag.name + 
            '<button onclick="removeTag(\'' + tag.slug + '\')" class="ml-2 text-indigo-600 dark:text-indigo-400 hover:text-indigo-800">&times;</button></span>'
        ).join('');
    }

    window.addLanguage = function() {
        const select = document.getElementById('language-select');
        const code = select.value;
        const name = select.options[select.selectedIndex].text;
        if (code && !selectedLanguages.find(l => l.code === code)) {
            selectedLanguages.push({ code, name });
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
        container.innerHTML = selectedLanguages.map(lang => 
            '<span class="inline-flex items-center px-3 py-1 rounded-full text-sm bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200">' + 
            lang.name + 
            '<button onclick="removeLanguage(\'' + lang.code + '\')" class="ml-2 text-green-600 dark:text-green-400 hover:text-green-800">&times;</button></span>'
        ).join('');
    }

    window.saveSkills = async function() {
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
                    sector,
                    rol,
                    especialidad,
                    seniority,
                    tags: selectedTags.map(t => ({ slug: t.slug, tag_type: 'nice' })),
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
            alert('Error de conexion: ' + error.message);
        }
    };

    // Skills modal cascading dropdowns
    document.getElementById('skills-sector-select').addEventListener('change', function() {
        const sectorSlug = this.value;
        populateSkillsRolDropdown(sectorSlug);
        document.getElementById('skills-especialidad-select').innerHTML = '<option value="">Seleccionar especialidad...</option>';
    });

    document.getElementById('skills-rol-select').addEventListener('change', function() {
        const sectorSlug = document.getElementById('skills-sector-select').value;
        const rolSlug = this.value;
        populateSkillsEspecialidadDropdown(sectorSlug, rolSlug);
    });

    // Initialize skills modal
    loadHierarchy();
    loadAllTags();
});