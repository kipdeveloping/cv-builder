document.addEventListener('DOMContentLoaded', function() {
    const publishBtn = document.getElementById('publish-btn');
    const publishModal = document.getElementById('publish-modal');
    const cancelPublish = document.getElementById('cancel-publish');
    const confirmPublish = document.getElementById('confirm-publish');
    const tagsContainer = document.getElementById('tags-container');
    const primaryTagSelect = document.getElementById('primary-tag-select');
    const publishError = document.getElementById('publish-error');

    let availableTags = [];

    async function loadTags() {
        try {
            const response = await fetch(tagsUrl);
            const data = await response.json();
            availableTags = data.tags || [];
            renderTags();
        } catch (error) {
            console.error('Error loading tags:', error);
        }
    }

    function renderTags() {
        tagsContainer.innerHTML = '';
        primaryTagSelect.innerHTML = '';

        availableTags.forEach(tag => {
            const checkbox = document.createElement('label');
            checkbox.className = 'flex items-center space-x-2 p-2 rounded hover:bg-gray-50';
            checkbox.innerHTML = `
                <input type="checkbox" value="${tag.id}" class="tag-checkbox rounded text-indigo-600 focus:ring-indigo-500">
                <span>${tag.name}</span>
            `;
            tagsContainer.appendChild(checkbox);

            const option = document.createElement('option');
            option.value = tag.id;
            option.textContent = tag.name;
            primaryTagSelect.appendChild(option);
        });
    }

    function showModal() {
        publishError.classList.add('hidden');
        publishModal.classList.remove('hidden');
        publishModal.classList.add('flex');
    }

    function hideModal() {
        publishModal.classList.add('hidden');
        publishModal.classList.remove('flex');
    }

    function getSelectedTags() {
        const checkboxes = document.querySelectorAll('.tag-checkbox:checked');
        return Array.from(checkboxes).map(cb => parseInt(cb.value));
    }

    async function publishResume() {
        const tags = getSelectedTags();
        const primaryTag = parseInt(primaryTagSelect.value);

        if (tags.length === 0) {
            publishError.textContent = 'Debes seleccionar al menos un sector.';
            publishError.classList.remove('hidden');
            return;
        }

        if (!primaryTag || !tags.includes(primaryTag)) {
            publishError.textContent = 'Debes seleccionar un sector principal válido.';
            publishError.classList.remove('hidden');
            return;
        }

        confirmPublish.disabled = true;
        confirmPublish.textContent = 'Publicando...';

        try {
            const response = await fetch(publishUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({
                    resume_id: resumeId,
                    tags: tags,
                    primary_tag: primaryTag
                })
            });

            const result = await response.json();

            if (result.status === 'ok') {
                hideModal();
                location.reload();
            } else {
                publishError.textContent = result.message || 'Error al publicar.';
                publishError.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error publishing:', error);
            publishError.textContent = 'Error de conexión. Inténtalo de nuevo.';
            publishError.classList.remove('hidden');
        } finally {
            confirmPublish.disabled = false;
            confirmPublish.textContent = 'Confirmar publicación';
        }
    }

    if (publishBtn) {
        publishBtn.addEventListener('click', function() {
            loadTags();
            showModal();
        });
    }

    if (cancelPublish) {
        cancelPublish.addEventListener('click', hideModal);
    }

    if (confirmPublish) {
        confirmPublish.addEventListener('click', publishResume);
    }

    publishModal.addEventListener('click', function(e) {
        if (e.target === publishModal) {
            hideModal();
        }
    });
});
