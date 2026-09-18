function getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return '';
}

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
    }
}

async function saveBio() {
    const bio = document.getElementById('bio-input').value;
    try {
        const response = await fetch(urls.updateRecruiterProfile, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ company_description: bio })
        });
        if (response.ok) {
            document.getElementById('bio-display').textContent = bio || 'Sin descripcion';
            closeModal('bio-modal');
        } else {
            const data = await response.json();
            alert(data.message || 'Error al guardar');
        }
    } catch (error) {
        alert('Error de conexion');
    }
}

async function saveSocialLinks() {
    const socialLinks = {
        linkedin: document.getElementById('social-linkedin').value,
        twitter: document.getElementById('social-twitter').value,
        website: document.getElementById('social-website').value
    };
    try {
        const response = await fetch(urls.updateRecruiterProfile, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ social_links: socialLinks })
        });
        if (response.ok) {
            location.reload();
        } else {
            const data = await response.json();
            alert(data.message || 'Error al guardar');
        }
    } catch (error) {
        alert('Error de conexion');
    }
}

async function toggleVisibility() {
    const toggle = document.getElementById('visibility-toggle');
    const dot = document.getElementById('visibility-dot');
    const wasPublic = toggle.getAttribute('aria-checked') === 'true';
    
    // Optimistic update
    toggle.setAttribute('aria-checked', !wasPublic);
    if (wasPublic) {
        toggle.classList.remove('bg-indigo-600');
        toggle.classList.add('bg-gray-300', 'dark:bg-gray-600');
        dot.classList.remove('translate-x-5');
        dot.classList.add('translate-x-0');
    } else {
        toggle.classList.remove('bg-gray-300', 'dark:bg-gray-600');
        toggle.classList.add('bg-indigo-600');
        dot.classList.remove('translate-x-0');
        dot.classList.add('translate-x-5');
    }
    
    try {
        const response = await fetch(urls.toggleVisibility, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        });
        if (!response.ok) {
            // Revert on error
            toggle.setAttribute('aria-checked', wasPublic);
            if (wasPublic) {
                toggle.classList.remove('bg-gray-300', 'dark:bg-gray-600');
                toggle.classList.add('bg-indigo-600');
                dot.classList.remove('translate-x-0');
                dot.classList.add('translate-x-5');
            } else {
                toggle.classList.remove('bg-indigo-600');
                toggle.classList.add('bg-gray-300', 'dark:bg-gray-600');
                dot.classList.remove('translate-x-5');
                dot.classList.add('translate-x-0');
            }
        }
    } catch (error) {
        location.reload();
    }
}
