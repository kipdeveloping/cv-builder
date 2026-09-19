document.addEventListener('DOMContentLoaded', function() {
    const profileGrid = document.getElementById('cv-grid');
    const loading = document.getElementById('loading');
    const noResults = document.getElementById('no-results');
    const countBadge = document.getElementById('results-count-badge');
    const sectorFilter = document.getElementById('sector-filter');
    const rolFilter = document.getElementById('rol-filter');
    const especialidadFilter = document.getElementById('especialidad-filter');
    const seniorityFilter = document.getElementById('seniority-filter');
    const locationFilter = document.getElementById('location-filter');
    const mustTagsInput = document.getElementById('must-tags-input');
    const mustTagsChips = document.getElementById('must-tags-chips');
    const mustTagsSuggestions = document.getElementById('must-tags-suggestions');
    const niceTagsInput = document.getElementById('nice-tags-input');
    const niceTagsChips = document.getElementById('nice-tags-chips');
    const niceTagsSuggestions = document.getElementById('nice-tags-suggestions');
    const toggleTags = document.getElementById('toggle-tags');
    const tagsSection = document.getElementById('tags-section');
    const tagsArrow = document.getElementById('tags-arrow');
    const toggleAdvanced = document.getElementById('toggle-advanced');
    const advancedSection = document.getElementById('advanced-section');
    const advancedArrow = document.getElementById('advanced-arrow');
    const clearFilters = document.getElementById('clear-filters');

    const i18n = window.wallI18n || {
        allSectors: 'Todos los sectores',
        allRoles: 'Todos los roles',
        allSpecialties: 'Todas las especialidades',
        loading: 'Buscando profesionales...',
        noResults: 'No se encontraron perfiles con estos filtros',
        showingCount: 'profesionales encontrados',
        showingOne: 'profesional encontrado',
        noDescription: 'Sin descripción',
        viewProfile: 'Ver perfil interactivo',
        availableStatus: 'Disponible',
        openStatus: 'Abierto a ofertas',
        match: 'Match',
        moreTags: 'más'
    };

    let hierarchy = [];
    let allTags = [];
    let selectedMustTags = [];
    let selectedNiceTags = [];
    let searchTimeout = null;

    function escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    if (toggleTags && tagsSection && tagsArrow) {
        toggleTags.addEventListener('click', function() {
            tagsSection.classList.toggle('hidden');
            tagsArrow.classList.toggle('rotate-180');
        });
    }

    if (toggleAdvanced && advancedSection && advancedArrow) {
        toggleAdvanced.addEventListener('click', function() {
            advancedSection.classList.toggle('hidden');
            advancedArrow.classList.toggle('rotate-180');
        });
    }

    async function loadHierarchy() {
        try {
            const response = await fetch(tagHierarchyUrl);
            const data = await response.json();
            hierarchy = data.hierarchy || [];
            populateSectorDropdown();

            // Check if initial URL param specifies sector
            const urlParams = new URLSearchParams(window.location.search);
            const initialSector = urlParams.get('sector');
            if (initialSector) {
                sectorFilter.value = initialSector;
                populateRoleDropdown(initialSector);
                loadProfiles();
            }
        } catch (error) {
            console.error('Error loading hierarchy:', error);
        }
    }

    function populateSectorDropdown() {
        sectorFilter.innerHTML = '<option value="" class="bg-white dark:bg-gray-700 text-gray-900 dark:text-white">' + escapeHtml(i18n.allSectors) + '</option>';
        hierarchy.forEach(sector => {
            const option = document.createElement('option');
            option.value = sector.slug;
            option.textContent = sector.name;
            option.className = 'bg-white dark:bg-gray-700 text-gray-900 dark:text-white';
            sectorFilter.appendChild(option);
        });
    }

    function populateRoleDropdown(sectorSlug) {
        rolFilter.innerHTML = '<option value="" class="bg-white dark:bg-gray-700 text-gray-900 dark:text-white">' + escapeHtml(i18n.allRoles) + '</option>';
        especialidadFilter.innerHTML = '<option value="" class="bg-white dark:bg-gray-700 text-gray-900 dark:text-white">' + escapeHtml(i18n.allSpecialties) + '</option>';

        if (!sectorSlug) return;

        const sector = hierarchy.find(s => s.slug === sectorSlug);
        if (!sector) return;

        sector.roles.forEach(role => {
            const option = document.createElement('option');
            option.value = role.slug;
            option.textContent = role.name;
            option.className = 'bg-white dark:bg-gray-700 text-gray-900 dark:text-white';
            rolFilter.appendChild(option);
        });
    }

    function populateEspecialidadDropdown(sectorSlug, rolSlug) {
        especialidadFilter.innerHTML = '<option value="" class="bg-white dark:bg-gray-700 text-gray-900 dark:text-white">' + escapeHtml(i18n.allSpecialties) + '</option>';

        if (!sectorSlug || !rolSlug) return;

        const sector = hierarchy.find(s => s.slug === sectorSlug);
        if (!sector) return;

        const role = sector.roles.find(r => r.slug === rolSlug);
        if (!role) return;

        role.especialidades.forEach(esp => {
            const option = document.createElement('option');
            option.value = esp.slug;
            option.textContent = esp.name;
            option.className = 'bg-white dark:bg-gray-700 text-gray-900 dark:text-white';
            especialidadFilter.appendChild(option);
        });
    }

    sectorFilter.addEventListener('change', function() {
        populateRoleDropdown(this.value);
        loadProfiles();
    });

    rolFilter.addEventListener('change', function() {
        populateEspecialidadDropdown(sectorFilter.value, this.value);
        loadProfiles();
    });

    especialidadFilter.addEventListener('change', function() {
        loadProfiles();
    });

    seniorityFilter.addEventListener('change', function() {
        loadProfiles();
    });

    locationFilter.addEventListener('change', function() {
        loadProfiles();
    });

    async function loadAllTags() {
        try {
            const response = await fetch(allTagsUrl);
            const data = await response.json();
            allTags = data.tags || [];
        } catch (error) {
            console.error('Error loading tags:', error);
        }
    }

    function searchTags(query) {
        if (!query) return [];
        const lower = query.toLowerCase();
        return allTags.filter(tag =>
            tag.name.toLowerCase().includes(lower) ||
            tag.slug.toLowerCase().includes(lower)
        ).slice(0, 10);
    }

    function renderTagChips(container, tags, type) {
        container.innerHTML = '';
        const chipColor = type === 'must'
            ? 'bg-indigo-100 dark:bg-indigo-900/60 text-indigo-800 dark:text-indigo-200 border-indigo-200 dark:border-indigo-800'
            : 'bg-purple-100 dark:bg-purple-900/60 text-purple-800 dark:text-purple-200 border-purple-200 dark:border-purple-800';

        tags.forEach(tag => {
            const chip = document.createElement('span');
            chip.className = 'inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-semibold border shadow-xs ' + chipColor;
            chip.innerHTML = escapeHtml(tag.name) +
                '<button type="button" class="ml-1 hover:text-red-500 font-bold" data-slug="' + tag.slug + '">' +
                '&times;</button>';
            container.appendChild(chip);
        });
    }

    function showSuggestions(input, container, suggestions, type) {
        container.innerHTML = '';
        if (suggestions.length === 0) {
            container.classList.add('hidden');
            return;
        }

        suggestions.forEach(tag => {
            const item = document.createElement('div');
            item.className = 'px-3 py-2 hover:bg-indigo-50 dark:hover:bg-gray-650 cursor-pointer text-xs font-medium text-gray-800 dark:text-gray-200 flex items-center justify-between border-b border-gray-100 dark:border-gray-650 last:border-0';
            item.innerHTML = '<span>' + escapeHtml(tag.name) + '</span>' +
                (tag.especialidad ? '<span class="text-[10px] text-gray-400">' + escapeHtml(tag.especialidad) + '</span>' : '');

            item.addEventListener('click', function() {
                addTag(tag, type);
                container.classList.add('hidden');
                input.value = '';
            });
            container.appendChild(item);
        });

        container.classList.remove('hidden');
    }

    mustTagsInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const suggestions = searchTags(this.value);
            showSuggestions(this, mustTagsSuggestions, suggestions, 'must');
        }, 200);
    });

    niceTagsInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const suggestions = searchTags(this.value);
            showSuggestions(this, niceTagsSuggestions, suggestions, 'nice');
        }, 200);
    });

    function addTag(tag, type) {
        const tags = type === 'must' ? selectedMustTags : selectedNiceTags;
        if (tags.find(t => t.slug === tag.slug)) return;

        tags.push(tag);
        const chips = type === 'must' ? mustTagsChips : niceTagsChips;
        renderTagChips(chips, tags, type);
        loadProfiles();
    }

    function removeTag(slug, type) {
        if (type === 'must') {
            selectedMustTags = selectedMustTags.filter(t => t.slug !== slug);
            renderTagChips(mustTagsChips, selectedMustTags, 'must');
        } else {
            selectedNiceTags = selectedNiceTags.filter(t => t.slug !== slug);
            renderTagChips(niceTagsChips, selectedNiceTags, 'nice');
        }
        loadProfiles();
    }

    mustTagsChips.addEventListener('click', function(e) {
        const btn = e.target.closest('button[data-slug]');
        if (btn) removeTag(btn.dataset.slug, 'must');
    });

    niceTagsChips.addEventListener('click', function(e) {
        const btn = e.target.closest('button[data-slug]');
        if (btn) removeTag(btn.dataset.slug, 'nice');
    });

    clearFilters.addEventListener('click', function() {
        sectorFilter.value = '';
        rolFilter.innerHTML = '<option value="">' + escapeHtml(i18n.allRoles) + '</option>';
        especialidadFilter.innerHTML = '<option value="">' + escapeHtml(i18n.allSpecialties) + '</option>';
        seniorityFilter.value = '';
        locationFilter.value = '';
        selectedMustTags = [];
        selectedNiceTags = [];
        renderTagChips(mustTagsChips, [], 'must');
        renderTagChips(niceTagsChips, [], 'nice');
        loadProfiles();
    });

    document.addEventListener('click', function(e) {
        if (!mustTagsInput.contains(e.target) && !mustTagsSuggestions.contains(e.target)) {
            mustTagsSuggestions.classList.add('hidden');
        }
        if (!niceTagsInput.contains(e.target) && !niceTagsSuggestions.contains(e.target)) {
            niceTagsSuggestions.classList.add('hidden');
        }
    });

    function updateCountBadge(count) {
        if (!countBadge) return;
        if (count === 1) {
            countBadge.textContent = '1 ' + (i18n.showingOne || 'profesional encontrado');
        } else {
            countBadge.textContent = count + ' ' + (i18n.showingCount || 'profesionales encontrados');
        }
    }

    async function loadProfiles() {
        loading.classList.remove('hidden');
        profileGrid.innerHTML = '';
        noResults.classList.add('hidden');

        try {
            let url = wallApiUrl + '?';

            if (sectorFilter.value) url += 'sector=' + encodeURIComponent(sectorFilter.value) + '&';
            if (rolFilter.value) url += 'rol=' + encodeURIComponent(rolFilter.value) + '&';
            if (especialidadFilter.value) url += 'especialidad=' + encodeURIComponent(especialidadFilter.value) + '&';
            if (seniorityFilter.value) url += 'seniority=' + encodeURIComponent(seniorityFilter.value) + '&';
            if (locationFilter.value) url += 'location=' + encodeURIComponent(locationFilter.value) + '&';
            if (selectedMustTags.length > 0) url += 'tags_must=' + selectedMustTags.map(t => encodeURIComponent(t.slug)).join(',') + '&';
            if (selectedNiceTags.length > 0) url += 'tags_nice=' + selectedNiceTags.map(t => encodeURIComponent(t.slug)).join(',') + '&';

            url = url.replace(/[&?]$/, '');

            const response = await fetch(url);
            const data = await response.json();

            loading.classList.add('hidden');

            if (data.profiles && data.profiles.length > 0) {
                updateCountBadge(data.profiles.length);
                renderProfiles(data.profiles);
            } else {
                updateCountBadge(0);
                noResults.classList.remove('hidden');
            }
        } catch (error) {
            console.error('Error loading profiles:', error);
            loading.classList.add('hidden');
            noResults.classList.remove('hidden');
            updateCountBadge(0);
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
        card.className = 'group bg-white dark:bg-gray-800 rounded-2xl sm:rounded-3xl border border-gray-200/80 dark:border-gray-700/80 shadow-md hover:shadow-2xl hover:border-indigo-500/40 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between overflow-hidden cursor-pointer';

        const safeName = escapeHtml(profile.name);
        const headline = escapeHtml(profile.headline || '');
        const photoUrl = profile.photo || '';
        const score = profile.score || 0;
        const seniority = escapeHtml(profile.seniority_display || profile.seniority || '');
        const location = escapeHtml(profile.location_display || profile.location || '');
        const sector = escapeHtml(profile.sector || '');
        const rol = escapeHtml(profile.rol || '');
        const especialidad = escapeHtml(profile.especialidad || '');
        const searchStatus = profile.search_status || 'active';
        const statusText = escapeHtml(profile.search_status_display || i18n.availableStatus);
        const safeBio = profile.bio && profile.bio.length > 90
            ? escapeHtml(profile.bio.substring(0, 90)) + '...'
            : (escapeHtml(profile.bio) || i18n.noDescription);

        // Top Status & Score badges
        let statusBadge = '';
        if (searchStatus === 'active') {
            statusBadge = '<span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-100 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 border border-emerald-200/60 dark:border-emerald-800/60">' +
                '<span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>' +
                statusText + '</span>';
        } else {
            statusBadge = '<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300">' +
                statusText + '</span>';
        }

        let scoreBadge = '';
        if (score > 0) {
            scoreBadge = '<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-extrabold bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-xs">' +
                '⚡ ' + score + '%</span>';
        }

        // Avatar
        let avatarHtml = '';
        if (photoUrl) {
            avatarHtml = '<img src="' + escapeHtml(photoUrl) + '" alt="' + safeName + '" class="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl object-cover border-2 border-white dark:border-gray-700 shadow-md group-hover:scale-105 transition-transform duration-300">';
        } else {
            const initials = safeName.split(' ').map(n => n[0]).slice(0, 2).join('').toUpperCase() || 'CV';
            avatarHtml = '<div class="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-tr from-indigo-600 via-purple-600 to-pink-500 p-0.5 shadow-md group-hover:scale-105 transition-transform duration-300">' +
                '<div class="w-full h-full rounded-2xl bg-white dark:bg-gray-800 flex items-center justify-center font-bold text-base text-indigo-600 dark:text-indigo-400">' +
                initials + '</div></div>';
        }

        // Seniority Style
        let seniorityClass = 'bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300 border-indigo-200/60 dark:border-indigo-800/60';
        if (profile.seniority === 'junior') {
            seniorityClass = 'bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 border-emerald-200/60 dark:border-emerald-800/60';
        } else if (profile.seniority === 'lead') {
            seniorityClass = 'bg-purple-50 dark:bg-purple-950/60 text-purple-700 dark:text-purple-300 border-purple-200/60 dark:border-purple-800/60';
        }

        // Taxonomy
        const taxParts = [];
        if (sector) taxParts.push(sector);
        if (rol) taxParts.push(rol);
        if (especialidad) taxParts.push(especialidad);
        let taxonomyHtml = '';
        if (taxParts.length > 0) {
            taxonomyHtml = '<div class="text-[11px] text-gray-500 dark:text-gray-400 font-medium line-clamp-1 mb-2">' +
                taxParts.map(p => '<span>' + p + '</span>').join(' <span class="text-gray-400 dark:text-gray-600">&bull;</span> ') +
                '</div>';
        }

        // Tags
        let tagsHtml = '';
        if (profile.tag_items && profile.tag_items.length > 0) {
            const visible = profile.tag_items.slice(0, 4);
            visible.forEach(t => {
                tagsHtml += '<span class="px-2 py-0.5 rounded-md text-[11px] font-semibold bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 group-hover:bg-indigo-50 dark:group-hover:bg-indigo-950/50 group-hover:text-indigo-600 dark:group-hover:text-indigo-300 transition-colors">' + escapeHtml(t.name) + '</span>';
            });
            if (profile.tag_items.length > 4) {
                const moreCount = profile.tag_items.length - 4;
                tagsHtml += '<span class="px-2 py-0.5 rounded-md text-[11px] font-semibold bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300 border border-indigo-200/50 dark:border-indigo-800/50">+' + moreCount + ' ' + escapeHtml(i18n.moreTags) + '</span>';
            }
        }

        const safeProfileUrl = '/candidato/' + (parseInt(profile.user_id) || 0) + '/';

        card.innerHTML =
            '<div class="p-5 sm:p-6 space-y-4">' +
                '<div class="flex items-center justify-between gap-2">' +
                    statusBadge + scoreBadge +
                '</div>' +
                '<div class="flex items-start gap-3.5">' +
                    avatarHtml +
                    '<div class="min-w-0 flex-1">' +
                        '<h3 class="font-bold text-gray-900 dark:text-white text-base group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors truncate">' + safeName + '</h3>' +
                        (headline ? '<p class="text-xs font-semibold text-indigo-600 dark:text-indigo-400 line-clamp-1 mt-0.5">' + headline + '</p>' : '') +
                        '<div class="flex flex-wrap items-center gap-1.5 mt-2">' +
                            (seniority ? '<span class="px-2 py-0.5 rounded-md text-[10px] font-bold border ' + seniorityClass + '">' + seniority + '</span>' : '') +
                            (location ? '<span class="px-2 py-0.5 rounded-md text-[10px] font-medium bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300">📍 ' + location + '</span>' : '') +
                        '</div>' +
                    </div>' +
                '</div>' +
                '<p class="text-xs text-gray-600 dark:text-gray-300 line-clamp-2 leading-relaxed">' + safeBio + '</p>' +
                taxonomyHtml +
                (tagsHtml ? '<div class="flex flex-wrap gap-1.5 pt-1">' + tagsHtml + '</div>' : '') +
            '</div>' +
            '<div class="px-5 sm:px-6 py-3 bg-gray-50/80 dark:bg-gray-750/70 border-t border-gray-100 dark:border-gray-700/70 flex items-center justify-between text-xs font-bold text-indigo-600 dark:text-indigo-400">' +
                '<span>' + escapeHtml(i18n.viewProfile) + '</span>' +
                '<svg class="w-4 h-4 transform group-hover:translate-x-1.5 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">' +
                    '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path>' +
                '</svg>' +
            '</div>';

        card.addEventListener('click', function() {
            window.location.href = safeProfileUrl;
        });

        return card;
    }

    loadHierarchy();
    loadAllTags();
    loadProfiles();
});
