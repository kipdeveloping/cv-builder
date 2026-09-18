document.addEventListener('DOMContentLoaded', function() {
    const recruiterGrid = document.getElementById('recruiter-grid');
    const loading = document.getElementById('loading');
    const noResults = document.getElementById('no-results');
    const sectorInput = document.getElementById('sector-input');
    const sectorChips = document.getElementById('sector-chips');
    const sectorSuggestions = document.getElementById('sector-suggestions');
    const modalityRemote = document.getElementById('modality-remote');
    const modalityHybrid = document.getElementById('modality-hybrid');
    const modalityOnsite = document.getElementById('modality-onsite');
    const clearFilters = document.getElementById('clear-filters');
    const companyTypeRadios = document.querySelectorAll('input[name="company_type"]');

    let allSectors = [];
    let selectedSectors = [];
    let searchTimeout = null;

    function escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    async function loadSectors() {
        try {
            const response = await fetch(tagsApiUrl);
            const data = await response.json();
            allSectors = data.tags || [];
        } catch (error) {
            console.error('Error loading sectors:', error);
        }
    }

    function searchSectors(query) {
        if (!query) return [];
        const lower = query.toLowerCase();
        return allSectors.filter(sector =>
            sector.name.toLowerCase().includes(lower) ||
            sector.slug.toLowerCase().includes(lower)
        ).slice(0, 10);
    }

    function renderSectorChips() {
        sectorChips.innerHTML = '';
        selectedSectors.forEach(sector => {
            const chip = document.createElement('span');
            chip.className = 'inline-flex items-center gap-1 px-3 py-1 rounded-full text-sm font-semibold bg-indigo-100 dark:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200';
            chip.innerHTML = escapeHtml(sector.name) +
                '<button type="button" class="ml-1 hover:text-indigo-600 dark:hover:text-indigo-300" data-slug="' + sector.slug + '">' +
                '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">' +
                '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>' +
                '</svg></button>';
            sectorChips.appendChild(chip);
        });
    }

    function addSector(sector) {
        if (selectedSectors.find(s => s.slug === sector.slug)) return;
        selectedSectors.push(sector);
        renderSectorChips();
        loadRecruiters();
    }

    function removeSector(slug) {
        selectedSectors = selectedSectors.filter(s => s.slug !== slug);
        renderSectorChips();
        loadRecruiters();
    }

    sectorChips.addEventListener('click', function(e) {
        const btn = e.target.closest('button[data-slug]');
        if (btn) removeSector(btn.dataset.slug);
    });

    sectorInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const suggestions = searchSectors(this.value);
            showSuggestions(suggestions);
        }, 300);
    });

    function showSuggestions(suggestions) {
        sectorSuggestions.innerHTML = '';
        if (suggestions.length === 0) {
            sectorSuggestions.classList.add('hidden');
            return;
        }

        suggestions.forEach(sector => {
            const item = document.createElement('div');
            item.className = 'px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 cursor-pointer text-sm text-gray-900 dark:text-white';
            item.textContent = sector.name;
            item.addEventListener('click', function() {
                addSector(sector);
                sectorSuggestions.classList.add('hidden');
                sectorInput.value = '';
            });
            sectorSuggestions.appendChild(item);
        });

        sectorSuggestions.classList.remove('hidden');
    }

    document.addEventListener('click', function(e) {
        if (!sectorInput.contains(e.target) && !sectorSuggestions.contains(e.target)) {
            sectorSuggestions.classList.add('hidden');
        }
    });

    function getSelectedModalities() {
        const modalities = [];
        if (modalityRemote.checked) modalities.push('remote');
        if (modalityHybrid.checked) modalities.push('hybrid');
        if (modalityOnsite.checked) modalities.push('onsite');
        return modalities;
    }

    function getSelectedCompanyType() {
        const checked = document.querySelector('input[name="company_type"]:checked');
        return checked ? checked.value : '';
    }

    modalityRemote.addEventListener('change', loadRecruiters);
    modalityHybrid.addEventListener('change', loadRecruiters);
    modalityOnsite.addEventListener('change', loadRecruiters);
    companyTypeRadios.forEach(radio => radio.addEventListener('change', loadRecruiters));

    clearFilters.addEventListener('click', function() {
        selectedSectors = [];
        renderSectorChips();
        sectorInput.value = '';
        modalityRemote.checked = false;
        modalityHybrid.checked = false;
        modalityOnsite.checked = false;
        document.querySelector('input[name="company_type"][value=""]').checked = true;
        loadRecruiters();
    });

    async function loadRecruiters() {
        loading.classList.remove('hidden');
        recruiterGrid.innerHTML = '';
        noResults.classList.add('hidden');

        try {
            let url = recruiterWallApiUrl + '?';

            if (selectedSectors.length > 0) {
                selectedSectors.forEach(s => {
                    url += 'sector[]=' + s.slug + '&';
                });
            }

            const modalities = getSelectedModalities();
            if (modalities.length > 0) {
                modalities.forEach(m => {
                    url += 'modality[]=' + m + '&';
                });
            }

            const companyType = getSelectedCompanyType();
            if (companyType) {
                url += 'company_type=' + companyType + '&';
            }

            url = url.replace(/[&?]$/, '');

            const response = await fetch(url);
            const data = await response.json();

            loading.classList.add('hidden');

            if (data.profiles && data.profiles.length > 0) {
                renderRecruiters(data.profiles);
            } else {
                noResults.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error loading recruiters:', error);
            loading.classList.add('hidden');
            noResults.classList.remove('hidden');
        }
    }

    function renderRecruiters(profiles) {
        recruiterGrid.innerHTML = '';

        profiles.forEach(profile => {
            const card = createRecruiterCard(profile);
            recruiterGrid.appendChild(card);
        });
    }

    function createRecruiterCard(profile) {
        const card = document.createElement('div');
        card.className = 'bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300';

        const logoUrl = profile.company_logo || '';
        const companyName = escapeHtml(profile.company_name);
        const sector = profile.sector || '';
        const companyType = profile.company_type || '';
        const workModality = profile.work_modality || '';
        const description = profile.company_description && profile.company_description.length > 100
            ? escapeHtml(profile.company_description.substring(0, 100)) + '...'
            : escapeHtml(profile.company_description) || 'Sin descripcion';

        const tagsHtml = [];
        if (sector) tagsHtml.push('<span class="bg-indigo-100 dark:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(sector) + '</span>');
        if (companyType) tagsHtml.push('<span class="bg-purple-100 dark:bg-purple-900/50 text-purple-800 dark:text-purple-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(companyType) + '</span>');
        if (workModality) tagsHtml.push('<span class="bg-blue-100 dark:bg-blue-900/50 text-blue-800 dark:text-blue-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(workModality) + '</span>');

        const safeProfileUrl = '/empresa/' + (parseInt(profile.user_id) || 0) + '/';

        card.innerHTML =
            '<div class="aspect-square bg-gray-100 dark:bg-gray-700 relative">' +
                (logoUrl
                    ? '<img src="' + escapeHtml(logoUrl) + '" alt="' + companyName + '" class="w-full h-full object-cover">'
                    : '<div class="w-full h-full flex items-center justify-center"><svg class="w-16 h-16 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg></div>') +
            '</div>' +
            '<div class="p-4">' +
                '<h3 class="font-semibold text-gray-900 dark:text-white text-lg mb-1">' + companyName + '</h3>' +
                '<p class="text-gray-600 dark:text-gray-400 text-sm mb-3">' + description + '</p>' +
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
    loadRecruiters();
});
