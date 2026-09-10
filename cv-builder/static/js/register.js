document.addEventListener('DOMContentLoaded', function() {
    const roleSelect = document.getElementById('role-select');
    const wizard = document.getElementById('wizard');
    const roleWorker = document.getElementById('role-worker');
    const roleCompany = document.getElementById('role-company');
    const companyNotice = document.getElementById('company-notice');
    const startWorker = document.getElementById('start-worker');
    const form = document.getElementById('register-form');
    const steps = Array.from(document.querySelectorAll('.wizard-step'));
    const prevBtn = document.getElementById('wizard-prev');
    const nextBtn = document.getElementById('wizard-next');
    const submitBtn = document.getElementById('wizard-submit');
    const errorBox = document.getElementById('wizard-error');
    const msgSpans = Array.from(document.querySelectorAll('[data-msg]')).reduce(function(acc, el) {
        acc[el.dataset.msg] = el.textContent;
        return acc;
    }, {});
    const startStepEl = document.getElementById('start-step');
    const password1 = document.getElementById('id_password1');
    const passwordRuleItems = document.querySelectorAll('#password-rules [data-rule]');

    const TOTAL_STEPS = steps.length;
    let currentStep = 1;

    function openWizard(step) {
        roleSelect.classList.add('hidden');
        wizard.classList.remove('hidden');
        goToStep(step || 1, false);
    }

    if (roleWorker) {
        roleWorker.addEventListener('click', function() {
            openWizard(1);
        });
    }
    if (startWorker) {
        startWorker.addEventListener('click', function() {
            openWizard(1);
        });
    }
    if (roleCompany) {
        roleCompany.addEventListener('click', function() {
            companyNotice.classList.toggle('hidden');
        });
    }

    function updateProgress(step) {
        document.querySelectorAll('.step-indicator').forEach(function(el) {
            const s = parseInt(el.dataset.step, 10);
            el.classList.remove('bg-indigo-600', 'text-white', 'bg-green-500');
            el.classList.add('bg-gray-200', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
            if (s < step) {
                el.classList.add('bg-green-500', 'text-white');
                el.classList.remove('bg-gray-200', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
            } else if (s === step) {
                el.classList.add('bg-indigo-600', 'text-white');
                el.classList.remove('bg-gray-200', 'dark:bg-gray-700', 'text-gray-500', 'dark:text-gray-400');
            }
        });
        document.querySelectorAll('.step-line').forEach(function(el) {
            const s = parseInt(el.dataset.line, 10);
            el.classList.toggle('bg-indigo-400', s < step);
            el.classList.toggle('bg-gray-200', s >= step);
            el.classList.toggle('dark:bg-indigo-500', s < step);
            el.classList.toggle('dark:bg-gray-700', s >= step);
        });
        document.querySelectorAll('[data-step-label]').forEach(function(el) {
            el.classList.toggle('font-semibold', parseInt(el.dataset.stepLabel, 10) === step);
            el.classList.toggle('text-indigo-600', parseInt(el.dataset.stepLabel, 10) === step);
        });
    }

    function showError(message) {
        errorBox.textContent = message;
        errorBox.classList.remove('hidden');
    }

    function clearError() {
        errorBox.classList.add('hidden');
        errorBox.textContent = '';
    }

    function validateStep(step) {
        if (step === 1) {
            const fn = document.getElementById('id_first_name');
            const ln = document.getElementById('id_last_name');
            if (!fn.value.trim()) {
                showError(msgSpans['required']);
                fn.focus();
                return false;
            }
            if (!ln.value.trim()) {
                showError(msgSpans['required']);
                ln.focus();
                return false;
            }
        }
        if (step === 2) {
            return true;
        }
        if (step === 3) {
            const email = document.getElementById('id_email');
            const p2 = document.getElementById('id_password2');
            if (!email.value.trim() || !/^\S+@\S+\.\S+$/.test(email.value.trim())) {
                showError(msgSpans['email']);
                email.focus();
                return false;
            }
            if (!checkPasswordStrength(password1.value)) {
                showError(msgSpans['password']);
                password1.focus();
                return false;
            }
            if (password1.value !== p2.value) {
                showError(msgSpans['mismatch']);
                p2.focus();
                return false;
            }
        }
        return true;
    }

    function checkPasswordStrength(value) {
        const rules = {
            length: /.{8,}/.test(value),
            upper: /[A-Z]/.test(value),
            number: /[0-9]/.test(value),
            special: /[!@#$%^&*(),.?":{}|<>]/.test(value)
        };
        passwordRuleItems.forEach(function(item) {
            const ok = rules[item.dataset.rule];
            item.classList.toggle('text-green-600', ok);
            item.classList.toggle('dark:text-green-400', ok);
            item.classList.toggle('line-through', !ok);
        });
        return rules.length && rules.upper && rules.number && rules.special;
    }

    function goToStep(step, validate) {
        if (validate && !validateStep(currentStep)) {
            return;
        }
        if (step < 1) step = 1;
        if (step > TOTAL_STEPS) step = TOTAL_STEPS;

        currentStep = step;
        clearError();

        steps.forEach(function(el) {
            el.classList.toggle('hidden', parseInt(el.dataset.step, 10) !== step);
        });

        prevBtn.classList.toggle('invisible', step === 1);
        nextBtn.classList.toggle('hidden', step === TOTAL_STEPS);
        submitBtn.classList.toggle('hidden', step !== TOTAL_STEPS);

        updateProgress(step);
    }

    prevBtn.addEventListener('click', function() {
        goToStep(currentStep - 1, false);
    });
    nextBtn.addEventListener('click', function() {
        goToStep(currentStep + 1, true);
    });

    if (password1) {
        password1.addEventListener('input', function() {
            checkPasswordStrength(password1.value);
        });
    }

    const sectorHidden = document.getElementById('id_sector');
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

    const startStep = parseInt(startStepEl ? startStepEl.value : '0', 10);
    if (startStep > 0) {
        openWizard(startStep);
    }
});