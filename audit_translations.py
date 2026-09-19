import re
import os
import glob
import polib

def check_all_templates():
    template_files = glob.glob('templates/**/*.html', recursive=True)
    all_trans = set()
    for tf in template_files:
        with open(tf, encoding='utf-8', errors='ignore') as f:
            content = f.read()
        matches = re.findall(r'{%\s*trans\s*["\'](.*?)["\']\s*%}', content)
        all_trans.update(matches)
        
    print(f"Total unique trans strings across ALL templates: {len(all_trans)}")
    
    # Specifically for dashboard.html:
    with open('templates/accounts/dashboard.html', encoding='utf-8') as f:
        dash_content = f.read()
    dash_matches = set(re.findall(r'{%\s*trans\s*["\'](.*?)["\']\s*%}', dash_content))
    print(f"Total in dashboard.html: {len(dash_matches)}")

    en_po = polib.pofile('locale/en/LC_MESSAGES/django.po')
    en_dict = {e.msgid: e for e in en_po}

    print("\n--- ALL TEMPLATES MISSING IN EN PO ---")
    all_missing = sorted([s for s in all_trans if s not in en_dict])
    print(f"Total missing in EN PO: {len(all_missing)}")
    for s in all_missing:
        print(f"ALL_MISSING: {repr(s)}")

    print("\n--- DASHBOARD STRINGS FUZZY IN EN PO ---")
    dash_fuzzy = sorted([s for s in dash_matches if s in en_dict and 'fuzzy' in en_dict[s].flags])
    for s in dash_fuzzy:
        print(f"FUZZY: {repr(s)} -> current msgstr: {repr(en_dict[s].msgstr)}")

if __name__ == '__main__':
    check_all_templates()

