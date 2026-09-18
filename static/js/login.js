function selectLoginRole(role) {
    const buttons = document.querySelectorAll('.oauth-btn');
    const githubBtn = document.getElementById('oauth-github');

    buttons.forEach(btn => {
        btn.classList.remove('ring-2', 'ring-indigo-500');
    });

    if (role === 'recruiter') {
        if (githubBtn) {
            githubBtn.closest('form').style.display = 'none';
        }
    } else {
        if (githubBtn) {
            githubBtn.closest('form').style.display = 'block';
        }
    }

    document.getElementById('login-role').value = role;
}
