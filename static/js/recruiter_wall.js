document.addEventListener('DOMContentLoaded', function() {
    const recruiterGrid = document.getElementById('recruiter-grid');
    const loading = document.getElementById('loading');
    const noResults = document.getElementById('no-results');
    const countBadge = document.getElementById('results-count-badge');
    const sectorInput = document.getElementById('sector-input');
    const sectorChips = document.getElementById('sector-chips');
    const sectorSuggestions = document.getElementById('sector-suggestions');
    const modalityRemote = document.getElementById('modality-remote');
    const modalityHybrid = document.getElementById('modality-hybrid');
    const modalityOnsite = document.getElementById('modality-onsite');
    const clearFilters = document.getElementById('clear-filters');
    const companyTypeRadios = document.querySelectorAll('input[name="company_type"]');

    const i18n = window.recruiterWallI18n || {
        all: 'Todos los tipos',
        loading: 'Buscando empresas y reclutadores...',
        noResults: 'No se encontraron empresas con estos filtros',
        showingCount: 'empresas encontradas',
        showingOne: 'empresa encontrada',
        noDescription: 'Sin descripción',
        viewCompany: 'Ver empresa y vacantes',
        directCompany: 'Empresa Directa',
        independentRecruiter: 'Reclutador Independiente',
        remote: 'Remoto',
        hybrid: 'Híbrido',
        onsite: 'Presencial'
    };

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
            chip.className = 'inline-flex items-center gap-1.5 px-3 py-1 rounded-xl text-xs font-semibold bg-indigo-50 dark:bg-indigo-950/70 text-indigo-700 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800 shadow-xs';
            chip.innerHTML = escapeHtml(sector.name) +
                '<button type="button" class="ml-1 hover:text-red-500 font-bold" data-slug="' + sector.slug + '">' +
                '&times;</button>';
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
        }, 200);
    });

    function showSuggestions(suggestions) {
        sectorSuggestions.innerHTML = '';
        if (suggestions.length === 0) {
            sectorSuggestions.classList.add('hidden');
            return;
        }

        suggestions.forEach(sector => {
            const item = document.createElement('div');
            item.className = 'px-4 py-2 hover:bg-indigo-50 dark:hover:bg-gray-650 cursor-pointer text-xs font-medium text-gray-800 dark:text-gray-200 border-b border-gray-100 dark:border-gray-650 last:border-0';
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
        if (modalityRemote && modalityRemote.checked) modalities.push('remote');
        if (modalityHybrid && modalityHybrid.checked) modalities.push('hybrid');
        if (modalityOnsite && modalityOnsite.checked) modalities.push('onsite');
        return modalities;
    }

    function getSelectedCompanyType() {
        const selected = document.querySelector('input[name="company_type"]:checked');
        return selected ? selected.value : '';
    }

    if (modalityRemote) modalityRemote.addEventListener('change', loadRecruiters);
    if (modalityHybrid) modalityHybrid.addEventListener('change', loadRecruiters);
    if (modalityOnsite) modalityOnsite.addEventListener('change', loadRecruiters);

    companyTypeRadios.forEach(radio => {
        radio.addEventListener('change', loadRecruiters);
    });

    clearFilters.addEventListener('click', function() {
        selectedSectors = [];
        renderSectorChips();
        sectorInput.value = '';
        if (modalityRemote) modalityRemote.checked = false;
        if (modalityHybrid) modalityHybrid.checked = false;
        if (modalityOnsite) modalityOnsite.checked = false;
        const allRadio = document.querySelector('input[name="company_type"][value=""]');
        if (allRadio) allRadio.checked = true;
        loadRecruiters();
    });

    function updateCountBadge(count) {
        if (!countBadge) return;
        if (count === 1) {
            countBadge.textContent = '1 ' + (i18n.showingOne || 'empresa encontrada');
        } else {
            countBadge.textContent = count + ' ' + (i18n.showingCount || 'empresas encontradas');
        }
    }

    async function loadRecruiters() {
        loading.classList.remove('hidden');
        recruiterGrid.innerHTML = '';
        noResults.classList.add('hidden');

        try {
            let url = recruiterWallApiUrl + '?';

            if (selectedSectors.length > 0) {
                selectedSectors.forEach(s => {
                    url += 'sector[]=' + encodeURIComponent(s.slug) + '&';
                });
            }

            const modalities = getSelectedModalities();
            if (modalities.length > 0) {
                modalities.forEach(m => {
                    url += 'modality[]=' + encodeURIComponent(m) + '&';
                });
            }

            const companyType = getSelectedCompanyType();
            if (companyType) {
                url += 'company_type=' + encodeURIComponent(companyType) + '&';
            }

            url = url.replace(/[&?]$/, '');

            const response = await fetch(url);
            const data = await response.json();

            loading.classList.add('hidden');

            if (data.profiles && data.profiles.length > 0) {
                updateCountBadge(data.profiles.length);
                renderRecruiters(data.profiles);
            } else {
                updateCountBadge(0);
                noResults.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error loading recruiters:', error);
            loading.classList.add('hidden');
            noResults.classList.remove('hidden');
            updateCountBadge(0);
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
        card.className = 'group bg-white dark:bg-gray-800 rounded-2xl sm:rounded-3xl border border-gray-200/80 dark:border-gray-700/80 shadow-md hover:shadow-2xl hover:border-indigo-500/40 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between overflow-hidden cursor-pointer';

        const logoUrl = profile.company_logo || '';
        const companyName = escapeHtml(profile.company_name);
        const sector = escapeHtml(profile.sector || '');
        const companyType = profile.company_type || '';
        const companyTypeDisplay = escapeHtml(profile.company_type_display || (companyType === 'particular' ? i18n.independentRecruiter : i18n.directCompany));
        const modalityDisplay = escapeHtml(profile.work_modality_display || profile.work_modality || '');
        const description = profile.company_description && profile.company_description.length > 100
            ? escapeHtml(profile.company_description.substring(0, 100)) + '...'
            : (escapeHtml(profile.company_description) || i18n.noDescription);

        let logoHtml = '';
        if (logoUrl) {
            logoHtml = '<img src="' + escapeHtml(logoUrl) + '" alt="' + companyName + '" class="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl object-cover border border-gray-200 dark:border-gray-700 shadow-sm group-hover:scale-105 transition-transform duration-300">';
        } else {
            logoHtml = '<div class="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-tr from-purple-600 via-indigo-600 to-blue-500 p-0.5 shadow-sm group-hover:scale-105 transition-transform duration-300">' +
                '<div class="w-full h-full rounded-2xl bg-white dark:bg-gray-800 flex items-center justify-center text-purple-600 dark:text-purple-400">' +
                    '<svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>' +
                '</div></div>';
        }

        const safeProfileUrl = '/empresa/' + (parseInt(profile.user_id) || 0) + '/';

        card.innerHTML =
            '<div class="p-5 sm:p-6 space-y-4">' +
                '<div class="flex items-start gap-3.5">' +
                    logoHtml +
                    '<div class="min-w-0 flex-1">' +
                        '<h3 class="font-bold text-gray-900 dark:text-white text-base group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors truncate">' + companyName + '</h3>' +
                        '<div class="flex flex-wrap items-center gap-1.5 mt-1.5">' +
                            (companyType ? '<span class="px-2 py-0.5 rounded-md text-[10px] font-bold bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300 border border-indigo-200/60 dark:border-indigo-800/60">' + companyTypeDisplay + '</span>' : '') +
                            (modalityDisplay ? '<span class="px-2 py-0.5 rounded-md text-[10px] font-medium bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300">📍 ' + modalityDisplay + '</span>' : '') +
                        '</div>' +
                    </div>' +
                '</div>' +
                (sector ? '<div class="text-[11px] font-semibold text-purple-600 dark:text-purple-400">🏷️ ' + sector + '</div>' : '') +
                '<p class="text-xs text-gray-600 dark:text-gray-300 line-clamp-3 leading-relaxed">' + description + '</p>' +
            '</div>' +
            '<div class="px-5 sm:px-6 py-3 bg-gray-50/80 dark:bg-gray-750/70 border-t border-gray-100 dark:border-gray-700/70 flex items-center justify-between text-xs font-bold text-indigo-600 dark:text-indigo-400">' +
                '<span>' + escapeHtml(i18n.viewCompany) + '</span>' +
                '<svg class="w-4 h-4 transform group-hover:translate-x-1.5 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">' +
                    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>' +
                '</svg>' +
            '</div>';

        card.addEventListener('click', function() {
            window.location.href = safeProfileUrl;
        });

        return card;
    }

    loadSectors();
    loadRecruiters();
});
