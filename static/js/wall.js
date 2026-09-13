document.addEventListener('DOMContentLoaded', function() {
    const profileGrid = document.getElementById('cv-grid');
    const loading = document.getElementById('loading');
    const noResults = document.getElementById('no-results');
    const filtersContainer = document.getElementById('filters');
    const sectorCarousel = document.getElementById('sector-carousel');

    let currentFilter = 'all';
    let sectors = [];

    function escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    const sectorIcons = {
        'tecnologia': '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>',
        'diseno': '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"></path></svg>',
        'marketing': '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"></path></svg>',
        'finanzas': '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599 1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>',
        'educacion': '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M12 14l9-5-9-5-9 5 9 5z"></path><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"></path></svg>',
        'salud': '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>',
        'default': '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>',
    };

    function getSectorIcon(name) {
        const lower = name.toLowerCase();
        for (const [key, icon] of Object.entries(sectorIcons)) {
            if (lower.includes(key)) return icon;
        }
        return sectorIcons['default'];
    }

    const INACTIVE_FILTER = ['bg-gray-200', 'dark:bg-gray-700', 'text-gray-700', 'dark:text-gray-300'];
    const ACTIVE_FILTER = ['bg-indigo-600', 'dark:bg-indigo-500', 'text-white'];
    const INACTIVE_CHIP = ['bg-gray-100', 'dark:bg-gray-700', 'text-gray-700', 'dark:text-gray-300'];

    function setActiveFilter(slug) {
        currentFilter = slug;

        sectorCarousel.querySelectorAll('.sector-chip').forEach(c => {
            c.classList.remove('active', 'bg-indigo-600', 'text-white');
            c.classList.add(...INACTIVE_CHIP);
        });
        const activeChip = sectorCarousel.querySelector('.sector-chip[data-slug="' + slug + '"]');
        if (activeChip) {
            activeChip.classList.remove(...INACTIVE_CHIP);
            activeChip.classList.add('active', 'bg-indigo-600', 'text-white');
        }

        filtersContainer.querySelectorAll('.filter-btn').forEach(b => {
            b.classList.remove('active', ...ACTIVE_FILTER);
            b.classList.add(...INACTIVE_FILTER);
        });
        const activeBtn = filtersContainer.querySelector('.filter-btn[data-slug="' + slug + '"]');
        if (activeBtn) {
            activeBtn.classList.remove(...INACTIVE_FILTER);
            activeBtn.classList.add('active', ...ACTIVE_FILTER);
        }

        loadProfiles();
    }

    async function loadSectors() {
        try {
            const response = await fetch(tagsApiUrl);
            const data = await response.json();
            sectors = data.tags || [];
            renderSectorCarousel();
            renderFilters();
        } catch (error) {
            console.error('Error loading sectors:', error);
        }
    }

    function renderSectorCarousel() {
        sectorCarousel.innerHTML = '';

        const allChip = document.createElement('button');
        allChip.className = 'sector-chip active flex-shrink-0 flex items-center gap-2 px-4 py-2 rounded-full text-sm font-semibold bg-indigo-600 text-white transition';
        allChip.dataset.slug = 'all';
        allChip.innerHTML = '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"></path></svg> Todos';
        allChip.addEventListener('click', function() {
            setActiveFilter('all');
        });
        sectorCarousel.appendChild(allChip);

        sectors.forEach(sector => {
            const chip = document.createElement('button');
            chip.className = 'sector-chip flex-shrink-0 flex items-center gap-2 px-4 py-2 rounded-full text-sm font-semibold bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 transition';
            chip.dataset.slug = sector.slug;
            chip.dataset.id = sector.id;
            chip.innerHTML = getSectorIcon(sector.name) + ' ' + escapeHtml(sector.name);
            chip.addEventListener('click', function() {
                setActiveFilter(this.dataset.slug);
            });
            sectorCarousel.appendChild(chip);
        });
    }

    function renderFilters() {
        filtersContainer.querySelectorAll('.filter-btn[data-slug!="all"]').forEach(btn => btn.remove());

        sectors.forEach(sector => {
            const btn = document.createElement('button');
            btn.className = 'filter-btn px-4 py-2 rounded-full text-sm font-semibold transition duration-200 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600';
            btn.dataset.slug = sector.slug;
            btn.dataset.id = sector.id;
            btn.textContent = sector.name;
            btn.addEventListener('click', function() {
                setActiveFilter(this.dataset.slug);
            });
            filtersContainer.appendChild(btn);
        });
    }

    async function loadProfiles() {
        loading.classList.remove('hidden');
        profileGrid.innerHTML = '';
        noResults.classList.add('hidden');

        try {
            let url = wallApiUrl;
            if (currentFilter !== 'all') {
                url += '?sector=' + currentFilter;
            }

            const response = await fetch(url);
            const data = await response.json();

            loading.classList.add('hidden');

            if (data.profiles && data.profiles.length > 0) {
                renderProfiles(data.profiles);
            } else {
                noResults.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error loading profiles:', error);
            loading.classList.add('hidden');
            noResults.classList.remove('hidden');
        }
    }

    function renderProfiles(profiles) {
        profileGrid.innerHTML = '';

        profiles.forEach(profile => {
            const card = createProfileCard(profile);
            profileGrid.appendChild(card);
        });
    }

    function createProfileCard(profile) {
        const card = document.createElement('div');
        card.className = 'bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300';

        const photoUrl = profile.photo || '';
        const safeName = escapeHtml(profile.name);
        const headline = profile.headline || '';
        const location = profile.location || '';
        const sector = profile.sector || '';
        const truncatedBio = profile.bio && profile.bio.length > 80
            ? escapeHtml(profile.bio.substring(0, 80)) + '...'
            : escapeHtml(profile.bio) || 'Sin descripcion';

        const tagsHtml = [];
        if (sector) tagsHtml.push('<span class="bg-indigo-100 dark:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(sector) + '</span>');
        if (location) tagsHtml.push('<span class="bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(location) + '</span>');

        const safeProfileUrl = '/candidato/' + (parseInt(profile.user_id) || 0) + '/';

        card.innerHTML = 
            '<div class="aspect-square bg-gray-100 dark:bg-gray-700 relative">' +
                '<img src="' + escapeHtml(photoUrl) + '" alt="' + safeName + '"' +
                    'class="w-full h-full object-cover">' +
            '</div>' +
            '<div class="p-4">' +
                '<h3 class="font-semibold text-gray-900 dark:text-white text-lg mb-1">' + safeName + '</h3>' +
                (headline ? '<p class="text-gray-600 dark:text-gray-400 text-sm mb-1">' + escapeHtml(headline) + '</p>' : '') +
                (location ? '<p class="text-gray-500 dark:text-gray-500 text-xs mb-2">' + escapeHtml(location) + '</p>' : '') +
                '<p class="text-gray-600 dark:text-gray-400 text-sm mb-3">' + truncatedBio + '</p>' +
                '<div class="flex flex-wrap gap-1">' +
                    tagsHtml.join('') +
                '</div>' +
            '</div>';

        card.addEventListener('click', function() {
            window.location.href = safeProfileUrl;
        });

        card.style.cursor = 'pointer';

        return card;
    }

    loadSectors();
    loadProfiles();
});
