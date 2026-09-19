import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_cvs.settings')
import django
django.setup()

from django.utils import translation
from django.utils.translation import gettext as _
from apps.accounts.models import SEARCH_STATUS_CHOICES, AVAILABILITY_CHOICES, LOCATION_FLEX_CHOICES, SectorTag, Tag

test_strings = [
    "Mis Habilidades",
    "Editar estado",
    "Experiencia y Proyectos",
    "Perfil público",
    "Sin titular",
    "Sin biografía",
    "Activa para que tu perfil sea visible en el tablón",
    "Agregar experiencia",
    "Editar experiencia",
    "Agregar proyecto",
    "Editar proyecto",
    "¿Deseas eliminar esta experiencia laboral?",
    "¿Deseas eliminar este proyecto?",
    "Especialidad y Habilidades",
    "Experiencia Laboral",
    "Proyectos Destacados",
    "Redes Sociales y Portafolio",
    "Tecnologías",
]

languages = ['es', 'en', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'zh-hans', 'ar', 'ru', 'hi']

print("=== VERIFYING TRANSLATION FOR USER'S CORE STRINGS ===")
for lang in languages:
    translation.activate(lang)
    print(f"\n--- LANGUAGE: {lang} ---")
    for s in test_strings:
        trans = _(s)
        if trans == s and lang != 'es':
            print(f"  [WARN NOT TRANSLATED] '{s}' => '{trans}'")
        else:
            print(f"  [OK] '{s}' => '{trans}'")

print("\n=== VERIFYING MODEL CHOICES TRANSLATIONS IN EN ===")
translation.activate('en')
for code, label in SEARCH_STATUS_CHOICES:
    print(f"Search status: {code} => {label}")
for code, label in AVAILABILITY_CHOICES:
    print(f"Availability: {code} => {label}")
for code, label in LOCATION_FLEX_CHOICES:
    print(f"Location flex: {code} => {label}")

print("\n=== VERIFYING MODEL DISPLAY_NAME LOGIC ===")
s = SectorTag(name_es="Tecnología", name_en="Technology", slug="tech")
translation.activate('es')
print(f"Sector in 'es': {s.display_name}")
assert s.display_name == "Tecnología"

translation.activate('en')
print(f"Sector in 'en': {s.display_name}")
assert s.display_name == "Technology"

t = Tag(name_es="Desarrollo Web", name_en="Web Development", slug="web-dev")
translation.activate('es')
print(f"Tag in 'es': {t.display_name}")
assert t.display_name == "Desarrollo Web"

translation.activate('en')
print(f"Tag in 'en': {t.display_name}")
assert t.display_name == "Web Development"

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
