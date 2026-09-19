# -*- coding: utf-8 -*-
import polib
import re

with open('templates/landing.html', encoding='utf-8') as f:
    text = f.read()

matches = sorted(list(set(re.findall(r'{%\s*trans\s*["\'](.*?)["\']\s*%}', text))))
en_po = polib.pofile('locale/en/LC_MESSAGES/django.po')
en_dict = {e.msgid: e for e in en_po}

missing = [m for m in matches if m not in en_dict or not en_dict[m].msgstr.strip()]
print(f"Missing in landing.html: {len(missing)}")
for m in missing:
    print(m)
