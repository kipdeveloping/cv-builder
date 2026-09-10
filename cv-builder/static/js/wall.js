document.addEventListener('DOMContentLoaded', function() {
    const cvGrid = document.getElementById('cv-grid');
    const loading = document.getElementById('loading');
    const noResults = document.getElementById('no-results');
    const track = document.getElementById('sector-track');
    const windowEl = document.getElementById('sector-window');
    const prevBtn = document.getElementById('prev-sector');
    const nextBtn = document.getElementById('next-sector');
    const allSectorsBtn = document.getElementById('all-sectors-btn');
    const allSectorsMenu = document.getElementById('all-sectors-menu');
    const allSectorsList = document.getElementById('all-sectors-list');
    const allSectorsEmpty = document.getElementById('all-sectors-empty');
    const sectorSearch = document.getElementById('sector-search');
    const sectorSearchClear = document.getElementById('sector-search-clear');
    const carousel = document.getElementById('sector-carousel');

    let currentIndex = 0;
    let tags = [];
    let step = 0;
    let allSectorItems = [];
    let lastQuery = '';
    const GAP = 8;

    const ACTIVE_CLS = ['bg-indigo-600', 'text-white'];
    const INACTIVE_CLS = ['bg-gray-200', 'text-gray-700', 'hover:bg-gray-300',
        'dark:bg-gray-700', 'dark:text-gray-300', 'dark:hover:bg-gray-600'];

    async function loadTags() {
        try {
            const response = await fetch(tagsApiUrl);
            if (response.status === 401 || response.status === 403) {
                redirectToLogin();
                return;
            }
            const data = await response.json();
            tags = data.tags || [];
            renderFilters();
        } catch (error) {
            console.error('Error loading tags:', error);
            renderFilters();
        }
    }

    function redirectToLogin() {
        const next = encodeURIComponent('/tablon/');
        window.location.href = '/accounts/login/?next=' + next;
    }

    function buildPill(tag, compact) {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = (compact
            ? 'filter-btn px-3 py-1.5 rounded-full text-sm font-semibold transition duration-200 whitespace-nowrap '
            : 'w-full text-left px-3 py-1.5 rounded-md text-sm font-medium transition duration-200 ')
            + 'bg-gray-200 text-gray-700 hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600';
        btn.dataset.slug = tag.slug;
        btn.dataset.id = tag.id;
        btn.textContent = tag.name;
        return btn;
    }

    function renderFilters() {
        track.replaceChildren();

        const allBtn = document.createElement('button');
        allBtn.type = 'button';
        allBtn.className = 'filter-btn active px-3 py-1.5 rounded-full text-sm font-semibold transition duration-200 bg-indigo-600 text-white whitespace-nowrap';
        allBtn.dataset.slug = 'all';
        allBtn.textContent = 'Todos';
        track.appendChild(allBtn);

        tags.forEach(tag => {
            const btn = buildPill(tag, true);
            track.appendChild(btn);
        });

        const pills = Array.from(track.querySelectorAll('.filter-btn'));
        pills.forEach((btn, index) => {
            btn.addEventListener('click', function() {
                selectFilter(index);
            });
        });

        buildAllSectorItems();
        renderAllSectorsList(allSectorItems);
        requestAnimationFrame(function() {
            requestAnimationFrame(measureAndCenter);
        });
    }

    function buildAllSectorItems() {
        allSectorItems = [
            { slug: 'all', name: 'Todos', index: 0 }
        ];
        tags.forEach(function(tag, i) {
            allSectorItems.push({ slug: tag.slug, name: tag.name, index: i + 1 });
        });
    }

    function renderAllSectorsList(items) {
        allSectorsList.innerHTML = '';
        const list = items || allSectorItems;
        if (!list.length) {
            allSectorsEmpty.classList.remove('hidden');
            return;
        }
        allSectorsEmpty.classList.add('hidden');

        list.forEach(function(item) {
            const el = document.createElement('button');
            el.type = 'button';
            el.className = 'w-full text-left px-3 py-1.5 rounded-md text-sm font-medium transition duration-200 '
                + (item.index === currentIndex
                    ? 'bg-indigo-600 text-white'
                    : 'text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700');
            el.textContent = item.name;
            el.dataset.index = item.index;
            el.addEventListener('click', function() {
                selectFilter(item.index);
                allSectorsMenu.classList.add('hidden');
            });
            allSectorsList.appendChild(el);
        });
    }

    function filterAllSectors(query) {
        lastQuery = query;
        const q = query.trim().toLowerCase();
        if (!q) {
            renderAllSectorsList(allSectorItems);
            return;
        }
        renderAllSectorsList(allSectorItems.filter(function(item) {
            return item.name.toLowerCase().includes(q);
        }));
    }

    function getPills() {
        return Array.from(track.querySelectorAll('.filter-btn'));
    }

    function measureAndCenter() {
        const pills = getPills();
        if (!pills.length) return;
        step = pills[0].offsetWidth + GAP;
        windowEl.style.width = (step * 3 - GAP) + 'px';
        updateTrack(currentIndex);
    }

    function updateTrack(index) {
        const pills = getPills();
        const target = pills[index];
        if (!target) return;
        track.style.transform = 'translateX(' + (-target.offsetLeft) + 'px)';
    }

    function selectFilter(index) {
        const pills = getPills();
        if (!pills.length) return;
        if (index < 0) index = 0;
        if (index > pills.length - 1) index = pills.length - 1;

        pills.forEach(b => {
            b.classList.remove(...ACTIVE_CLS);
            b.classList.add(...INACTIVE_CLS);
        });

        const active = pills[index];
        active.classList.remove(...INACTIVE_CLS);
        active.classList.add(...ACTIVE_CLS);

        currentIndex = index;
        currentFilter = active.dataset.slug;

        if (step) {
            updateTrack(index);
        }

        prevBtn.disabled = index <= 0;
        nextBtn.disabled = index >= pills.length - 1;

        renderAllSectorsList(allSectorItems.filter(function(item) {
            const q = lastQuery.trim().toLowerCase();
            return !q || item.name.toLowerCase().includes(q);
        }));

        loadCVs();
    }

    function toggleMenu() {
        allSectorsMenu.classList.toggle('hidden');
        if (!allSectorsMenu.classList.contains('hidden')) {
            if (sectorSearch) {
                sectorSearch.value = '';
            }
            if (sectorSearchClear) {
                sectorSearchClear.classList.add('hidden');
            }
            lastQuery = '';
            renderAllSectorsList(allSectorItems);
        }
    }

    function setupCarousel() {
        if (prevBtn) {
            prevBtn.addEventListener('click', function() {
                selectFilter(currentIndex - 1);
            });
        }
        if (nextBtn) {
            nextBtn.addEventListener('click', function() {
                selectFilter(currentIndex + 1);
            });
        }

        if (allSectorsBtn) {
            allSectorsBtn.addEventListener('click', function() {
                toggleMenu();
            });
        }
        if (sectorSearch) {
            sectorSearch.addEventListener('input', function() {
                const hasQuery = sectorSearch.value.length > 0;
                sectorSearchClear.classList.toggle('hidden', !hasQuery);
                filterAllSectors(sectorSearch.value);
            });
        }
        if (sectorSearchClear) {
            sectorSearchClear.addEventListener('click', function() {
                sectorSearch.value = '';
                sectorSearchClear.classList.add('hidden');
                filterAllSectors('');
                sectorSearch.focus();
            });
        }
        document.addEventListener('click', function(event) {
            if (!carousel.contains(event.target)) {
                allSectorsMenu.classList.add('hidden');
            }
        });

        window.addEventListener('resize', function() {
            measureAndCenter();
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
            if (response.status === 401 || response.status === 403) {
                redirectToLogin();
                return;
            }
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
        card.className = 'bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300';

        const photoUrl = cv.photo || '/static/img/default-avatar.png';
        const truncatedBio = cv.bio && cv.bio.length > 80
            ? cv.bio.substring(0, 80) + '...'
            : cv.bio || 'Sin descripción';

        const tagsHtml = cv.tags && cv.tags.length > 0
            ? cv.tags.map(tag => `<span class="bg-indigo-100 dark:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 text-xs px-2 py-1 rounded-full">${tag}</span>`).join('')
            : '';

        card.innerHTML = `
            <div class="aspect-square bg-gray-100 dark:bg-gray-700 relative">
                <img src="${photoUrl}" alt="${cv.name}"
                    class="w-full h-full object-cover">
            </div>
            <div class="p-4">
                <h3 class="font-semibold text-gray-900 dark:text-white text-lg mb-1">${cv.name}</h3>
                <p class="text-gray-600 dark:text-gray-400 text-sm mb-3">${truncatedBio}</p>
                <div class="flex flex-wrap gap-1">
                    ${tagsHtml}
                </div>
            </div>
        `;

        card.addEventListener('click', function() {
            window.location.href = `/cv/${cv.id}/`;
        });

        card.style.cursor = 'pointer';

        return card;
    }

    let currentFilter = 'all';
    loadTags();
    loadCVs();
    setupCarousel();
});