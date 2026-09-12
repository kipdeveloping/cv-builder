document.addEventListener('DOMContentLoaded', function() {
    let currentSlide = 0;
    const carousel = document.getElementById('carousel-container');
    const cards = carousel ? carousel.querySelectorAll('.carousel-card') : [];
    const counter = document.getElementById('carousel-counter');
    
    if (typeof experienceData === 'undefined') window.experienceData = [];
    if (typeof projectsData === 'undefined') window.projectsData = [];
    if (typeof socialLinksData === 'undefined') window.socialLinksData = {};
    if (typeof currentResumeId === 'undefined') window.currentResumeId = null;

    window.dashboardContent = {};
    const dcNode = document.getElementById('dashboardContent');
    if (dcNode) {
        try { window.dashboardContent = JSON.parse(dcNode.textContent) || {}; } catch (e) { window.dashboardContent = {}; }
    }

    function getFullContent() {
        return Object.assign({}, window.dashboardContent);
    }

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

    // Skills management
    window.addSkill = function() {
        const input = document.getElementById('new-skill-input');
        const skillName = input.value.trim();
        if (!skillName) return;
        
        const skillsList = document.getElementById('skills-list-modal');
        const skillId = 'new_' + Date.now();
        
        const skillDiv = document.createElement('div');
        skillDiv.className = 'flex items-center justify-between p-2 bg-gray-50 rounded-lg skill-item';
        skillDiv.dataset.skillId = skillId;
        skillDiv.innerHTML = `
            <span class="text-sm">${skillName}</span>
            <div class="flex items-center gap-2">
                <button onclick="togglePrimary('${skillId}')" class="text-yellow-500 hover:text-yellow-600 opacity-50" title="Principal">
                    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                    </svg>
                </button>
                <button onclick="removeSkill('${skillId}')" class="text-red-500 hover:text-red-600">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                </button>
            </div>
        `;
        skillsList.appendChild(skillDiv);
        input.value = '';
    };

    window.removeSkill = function(skillId) {
        const item = document.querySelector(`[data-skill-id="${skillId}"]`);
        if (item) item.remove();
    };

    window.togglePrimary = function(skillId) {
        document.querySelectorAll('.skill-item button[title="Principal"]').forEach(btn => {
            btn.classList.add('opacity-50');
        });
        const item = document.querySelector(`[data-skill-id="${skillId}"]`);
        if (item) {
            const starBtn = item.querySelector('button[title="Principal"]');
            starBtn.classList.remove('opacity-50');
        }
    };

    // Save headline
    window.saveHeadline = async function() {
        const headline = document.getElementById('headline-input').value;
        if (!currentResumeId) {
            alert('Por favor, crea un CV primero antes de guardar.');
            return;
        }
        try {
            console.log('Saving headline:', headline);
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({ headline: headline })
            });
            
            const result = await response.json();
            console.log('Response:', result);
            
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
            console.log('Saving bio:', bio);
            const response = await fetch(urls.updateProfile, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({ bio: bio })
            });
            
            const result = await response.json();
            console.log('Response:', result);
            
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
            console.log('Saving status:', { searchStatus, availability, locationFlex });
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
            console.log('Response:', result);
            
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

    // Save skills
    window.saveSkills = async function() {
        const skills = [];
        let primarySkill = null;
        
        document.querySelectorAll('.skill-item').forEach(item => {
            const skillId = item.dataset.skillId;
            const skillName = item.querySelector('span').textContent;
            const isPrimary = !item.querySelector('button[title="Principal"]').classList.contains('opacity-50');
            
            if (isPrimary) primarySkill = skillName;
            skills.push(skillName);
        });
        
        if (!currentResumeId) {
            alert('Por favor, crea un CV primero antes de guardar.');
            return;
        }
        
        try {
            const content = getFullContent();
            content.skills = skills;
            const response = await fetch('/api/resume/save/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    resume_id: currentResumeId,
                    content: content
                })
            });
            
            if (response.ok) {
                location.reload();
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    // CV list modal
    window.setFeatured = async function(resumeId) {
        try {
            const response = await fetch(urls.setFeatured, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({ resume_id: resumeId })
            });
            
            if (response.ok) {
                location.reload();
            }
        } catch (error) {
            console.error('Error:', error);
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
        if (!currentResumeId) {
            alert('Por favor, crea un CV primero antes de guardar.');
            return false;
        }
        
        try {
            const content = getFullContent();
            content.experience = experienceData;
            content.projects = projectsData;
            const response = await fetch('/api/resume/save/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    resume_id: currentResumeId,
                    content: content
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
        
        if (!currentResumeId) {
            alert('Por favor, crea un CV primero antes de guardar.');
            return;
        }
        
        try {
            const content = getFullContent();
            content.social_links = socialLinks;
            const response = await fetch('/api/resume/save/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({
                    resume_id: currentResumeId,
                    content: content
                })
            });
            
            if (response.ok) {
                location.reload();
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };
});
