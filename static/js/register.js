document.addEventListener('DOMContentLoaded', () => {
    try {
        const _t = (typeof t === 'function') ? t : function(key) { return key; };

        const form = document.getElementById('wizard-form');
        if (!form) return;

        const configEl = document.getElementById('register-config');
        let blockedDomains = [];
        let initialStep = 1;
        let initialRole = 'candidate';

        if (configEl) {
            try {
                blockedDomains = JSON.parse(configEl.dataset.blockedDomains || '[]');
            } catch (e) {
                blockedDomains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'live.com', 'icloud.com'];
            }
            initialStep = parseInt(configEl.dataset.initialStep, 10) || 1;
            initialRole = configEl.dataset.initialRole || 'candidate';
        }

        const urlParams = new URLSearchParams(window.location.search);
        const roleParam = urlParams.get('role');
        if (roleParam === 'candidate' || roleParam === 'recruiter') {
            initialRole = roleParam;
            if (initialStep === 1) initialStep = 2;
        }

        let currentStep = initialStep;
        const totalSteps = 4;
        let selectedRole = initialRole;

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
        const recruiterHints = document.querySelectorAll('.recruiter-hint');
        const recruiterFields = document.querySelectorAll('.recruiter-fields');
        const labelFirstName = document.getElementById('label_first_name');
        const labelSector = document.getElementById('label_sector');

        // Inputs
        const emailInput = document.getElementById('id_email');
        const emailError = document.getElementById('email-error-msg');
        const password1Input = document.getElementById('id_password1');
        const password2Input = document.getElementById('id_password2');
        const passwordMatchFeedback = document.getElementById('password-match-feedback');
        const firstNameInput = document.getElementById('id_first_name');
        const lastNameInput = document.getElementById('id_last_name');
        const companyNameInput = document.getElementById('id_company_name');
        const sectorSelect = document.getElementById('id_sector');

        function getSubtitles() {
            return {
                1: _t('Paso 1 de 4 — ¿Qué buscas?'),
                2: _t('Paso 2 de 4 — Datos de acceso'),
                3: _t('Paso 3 de 4 — Datos personales'),
                4: _t('Paso 4 de 4 — Información específica')
            };
        }

        function showBannerError(message) {
            let errorDiv = document.getElementById('wizard-error');
            if (!errorDiv) {
                errorDiv = document.createElement('div');
                errorDiv.id = 'wizard-error';
                errorDiv.className = 'bg-red-50 dark:bg-red-900/50 border border-red-200 dark:border-red-700 text-red-700 dark:text-red-200 px-4 py-3 rounded-lg mb-4 text-sm';
                form.insertBefore(errorDiv, form.firstChild);
            }
            errorDiv.textContent = message;
            errorDiv.classList.remove('hidden');
            errorDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        function clearBannerError() {
            const errorDiv = document.getElementById('wizard-error');
            if (errorDiv) errorDiv.classList.add('hidden');
        }

        function setFieldError(input, errorEl, message) {
            if (input) {
                input.classList.add('input-error');
            }
            if (errorEl) {
                errorEl.textContent = message;
                errorEl.classList.remove('hidden');
            }
        }

        function clearFieldError(input, errorEl) {
            if (input) {
                input.classList.remove('input-error');
            }
            if (errorEl) {
                errorEl.textContent = '';
                errorEl.classList.add('hidden');
            }
        }

        // Live validation for password requirements
        function checkPasswordRules(password) {
            const rules = {
                length: password.length >= 8,
                uppercase: /[A-Z]/.test(password),
                number: /[0-9]/.test(password),
                special: /[!@#$%^&*(),.?":{}|<>]/.test(password)
            };

            function updateRule(elId, isValid) {
                const el = document.getElementById(elId);
                if (!el) return;
                const icon = el.querySelector('.rule-icon');
                if (isValid) {
                    el.classList.add('rule-valid');
                    el.classList.remove('text-gray-500', 'dark:text-gray-400');
                    if (icon) icon.textContent = '✓';
                } else {
                    el.classList.remove('rule-valid');
                    el.classList.add('text-gray-500', 'dark:text-gray-400');
                    if (icon) icon.textContent = '•';
                }
            }

            updateRule('rule-length', rules.length);
            updateRule('rule-uppercase', rules.uppercase);
            updateRule('rule-number', rules.number);
            updateRule('rule-special', rules.special);

            return rules.length && rules.uppercase && rules.number && rules.special;
        }

        if (password1Input) {
            password1Input.addEventListener('input', () => {
                checkPasswordRules(password1Input.value);
                if (password2Input && password2Input.value) {
                    checkPasswordMatch();
                }
                clearFieldError(password1Input);
            });
        }

        function checkPasswordMatch() {
            if (!password2Input || !passwordMatchFeedback) return false;
            const p1 = password1Input ? password1Input.value : '';
            const p2 = password2Input.value;

            if (!p2) {
                passwordMatchFeedback.classList.add('hidden');
                return false;
            }

            if (p1 === p2) {
                passwordMatchFeedback.textContent = _t('✓ Las contraseñas coinciden');
                passwordMatchFeedback.className = 'mt-1 text-xs text-green-600 dark:text-green-400';
                password2Input.classList.remove('input-error');
                return true;
            } else {
                passwordMatchFeedback.textContent = _t('Las contraseñas no coinciden');
                passwordMatchFeedback.className = 'mt-1 text-xs text-red-600 dark:text-red-400';
                password2Input.classList.add('input-error');
                return false;
            }
        }

        if (password2Input) {
            password2Input.addEventListener('input', () => {
                checkPasswordMatch();
            });
        }

        // Live validation for Email
        function checkEmailValid() {
            if (!emailInput) return false;
            const email = emailInput.value.trim();
            clearFieldError(emailInput, emailError);

            if (!email) return false;

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                setFieldError(emailInput, emailError, _t('Ingresa un correo electrónico válido.'));
                return false;
            }

            if (selectedRole === 'recruiter') {
                const domain = email.split('@').pop().toLowerCase();
                if (blockedDomains.includes(domain)) {
                    setFieldError(emailInput, emailError, _t('Los reclutadores deben usar un correo corporativo (no se permiten ' + domain + ', Gmail, Yahoo, etc).'));
                    return false;
                }
            }

            clearFieldError(emailInput, emailError);
            return true;
        }

        if (emailInput) {
            emailInput.addEventListener('input', () => {
                if (emailInput.value.includes('@')) {
                    checkEmailValid();
                } else {
                    clearFieldError(emailInput, emailError);
                }
            });
            emailInput.addEventListener('blur', () => {
                if (emailInput.value.trim()) {
                    checkEmailValid();
                }
            });
        }

        // Live clear on input for step 3 and 4 fields
        if (firstNameInput) {
            firstNameInput.addEventListener('input', () => {
                clearFieldError(firstNameInput, document.getElementById('error_first_name'));
            });
        }
        if (lastNameInput) {
            lastNameInput.addEventListener('input', () => {
                clearFieldError(lastNameInput, document.getElementById('error_last_name'));
            });
        }
        if (companyNameInput) {
            companyNameInput.addEventListener('input', () => {
                clearFieldError(companyNameInput, document.getElementById('error_company_name'));
            });
        }
        if (sectorSelect) {
            sectorSelect.addEventListener('change', () => {
                clearFieldError(sectorSelect, document.getElementById('error_sector'));
            });
        }

        function validateStep(step) {
            clearBannerError();

            if (step === 2) {
                const email = emailInput.value.trim();
                const p1 = password1Input.value;
                const p2 = password2Input.value;

                if (!email) {
                    setFieldError(emailInput, emailError, _t('El correo electrónico es obligatorio.'));
                    showBannerError(_t('Por favor, ingresa tu correo electrónico.'));
                    emailInput.focus();
                    return false;
                }

                if (!checkEmailValid()) {
                    showBannerError(_t('Por favor, corrige el correo electrónico.'));
                    emailInput.focus();
                    return false;
                }

                if (!p1) {
                    setFieldError(password1Input, null, '');
                    showBannerError(_t('Debes ingresar una contraseña.'));
                    password1Input.focus();
                    return false;
                }

                const isPasswordStrong = checkPasswordRules(p1);
                if (!isPasswordStrong) {
                    setFieldError(password1Input, null, '');
                    showBannerError(_t('La contraseña no cumple con todos los requisitos de seguridad requeridos.'));
                    password1Input.focus();
                    return false;
                }

                if (!p2) {
                    setFieldError(password2Input, null, '');
                    showBannerError(_t('Debes confirmar tu contraseña.'));
                    password2Input.focus();
                    return false;
                }

                if (p1 !== p2) {
                    setFieldError(password2Input, null, '');
                    showBannerError(_t('Las contraseñas no coinciden.'));
                    password2Input.focus();
                    return false;
                }
            }

            if (step === 3) {
                const fn = firstNameInput.value.trim();
                const ln = lastNameInput.value.trim();

                let hasError = false;

                if (!fn) {
                    setFieldError(firstNameInput, document.getElementById('error_first_name'), _t('Este campo es obligatorio.'));
                    hasError = true;
                } else {
                    clearFieldError(firstNameInput, document.getElementById('error_first_name'));
                }

                if (!ln) {
                    setFieldError(lastNameInput, document.getElementById('error_last_name'), _t('Este campo es obligatorio.'));
                    hasError = true;
                } else {
                    clearFieldError(lastNameInput, document.getElementById('error_last_name'));
                }

                if (selectedRole === 'recruiter') {
                    const cn = companyNameInput ? companyNameInput.value.trim() : '';
                    if (!cn) {
                        setFieldError(companyNameInput, document.getElementById('error_company_name'), _t('El nombre de la empresa es obligatorio.'));
                        hasError = true;
                    } else {
                        clearFieldError(companyNameInput, document.getElementById('error_company_name'));
                    }
                }

                if (hasError) {
                    showBannerError(_t('Por favor, completa todos los campos obligatorios del paso 3.'));
                    if (!fn) firstNameInput.focus();
                    else if (!ln) lastNameInput.focus();
                    else if (selectedRole === 'recruiter' && companyNameInput) companyNameInput.focus();
                    return false;
                }
            }

            if (step === 4) {
                const sector = sectorSelect ? sectorSelect.value.trim() : '';
                if (!sector) {
                    setFieldError(sectorSelect, document.getElementById('error_sector'), _t('Debes seleccionar un sector.'));
                    showBannerError(_t('Por favor, selecciona un sector para continuar.'));
                    sectorSelect.focus();
                    return false;
                } else {
                    clearFieldError(sectorSelect, document.getElementById('error_sector'));
                }
            }

            return true;
        }

        window.selectRole = function(role) {
            selectedRole = role;
            if (roleInput) roleInput.value = role;

            document.querySelectorAll('.role-btn').forEach(btn => {
                btn.classList.remove('selected');
            });
            const selectedBtn = document.getElementById('role-' + role);
            if (selectedBtn) selectedBtn.classList.add('selected');

            // Toggle recruiter hints
            recruiterHints.forEach(hint => {
                hint.classList.toggle('hidden', role !== 'recruiter');
            });

            // Toggle recruiter fields visibility and disabled state
            recruiterFields.forEach(el => {
                el.classList.toggle('hidden', role !== 'recruiter');
                const inputs = el.querySelectorAll('input, select, textarea');
                inputs.forEach(inp => {
                    inp.disabled = (role !== 'recruiter');
                });
            });

            // Update labels based on role
            if (labelFirstName) {
                labelFirstName.textContent = (role === 'recruiter')
                    ? _t('Nombre de Contacto')
                    : _t('Nombre');
            }

            if (labelSector) {
                labelSector.textContent = (role === 'recruiter')
                    ? _t('Sector de la Empresa')
                    : _t('Sector');
            }

            // Re-validate email if entered
            if (emailInput && emailInput.value.trim()) {
                checkEmailValid();
            }
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
            if (subtitle) subtitle.textContent = subtitles[currentStep];
            if (btnPrev) btnPrev.classList.toggle('hidden', currentStep === 1);
            if (btnNext) btnNext.classList.toggle('hidden', currentStep === totalSteps);
            if (btnSubmit) btnSubmit.classList.toggle('hidden', currentStep !== totalSteps);
        }

        if (btnNext) {
            btnNext.addEventListener('click', () => {
                if (currentStep < totalSteps) {
                    if (!validateStep(currentStep)) return;
                    currentStep++;
                    updateUI();
                    window.scrollTo({ top: form.offsetTop - 50, behavior: 'smooth' });
                }
            });
        }

        if (btnPrev) {
            btnPrev.addEventListener('click', () => {
                if (currentStep > 1) {
                    clearBannerError();
                    currentStep--;
                    updateUI();
                    window.scrollTo({ top: form.offsetTop - 50, behavior: 'smooth' });
                }
            });
        }

        // Form submit validation safeguard
        form.addEventListener('submit', (e) => {
            if (!validateStep(currentStep)) {
                e.preventDefault();
            }
        });

        // Initialize role and UI
        selectRole(initialRole);
        updateUI();

        // If password was prefilled, check rules
        if (password1Input && password1Input.value) {
            checkPasswordRules(password1Input.value);
        }

    } catch (e) {
        console.error('Register wizard error:', e);
    }
});
