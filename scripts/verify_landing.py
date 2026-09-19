# -*- coding: utf-8 -*-
import os
import sys
import django

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_cvs.settings')
django.setup()

from django.test import Client
from django.utils import translation

client = Client()

languages_to_test = ['es', 'en', 'pt', 'fr', 'de', 'it', 'ja', 'ko', 'zh-hans', 'ar', 'ru', 'hi']

expected_snippets = {
    'es': ['Haz visible tu talento con un', 'perfil profesional interactivo', 'Perfil Vivo TalentStack', 'Superpoderes de TalentStack'],
    'en': ['Make your talent visible with an', 'interactive professional profile', 'TalentStack Live Profile', 'TalentStack Superpowers'],
    'pt': ['Torne seu talento visível com um', 'perfil profissional interativo', 'Perfil Vivo TalentStack', 'Superpoderes do TalentStack'],
    'fr': ['Rendez votre talent visible avec un', 'profil professionnel interactif', 'Profil Vivant TalentStack', 'Les Super-Pouvoirs de TalentStack'],
    'de': ['Machen Sie Ihr Talent sichtbar mit einem', 'interaktiven beruflichen Profil', 'TalentStack Live-Profil', 'Superkräfte von TalentStack'],
    'it': ['Rendi visibile il tuo talento con un', 'profilo professionale interattivo', 'Profilo Dinamico TalentStack', 'Superpoteri di TalentStack'],
    'ja': ['あなたの才能を可視化する', 'インタラクティブな専門プロフィール', 'TalentStack ライブプロフィール', 'TalentStack の強み'],
    'zh-hans': ['让您的才能脱颖而出：', '互动式专业人才主页', 'TalentStack 动态主页', 'TalentStack 核心超能力'],
    'ko': ['당신의 재능을 보여주는', '인터랙티브 전문 프로필', 'TalentStack 라이브 프로필', 'TalentStack의 핵심 역량'],
    'ar': ['اجعل موهبتك مرئية من خلال', 'ملف مهني تفاعلي', 'ملف TalentStack الحي', 'مزايا TalentStack الفائقة'],
    'ru': ['Раскройте свой талант с помощью', 'интерактивным профессиональным профилем', 'Живой профиль TalentStack', 'Суперсилы TalentStack'],
    'hi': ['अपनी प्रतिभा को दृश्यमान बनाएं', 'इंटरैक्टिव पेशेवर प्रोफ़ाइल', 'टैलेंटस्टैक लाइव प्रोफ़ाइल', 'टैलेंटस्टैक की महाशक्तियाँ'],
}

print("=== TESTING LANDING PAGE IN MULTIPLE LANGUAGES ===")
for lang, snippets in expected_snippets.items():
    client.cookies.load({django.conf.settings.LANGUAGE_COOKIE_NAME: lang})
    res = client.get('/', HTTP_ACCEPT_LANGUAGE=lang)
    assert res.status_code == 200, f"Failed with status {res.status_code} for {lang}"
    content = res.content.decode('utf-8')
    for snippet in snippets:
        assert snippet in content, f"Missing snippet '{snippet}' in landing for language '{lang}'"
    print(f"[{lang}] OK: Rendered 200 and all verified snippets matched!")

print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
