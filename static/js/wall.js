document.addEventListener('DOMContentLoaded', function() {
    const profileGrid = document.getElementById('cv-grid');
    const loading = document.getElementById('loading');
    const noResults = document.getElementById('no-results');
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

    toggleTags.addEventListener('click', function() {
        tagsSection.classList.toggle('hidden');
        tagsArrow.classList.toggle('rotate-180');
    });

    toggleAdvanced.addEventListener('click', function() {
        advancedSection.classList.toggle('hidden');
        advancedArrow.classList.toggle('rotate-180');
    });

    async function loadHierarchy() {
        try {
            const response = await fetch(tagHierarchyUrl);
            const data = await response.json();
            hierarchy = data.hierarchy || [];
            populateSectorDropdown();
        } catch (error) {
            console.error('Error loading hierarchy:', error);
        }
    }

    function populateSectorDropdown() {
        sectorFilter.innerHTML = '<option value="">Todos</option>';
        hierarchy.forEach(sector => {
            const option = document.createElement('option');
            option.value = sector.slug;
            option.textContent = sector.name;
            sectorFilter.appendChild(option);
        });
    }

    function populateRoleDropdown(sectorSlug) {
        rolFilter.innerHTML = '<option value="">Todos</option>';
        especialidadFilter.innerHTML = '<option value="">Todas</option>';

        if (!sectorSlug) return;

        const sector = hierarchy.find(s => s.slug === sectorSlug);
        if (!sector) return;

        sector.roles.forEach(role => {
            const option = document.createElement('option');
            option.value = role.slug;
            option.textContent = role.name;
            rolFilter.appendChild(option);
        });
    }

    function populateEspecialidadDropdown(sectorSlug, rolSlug) {
        especialidadFilter.innerHTML = '<option value="">Todas</option>';

        if (!sectorSlug || !rolSlug) return;

        const sector = hierarchy.find(s => s.slug === sectorSlug);
        if (!sector) return;

        const role = sector.roles.find(r => r.slug === rolSlug);
        if (!role) return;

        role.especialidades.forEach(esp => {
            const option = document.createElement('option');
            option.value = esp.slug;
            option.textContent = esp.name;
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
        tags.forEach(tag => {
            const chip = document.createElement('span');
            chip.className = 'inline-flex items-center gap-1 px-3 py-1 rounded-full text-sm font-semibold ' +
                (type === 'must' ? 'bg-indigo-100 dark:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200' :
                'bg-green-100 dark:bg-green-900/50 text-green-800 dark:text-green-200');
            chip.innerHTML = escapeHtml(tag.name) +
                '<button type="button" class="ml-1 hover:text-indigo-600 dark:hover:text-indigo-300" data-slug="' + tag.slug + '">' +
                '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">' +
                '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>' +
                '</svg></button>';
            container.appendChild(chip);
        });
    }

    mustTagsInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const suggestions = searchTags(this.value);
            showSuggestions(mustTagsSuggestions, suggestions, 'must');
        }, 300);
    });

    niceTagsInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const suggestions = searchTags(this.value);
            showSuggestions(niceTagsSuggestions, suggestions, 'nice');
        }, 300);
    });

    function showSuggestions(container, suggestions, type) {
        container.innerHTML = '';
        if (suggestions.length === 0) {
            container.classList.add('hidden');
            return;
        }

        suggestions.forEach(tag => {
            const item = document.createElement('div');
            item.className = 'px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 cursor-pointer text-sm text-gray-900 dark:text-white';
            item.textContent = tag.name + ' (' + tag.category + ')';
            item.addEventListener('click', function() {
                addTag(tag, type);
                container.classList.add('hidden');
                if (type === 'must') mustTagsInput.value = '';
                else niceTagsInput.value = '';
            });
            container.appendChild(item);
        });

        container.classList.remove('hidden');
    }

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
        rolFilter.innerHTML = '<option value="">Todos</option>';
        especialidadFilter.innerHTML = '<option value="">Todas</option>';
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

    async function loadProfiles() {
        loading.classList.remove('hidden');
        profileGrid.innerHTML = '';
        noResults.classList.add('hidden');

        try {
            let url = wallApiUrl + '?';

            if (sectorFilter.value) url += 'sector=' + sectorFilter.value + '&';
            if (rolFilter.value) url += 'rol=' + rolFilter.value + '&';
            if (especialidadFilter.value) url += 'especialidad=' + especialidadFilter.value + '&';
            if (seniorityFilter.value) url += 'seniority=' + seniorityFilter.value + '&';
            if (locationFilter.value) url += 'location=' + locationFilter.value + '&';
            if (selectedMustTags.length > 0) url += 'tags_must=' + selectedMustTags.map(t => t.slug).join(',') + '&';
            if (selectedNiceTags.length > 0) url += 'tags_nice=' + selectedNiceTags.map(t => t.slug).join(',') + '&';

            url = url.replace(/[&?]$/, '');

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
        const rol = profile.rol || '';
        const especialidad = profile.especialidad || '';
        const seniority = profile.seniority || '';
        const score = profile.score || 0;
        const truncatedBio = profile.bio && profile.bio.length > 80
            ? escapeHtml(profile.bio.substring(0, 80)) + '...'
            : escapeHtml(profile.bio) || 'Sin descripcion';

        const tagsHtml = [];
        if (sector) tagsHtml.push('<span class="bg-indigo-100 dark:bg-indigo-900/50 text-indigo-800 dark:text-indigo-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(sector) + '</span>');
        if (rol) tagsHtml.push('<span class="bg-purple-100 dark:bg-purple-900/50 text-purple-800 dark:text-purple-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(rol) + '</span>');
        if (especialidad) tagsHtml.push('<span class="bg-blue-100 dark:bg-blue-900/50 text-blue-800 dark:text-blue-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(especialidad) + '</span>');
        if (seniority) tagsHtml.push('<span class="bg-yellow-100 dark:bg-yellow-900/50 text-yellow-800 dark:text-yellow-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(seniority) + '</span>');
        if (location) tagsHtml.push('<span class="bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-xs px-2 py-1 rounded-full">' + escapeHtml(location) + '</span>');

        const safeProfileUrl = '/candidato/' + (parseInt(profile.user_id) || 0) + '/';

        card.innerHTML = 
            '<div class="aspect-square bg-gray-100 dark:bg-gray-700 relative">' +
                '<img src="' + escapeHtml(photoUrl) + '" alt="' + safeName + '"' +
                    'class="w-full h-full object-cover">' +
                (score > 0 ? '<span class="absolute top-2 right-2 bg-indigo-600 text-white text-xs font-bold px-2 py-1 rounded-full">' + score + '%</span>' : '') +
            '</div>' +
            '<div class="p-4">' +
                '<h3 class="font-semibold text-gray-900 dark:text-white text-lg mb-1">' + safeName + '</h3>' +
                (headline ? '<p class="text-gray-600 dark:text-gray-400 text-sm mb-1">' + escapeHtml(headline) + '</p>' : '') +
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

    loadHierarchy();
    loadAllTags();
    loadProfiles();
});
