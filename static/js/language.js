document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('language-btn');
    const menu = document.getElementById('language-menu');
    if (!btn || !menu) return;

    btn.addEventListener('click', function(e) {
        e.stopPropagation();
        menu.classList.toggle('hidden');
    });

    document.addEventListener('click', function(e) {
        if (menu.classList.contains('hidden')) return;
        if (!menu.contains(e.target) && !btn.contains(e.target)) {
            menu.classList.add('hidden');
        }
    });

    menu.addEventListener('click', function(e) {
        e.stopPropagation();
    });
});