document.addEventListener('DOMContentLoaded', function() {
    const cvGrid = document.getElementById('cv-grid');
    const loading = document.getElementById('loading');
    const noResults = document.getElementById('no-results');
    const filtersContainer = document.getElementById('filters');

    let currentFilter = 'all';
    let tags = [];

    async function loadTags() {
        try {
            const response = await fetch(tagsApiUrl);
            const data = await response.json();
            tags = data.tags || [];
            renderFilters();
        } catch (error) {
            console.error('Error loading tags:', error);
        }
    }

    function renderFilters() {
        const allBtn = filtersContainer.querySelector('[data-slug="all"]');

        tags.forEach(tag => {
            const btn = document.createElement('button');
            btn.className = 'filter-btn px-4 py-2 rounded-full text-sm font-semibold transition duration-200 bg-gray-200 text-gray-700 hover:bg-gray-300';
            btn.dataset.slug = tag.slug;
            btn.dataset.id = tag.id;
            btn.textContent = tag.name;
            filtersContainer.appendChild(btn);
        });

        filtersContainer.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                filtersContainer.querySelectorAll('.filter-btn').forEach(b => {
                    b.classList.remove('bg-indigo-600', 'text-white');
                    b.classList.add('bg-gray-200', 'text-gray-700');
                });
                this.classList.remove('bg-gray-200', 'text-gray-700');
                this.classList.add('bg-indigo-600', 'text-white');

                currentFilter = this.dataset.slug;
                loadCVs();
            });
        });
    }

    async function loadCVs() {
        loading.classList.remove('hidden');
        cvGrid.innerHTML = '';
        noResults.classList.add('hidden');

        try {
            let url = wallApiUrl;
            if (currentFilter !== 'all') {
                url += `?sector=${currentFilter}`;
            }

            const response = await fetch(url);
            const data = await response.json();

            loading.classList.add('hidden');

            if (data.cvs && data.cvs.length > 0) {
                renderCVs(data.cvs);
            } else {
                noResults.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error loading CVs:', error);
            loading.classList.add('hidden');
            noResults.classList.remove('hidden');
        }
    }

    function renderCVs(cvs) {
        cvGrid.innerHTML = '';

        cvs.forEach(cv => {
            const card = createCVCard(cv);
            cvGrid.appendChild(card);
        });
    }

    function createCVCard(cv) {
        const card = document.createElement('div');
        card.className = 'bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300';

        const photoUrl = cv.photo || '/static/img/default-avatar.png';
        const truncatedBio = cv.bio && cv.bio.length > 80
            ? cv.bio.substring(0, 80) + '...'
            : cv.bio || 'Sin descripción';

        const tagsHtml = cv.tags && cv.tags.length > 0
            ? cv.tags.map(tag => `<span class="bg-indigo-100 text-indigo-800 text-xs px-2 py-1 rounded-full">${tag}</span>`).join('')
            : '';

        card.innerHTML = `
            <div class="aspect-square bg-gray-100 relative">
                <img src="${photoUrl}" alt="${cv.name}"
                    class="w-full h-full object-cover">
            </div>
            <div class="p-4">
                <h3 class="font-semibold text-gray-900 text-lg mb-1">${cv.name}</h3>
                <p class="text-gray-600 text-sm mb-3">${truncatedBio}</p>
                <div class="flex flex-wrap gap-1">
                    ${tagsHtml}
                </div>
            </div>
        `;

        card.addEventListener('click', function() {
            window.location.href = `/candidato/${cv.user_id}/`;
        });

        card.style.cursor = 'pointer';

        return card;
    }

    loadTags();
    loadCVs();
});
