document.addEventListener('DOMContentLoaded', () => {
    let currentStep = 1;
    const totalSteps = 4;
    let selectedRole = 'candidate';

    const form = document.getElementById('wizard-form');
    const btnNext = document.getElementById('btn-next');
    const btnPrev = document.getElementById('btn-prev');
    const btnSubmit = document.getElementById('btn-submit');
    const subtitle = document.getElementById('step-subtitle');
    const steps = document.querySelectorAll('.step');
    const dots = [
        document.getElementById('dot-1'),
        document.getElementById('dot-2'),
        document.getElementById('dot-3'),
        document.getElementById('dot-4')
    ];
    const roleInput = document.getElementById('id_role');
    const githubBtn = document.getElementById('oauth-github');
    const recruiterHints = document.querySelectorAll('.recruiter-hint');

    function getSubtitles() {
        return {
            1: t('Paso 1 de 4 \u2014 \u00bfQu\u00e9 buscas?'),
            2: t('Paso 2 de 4 \u2014 Datos de acceso'),
            3: t('Paso 3 de 4 \u2014 Datos personales'),
            4: t('Paso 4 de 4 \u2014 Informaci\u00f3n espec\u00edfica')
        };
    }

    function showError(message) {
        let errorDiv = document.getElementById('wizard-error');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.id = 'wizard-error';
            errorDiv.className = 'bg-red-50 dark:bg-red-900/50 border border-red-200 dark:border-red-700 text-red-700 dark:text-red-200 px-4 py-3 rounded-lg mb-4';
            form.insertBefore(errorDiv, form.firstChild);
        }
        errorDiv.textContent = message;
        errorDiv.classList.remove('hidden');
    }

    function clearError() {
        const errorDiv = document.getElementById('wizard-error');
        if (errorDiv) errorDiv.classList.add('hidden');
    }

    function validateStep(step) {
        clearError();
        if (step === 2) {
            const email = document.getElementById('id_email');
            const password1 = document.getElementById('id_password1');
            const password2 = document.getElementById('id_password2');
            if (!email.value.trim()) {
                showError(t('El email es obligatorio.'));
                return false;
            }
            if (!password1.value) {
                showError(t('La contrase\u00f1a es obligatoria.'));
                return false;
            }
            if (!password2.value) {
                showError(t('Debes confirmar la contrase\u00f1a.'));
                return false;
            }
            if (password1.value !== password2.value) {
                showError(t('Las contrase\u00f1as no coinciden.'));
                return false;
            }
        }
        if (step === 3) {
            const firstName = document.getElementById('id_first_name');
            const lastName = document.getElementById('id_last_name');
            if (selectedRole === 'recruiter') {
                const companyName = document.getElementById('id_company_name');
                if (!firstName.value.trim() || !lastName.value.trim()) {
                    showError(t('Nombre y apellido son obligatorios.'));
                    return false;
                }
                if (!companyName.value.trim()) {
                    showError(t('El nombre de la empresa es obligatorio.'));
                    return false;
                }
            } else {
                if (!firstName.value.trim() || !lastName.value.trim()) {
                    showError(t('Nombre y apellido son obligatorios.'));
                    return false;
                }
            }
        }
        return true;
    }

    window.selectRole = function(role) {
        selectedRole = role;
        roleInput.value = role;

        document.querySelectorAll('.role-btn').forEach(btn => {
            btn.classList.remove('selected');
        });
        document.getElementById('role-' + role).classList.add('selected');

        recruiterHints.forEach(hint => {
            hint.classList.toggle('hidden', role !== 'recruiter');
        });

        if (githubBtn) {
            githubBtn.classList.toggle('hidden', role === 'recruiter');
        }

        document.querySelectorAll('.candidate-fields').forEach(el => {
            el.classList.toggle('hidden', role !== 'candidate');
        });
        document.querySelectorAll('.recruiter-fields').forEach(el => {
            el.classList.toggle('hidden', role !== 'recruiter');
        });
    };

    function updateUI() {
        const subtitles = getSubtitles();
        steps.forEach((s, i) => {
            s.classList.toggle('hidden', i + 1 !== currentStep);
        });
        dots.forEach((d, i) => {
            if (d) {
                d.classList.toggle('bg-indigo-600', i + 1 === currentStep);
                d.classList.toggle('bg-gray-300', i + 1 !== currentStep);
                d.classList.toggle('dark:bg-gray-600', i + 1 !== currentStep);
            }
        });
        subtitle.textContent = subtitles[currentStep];
        btnPrev.classList.toggle('hidden', currentStep === 1);
        btnNext.classList.toggle('hidden', currentStep === totalSteps);
        btnSubmit.classList.toggle('hidden', currentStep !== totalSteps);
    }

    btnNext.addEventListener('click', () => {
        if (currentStep < totalSteps) {
            if (!validateStep(currentStep)) return;
            currentStep++;
            updateUI();
        }
    });

    btnPrev.addEventListener('click', () => {
        if (currentStep > 1) {
            clearError();
            currentStep--;
            updateUI();
        }
    });

    const urlParams = new URLSearchParams(window.location.search);
    const roleParam = urlParams.get('role');
    if (roleParam === 'candidate' || roleParam === 'recruiter') {
        selectRole(roleParam);
        currentStep = 2;
        updateUI();
    } else {
        updateUI();
    }
});