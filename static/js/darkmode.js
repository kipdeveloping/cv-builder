document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;

    function isDark() {
        return html.classList.contains('dark');
    }

    function syncIcons() {
        const sunIcon = document.getElementById('icon-sun');
        const moonIcon = document.getElementById('icon-moon');
        if (sunIcon) sunIcon.classList.toggle('hidden', isDark());
        if (moonIcon) moonIcon.classList.toggle('hidden', !isDark());
    }

    function setTheme(theme, persist) {
        if (theme === 'dark') {
            html.classList.add('dark');
        } else {
            html.classList.remove('dark');
        }
        if (persist) localStorage.setItem('talentstack_theme', theme);
        syncIcons();
    }

    var saved = localStorage.getItem('talentstack_theme');
    if (saved !== 'dark' && saved !== 'light') {
        var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        setTheme(prefersDark ? 'dark' : 'light', false);
    }

    syncIcons();

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            setTheme(isDark() ? 'light' : 'dark', true);
        });
    }
});
