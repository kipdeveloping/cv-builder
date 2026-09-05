const I18N = {
    es: {
        'Guardando...': 'Guardando...',
        'Guardado a las': 'Guardado a las',
        'Error al guardar': 'Error al guardar',
        'Error de conexión': 'Error de conexión',
        'Nueva habilidad': 'Nueva habilidad',
        'Publicando...': 'Publicando...',
    },
    en: {
        'Guardando...': 'Saving...',
        'Guardado a las': 'Saved at',
        'Error al guardar': 'Error saving',
        'Error de conexión': 'Connection error',
        'Nueva habilidad': 'New skill',
        'Publicando...': 'Publishing...',
    }
};

function getLanguage() {
    const lang = document.documentElement.lang || 'es';
    return lang.startsWith('en') ? 'en' : 'es';
}

function translate(key) {
    const lang = getLanguage();
    return I18N[lang][key] || key;
}

function t(key) {
    return translate(key);
}
