(function() {
    function initTheme() {
        const themeToggle = document.getElementById('theme-toggle');
        const html = document.documentElement;

        function isDark() {
            return html.classList.contains('dark');
        }

        function syncIcons() {
            const sunIcon = document.getElementById('icon-sun');
            const moonIcon = document.getElementById('icon-moon');
            const dark = isDark();
            if (sunIcon) sunIcon.classList.toggle('hidden', dark);
            if (moonIcon) moonIcon.classList.toggle('hidden', !dark);
        }

        function setTheme(theme, persist) {
            if (theme === 'dark') {
                html.classList.add('dark');
            } else {
                html.classList.remove('dark');
            }
            if (persist) {
                try {
                    localStorage.setItem('talentstack_theme', theme);
                    localStorage.removeItem('cvbuilder_theme');
                } catch (e) {}
            }
            syncIcons();
        }

        // Read stored preference or system preference
        var saved = null;
        try {
            saved = localStorage.getItem('talentstack_theme') || localStorage.getItem('cvbuilder_theme');
        } catch (e) {}

        if (saved === 'dark' || saved === 'light') {
            setTheme(saved, false);
        } else {
            var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            setTheme(prefersDark ? 'dark' : 'light', false);
        }

        if (themeToggle) {
            themeToggle.onclick = function(e) {
                e.preventDefault();
                setTheme(isDark() ? 'light' : 'dark', true);
            };
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
    } else {
        initTheme();
    }
})();
