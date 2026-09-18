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

    const subtitles = {
        1: 'Paso 1 de 4 — ¿Qué buscas?',
        2: 'Paso 2 de 4 — Datos de acceso',
        3: 'Paso 3 de 4 — Datos personales',
        4: 'Paso 4 de 4 — Información específica'
    };

    // Role selection
    window.selectRole = function(role) {
        selectedRole = role;
        roleInput.value = role;
        
        // Update button styles
        document.querySelectorAll('.role-btn').forEach(btn => {
            btn.classList.remove('selected');
        });
        document.getElementById('role-' + role).classList.add('selected');
        
        // Show/hide recruiter hints
        recruiterHints.forEach(hint => {
            hint.classList.toggle('hidden', role !== 'recruiter');
        });
        
        // Show/hide GitHub button for recruiters
        if (githubBtn) {
            githubBtn.classList.toggle('hidden', role === 'recruiter');
        }
        
        // Show/hide role-specific fields
        document.querySelectorAll('.candidate-fields').forEach(el => {
            el.classList.toggle('hidden', role !== 'candidate');
        });
        document.querySelectorAll('.recruiter-fields').forEach(el => {
            el.classList.toggle('hidden', role !== 'recruiter');
        });
    };

    function updateUI() {
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
            currentStep++;
            updateUI();
        }
    });

    btnPrev.addEventListener('click', () => {
        if (currentStep > 1) {
            currentStep--;
            updateUI();
        }
    });

    // Initialize
    updateUI();
});
