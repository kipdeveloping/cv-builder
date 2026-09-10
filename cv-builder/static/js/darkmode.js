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

    function setTheme(theme) {
        if (theme === 'dark') {
            html.classList.add('dark');
        } else {
            html.classList.remove('dark');
        }
        localStorage.setItem('cvbuilder_theme', theme);
        syncIcons();
    }

    syncIcons();

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            setTheme(isDark() ? 'light' : 'dark');
        });
    }
});