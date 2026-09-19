# -*- coding: utf-8 -*-
import os
import sys
import django

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_cvs.settings')
django.setup()

from django.test import Client

client = Client()

print("=== VERIFYING WALLS & APIS ===")

# 1. Candidate Wall Template
res_wall = client.get('/tablon/')
assert res_wall.status_code == 200, f"Failed wall with status {res_wall.status_code}"
content_wall = res_wall.content.decode('utf-8')
assert 'Tablón de Talentos' in content_wall or 'Tabl' in content_wall
assert 'Para trabajadores (Candidatos)' in content_wall
assert 'Para reclutadores (Empresas)' in content_wall
assert 'Filtros de Búsqueda Taxonómica' in content_wall
assert 'window.wallI18n' in content_wall
print("[OK] Candidate wall (/tablon/) rendered HTTP 200 with dual segmented navigation and filters.")

# 2. Recruiter Wall Template
res_recruiter = client.get('/tablon-empresas/')
assert res_recruiter.status_code == 200, f"Failed recruiter wall with status {res_recruiter.status_code}"
content_recruiter = res_recruiter.content.decode('utf-8')
assert 'Tablón de Empresas' in content_recruiter or 'Tabl' in content_recruiter
assert 'Para trabajadores (Candidatos)' in content_recruiter
assert 'Para reclutadores (Empresas)' in content_recruiter
assert 'Filtros de Empresas y Vacantes' in content_recruiter
assert 'window.recruiterWallI18n' in content_recruiter
print("[OK] Recruiter wall (/tablon-empresas/) rendered HTTP 200 with dual segmented navigation and filters.")

# 3. Wall API Profiles
res_api_profiles = client.get('/api/wall/profiles/')
assert res_api_profiles.status_code == 200, f"Failed wall api profiles with status {res_api_profiles.status_code}"
data_profiles = res_api_profiles.json()
assert 'profiles' in data_profiles
print(f"[OK] Wall API (/api/wall/profiles/) returned HTTP 200 and {len(data_profiles['profiles'])} profiles.")

# 4. Wall API Recruiters
res_api_recruiters = client.get('/api/wall/recruiters/')
assert res_api_recruiters.status_code == 200, f"Failed wall api recruiters with status {res_api_recruiters.status_code}"
data_recruiters = res_api_recruiters.json()
assert 'profiles' in data_recruiters
print(f"[OK] Recruiter Wall API (/api/wall/recruiters/) returned HTTP 200 and {len(data_recruiters['profiles'])} companies.")

# 5. Multilingual check for Candidate Wall in English
res_en = client.get('/tablon/', HTTP_ACCEPT_LANGUAGE='en')
assert res_en.status_code == 200
content_en = res_en.content.decode('utf-8')
assert 'For talent (Candidates)' in content_en
assert 'For recruiters (Companies)' in content_en
assert 'Taxonomic Search Filters' in content_en
print("[OK] Candidate wall rendered in English with translated segmented headers and filters.")

# 6. Multilingual check for Recruiter Wall in English
res_rec_en = client.get('/tablon-empresas/', HTTP_ACCEPT_LANGUAGE='en')
assert res_rec_en.status_code == 200
content_rec_en = res_rec_en.content.decode('utf-8')
assert 'For talent (Candidates)' in content_rec_en
assert 'For recruiters (Companies)' in content_rec_en
assert 'Company and Vacancy Filters' in content_rec_en
print("[OK] Recruiter wall rendered in English with translated segmented headers and filters.")

print("\nALL WALL VERIFICATIONS PASSED SUCCESSFULLY!")
