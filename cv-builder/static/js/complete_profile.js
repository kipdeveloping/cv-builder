document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('complete-profile-form');
    const titleInput = document.getElementById('id_title');
    const sectorHidden = document.getElementById('id_sector');
    const errorBox = document.getElementById('profile-error');
    const requiredMsg = document.querySelector('[data-msg="required"]');

    document.querySelectorAll('.sector-pill').forEach(function(pill) {
        pill.addEventListener('click', function() {
            document.querySelectorAll('.sector-pill').forEach(function(p) {
                p.classList.remove('bg-indigo-600', 'text-white');
                p.classList.add('bg-gray-200', 'text-gray-700', 'hover:bg-gray-300',
                    'dark:bg-gray-700', 'dark:text-gray-300', 'dark:hover:bg-gray-600');
            });
            pill.classList.remove('bg-gray-200', 'text-gray-700', 'hover:bg-gray-300',
                'dark:bg-gray-700', 'dark:text-gray-300', 'dark:hover:bg-gray-600');
            pill.classList.add('bg-indigo-600', 'text-white');
            sectorHidden.value = pill.dataset.id;
        });
    });
    if (sectorHidden && sectorHidden.value) {
        const selected = document.querySelector('.sector-pill[data-id="' + sectorHidden.value + '"]');
        if (selected) {
            selected.click();
        }
    }

    form.addEventListener('submit', function(e) {
        const hasSector = !!(sectorHidden && sectorHidden.value);
        const hasTitle = !!(titleInput && titleInput.value.trim());
        if (!hasSector && !hasTitle) {
            e.preventDefault();
            const msg = requiredMsg ? requiredMsg.textContent : 'Debes seleccionar al menos un campo.';
            errorBox.textContent = msg;
            errorBox.classList.remove('hidden');
            titleInput.focus();
        }
    });
});