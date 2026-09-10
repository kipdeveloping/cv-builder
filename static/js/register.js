document.addEventListener('DOMContentLoaded', () => {
    let currentStep = 1;
    const totalSteps = 3;
    const form = document.getElementById('wizard-form');
    const btnNext = document.getElementById('btn-next');
    const btnPrev = document.getElementById('btn-prev');
    const btnSubmit = document.getElementById('btn-submit');
    const subtitle = document.getElementById('step-subtitle');
    const steps = document.querySelectorAll('.step');
    const dots = [document.getElementById('dot-1'), document.getElementById('dot-2'), document.getElementById('dot-3')];

    const subtitles = {
        1: typeof t === 'function' ? t('Paso 1 de 3 — Datos de acceso') : 'Paso 1 de 3 — Datos de acceso',
        2: typeof t === 'function' ? t('Paso 2 de 3 — Datos personales') : 'Paso 2 de 3 — Datos personales',
        3: typeof t === 'function' ? t('Paso 3 de 3 — Información profesional') : 'Paso 3 de 3 — Información profesional'
    };

    function updateUI() {
        steps.forEach((s, i) => {
            s.classList.toggle('hidden', i + 1 !== currentStep);
        });
        dots.forEach((d, i) => {
            d.classList.toggle('bg-indigo-600', i + 1 === currentStep);
            d.classList.toggle('bg-gray-300', i + 1 !== currentStep);
            d.classList.toggle('dark:bg-gray-600', i + 1 !== currentStep);
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
});
