document.addEventListener('DOMContentLoaded', function() {
    let currentSlide = 0;
    const carousel = document.getElementById('carousel-container');
    const cards = carousel ? carousel.querySelectorAll('.carousel-card') : [];
    const counter = document.getElementById('carousel-counter');

    function getCSRFToken() {
        const cookie = document.cookie.split(';').find(c => c.trim().startsWith('csrftoken='));
        return cookie ? cookie.split('=')[1] : '';
    }

    // Modal functions
    window.openModal = function(modalId) {
        document.getElementById(modalId).classList.remove('hidden');
        document.getElementById(modalId).classList.add('flex');
    };

    window.closeModal = function(modalId) {
        document.getElementById(modalId).classList.add('hidden');
        document.getElementById(modalId).classList.remove('flex');
    };

    // Carousel navigation
    window.nextSlide = function() {
        if (currentSlide < cards.length - 1) {
            currentSlide++;
            updateCarousel();
        }
    };

    window.prevSlide = function() {
        if (currentSlide > 0) {
            currentSlide--;
            updateCarousel();
        }
    };

    function updateCarousel() {
        if (cards[currentSlide]) {
            cards[currentSlide].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
        }
        if (counter) {
            counter.textContent = `${currentSlide + 1} of ${cards.length}`;
        }
    }

    // Contact form
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const name = document.getElementById('contact-name').value;
            const email = document.getElementById('contact-email').value;
            const message = document.getElementById('contact-message').value;
            const errorDiv = document.getElementById('contact-error');
            const successDiv = document.getElementById('contact-success');
            
            errorDiv.classList.add('hidden');
            successDiv.classList.add('hidden');
            
            try {
                const response = await fetch(profileUrls.contactEmail, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    },
                    body: JSON.stringify({ name, email, message })
                });
                
                const result = await response.json();
                
                if (result.status === 'ok') {
                    successDiv.textContent = t('Mensaje enviado correctamente.');
                    successDiv.classList.remove('hidden');
                    contactForm.reset();
                } else {
                    errorDiv.textContent = result.message || t('Error al enviar el mensaje.');
                    errorDiv.classList.remove('hidden');
                }
            } catch (error) {
                errorDiv.textContent = t('Error de conexion. Intenta de nuevo.');
                errorDiv.classList.remove('hidden');
            }
        });
    }
});
