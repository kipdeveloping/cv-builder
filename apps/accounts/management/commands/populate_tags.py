from django.core.management.base import BaseCommand
from apps.accounts.models import SectorTag, SectorRol, RolEspecialidad, Tag


class Command(BaseCommand):
    help = 'Populate the tag dictionary with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Populating tag dictionary...')

        # Create sectors
        sectors_data = {
            'tecnologia': {'name_es': 'Tecnología', 'name_en': 'Technology'},
            'marketing': {'name_es': 'Marketing', 'name_en': 'Marketing'},
            'diseno': {'name_es': 'Diseño', 'name_en': 'Design'},
            'salud': {'name_es': 'Salud', 'name_en': 'Health'},
            'finanzas': {'name_es': 'Finanzas', 'name_en': 'Finance'},
        }

        sectors = {}
        for slug, data in sectors_data.items():
            sector, _ = SectorTag.objects.update_or_create(
                slug=slug,
                defaults={'name_es': data['name_es'], 'name_en': data['name_en']}
            )
            sectors[slug] = sector
            self.stdout.write(f'  Sector: {sector.name_es}')

        # Create roles
        roles_data = {
            'tecnologia': [
                {'slug': 'dev-web', 'name_es': 'Dev Web', 'name_en': 'Web Dev'},
                {'slug': 'data-science', 'name_es': 'Data Science', 'name_en': 'Data Science'},
                {'slug': 'devops', 'name_es': 'DevOps', 'name_en': 'DevOps'},
            ],
            'marketing': [
                {'slug': 'growth-marketer', 'name_es': 'Growth Marketer', 'name_en': 'Growth Marketer'},
                {'slug': 'content-manager', 'name_es': 'Content Manager', 'name_en': 'Content Manager'},
            ],
            'diseno': [
                {'slug': 'disenador-3d', 'name_es': 'Diseñador 3D', 'name_en': '3D Designer'},
                {'slug': 'ui-ux-designer', 'name_es': 'UI/UX Designer', 'name_en': 'UI/UX Designer'},
            ],
            'salud': [
                {'slug': 'enfermero', 'name_es': 'Enfermero', 'name_en': 'Nurse'},
                {'slug': 'medico', 'name_es': 'Médico', 'name_en': 'Doctor'},
            ],
            'finanzas': [
                {'slug': 'analista-financiero', 'name_es': 'Analista Financiero', 'name_en': 'Financial Analyst'},
                {'slug': 'contador', 'name_es': 'Contador', 'name_en': 'Accountant'},
            ],
        }

        roles = {}
        for sector_slug, role_list in roles_data.items():
            for data in role_list:
                role, _ = SectorRol.objects.update_or_create(
                    sector=sectors[sector_slug],
                    slug=data['slug'],
                    defaults={'name_es': data['name_es'], 'name_en': data['name_en']}
                )
                roles[data['slug']] = role
                self.stdout.write(f'  Role: {role}')

        # Create specialties
        specialties_data = {
            'dev-web': [
                {'slug': 'backend', 'name_es': 'Backend', 'name_en': 'Backend'},
                {'slug': 'frontend', 'name_es': 'Frontend', 'name_en': 'Frontend'},
                {'slug': 'fullstack', 'name_es': 'Fullstack', 'name_en': 'Fullstack'},
            ],
            'data-science': [
                {'slug': 'ml-engineer', 'name_es': 'ML Engineer', 'name_en': 'ML Engineer'},
                {'slug': 'data-analyst', 'name_es': 'Data Analyst', 'name_en': 'Data Analyst'},
            ],
            'devops': [
                {'slug': 'cloud-infra', 'name_es': 'Cloud/Infra', 'name_en': 'Cloud/Infra'},
            ],
            'growth-marketer': [
                {'slug': 'b2b', 'name_es': 'B2B', 'name_en': 'B2B'},
                {'slug': 'b2c', 'name_es': 'B2C', 'name_en': 'B2C'},
            ],
            'content-manager': [
                {'slug': 'contenido', 'name_es': 'Contenido', 'name_en': 'Content'},
            ],
            'disenador-3d': [
                {'slug': 'renderizado', 'name_es': 'Renderizado', 'name_en': 'Rendering'},
            ],
            'ui-ux-designer': [
                {'slug': 'product-design', 'name_es': 'Product Design', 'name_en': 'Product Design'},
            ],
            'enfermero': [
                {'slug': 'uci', 'name_es': 'UCI', 'name_en': 'ICU'},
            ],
            'medico': [
                {'slug': 'general', 'name_es': 'General', 'name_en': 'General'},
            ],
            'analista-financiero': [
                {'slug': 'corporativo', 'name_es': 'Corporativo', 'name_en': 'Corporate'},
            ],
            'contador': [
                {'slug': 'fiscal', 'name_es': 'Fiscal', 'name_en': 'Tax'},
            ],
        }

        specialties = {}
        for role_slug, spec_list in specialties_data.items():
            for data in spec_list:
                spec, _ = RolEspecialidad.objects.update_or_create(
                    sector_rol=roles[role_slug],
                    slug=data['slug'],
                    defaults={'name_es': data['name_es'], 'name_en': data['name_en']}
                )
                specialties[data['slug']] = spec
                self.stdout.write(f'  Specialty: {spec}')

        # Create tags
        tags_data = {
            'backend': [
                {'slug': 'django', 'name_es': 'Django', 'name_en': 'Django', 'category': 'framework'},
                {'slug': 'typescript', 'name_es': 'TypeScript', 'name_en': 'TypeScript', 'category': 'lenguaje'},
                {'slug': 'docker', 'name_es': 'Docker', 'name_en': 'Docker', 'category': 'herramienta'},
                {'slug': 'postgresql', 'name_es': 'PostgreSQL', 'name_en': 'PostgreSQL', 'category': 'herramienta'},
            ],
            'frontend': [
                {'slug': 'react', 'name_es': 'React', 'name_en': 'React', 'category': 'framework'},
                {'slug': 'vue', 'name_es': 'Vue', 'name_en': 'Vue', 'category': 'framework'},
                {'slug': 'css', 'name_es': 'CSS', 'name_en': 'CSS', 'category': 'lenguaje'},
                {'slug': 'javascript', 'name_es': 'JavaScript', 'name_en': 'JavaScript', 'category': 'lenguaje'},
            ],
            'fullstack': [
                {'slug': 'django-react', 'name_es': 'Django+React', 'name_en': 'Django+React', 'category': 'framework'},
                {'slug': 'node-angular', 'name_es': 'Node+Angular', 'name_en': 'Node+Angular', 'category': 'framework'},
            ],
            'ml-engineer': [
                {'slug': 'python', 'name_es': 'Python', 'name_en': 'Python', 'category': 'lenguaje'},
                {'slug': 'tensorflow', 'name_es': 'TensorFlow', 'name_en': 'TensorFlow', 'category': 'framework'},
                {'slug': 'pytorch', 'name_es': 'PyTorch', 'name_en': 'PyTorch', 'category': 'framework'},
            ],
            'data-analyst': [
                {'slug': 'sql', 'name_es': 'SQL', 'name_en': 'SQL', 'category': 'lenguaje'},
                {'slug': 'power-bi', 'name_es': 'Power BI', 'name_en': 'Power BI', 'category': 'herramienta'},
                {'slug': 'excel', 'name_es': 'Excel', 'name_en': 'Excel', 'category': 'herramienta'},
            ],
            'cloud-infra': [
                {'slug': 'aws', 'name_es': 'AWS', 'name_en': 'AWS', 'category': 'herramienta'},
                {'slug': 'kubernetes', 'name_es': 'Kubernetes', 'name_en': 'Kubernetes', 'category': 'herramienta'},
                {'slug': 'terraform', 'name_es': 'Terraform', 'name_en': 'Terraform', 'category': 'herramienta'},
            ],
            'b2b': [
                {'slug': 'meta-ads', 'name_es': 'Meta Ads', 'name_en': 'Meta Ads', 'category': 'herramienta'},
                {'slug': 'hubspot', 'name_es': 'HubSpot', 'name_en': 'HubSpot', 'category': 'herramienta'},
                {'slug': 'google-analytics', 'name_es': 'Google Analytics', 'name_en': 'Google Analytics', 'category': 'herramienta'},
            ],
            'b2c': [
                {'slug': 'tiktok-ads', 'name_es': 'TikTok Ads', 'name_en': 'TikTok Ads', 'category': 'herramienta'},
                {'slug': 'mailchimp', 'name_es': 'Mailchimp', 'name_en': 'Mailchimp', 'category': 'herramienta'},
                {'slug': 'copywriting', 'name_es': 'Copywriting', 'name_en': 'Copywriting', 'category': 'soft_skill'},
            ],
            'contenido': [
                {'slug': 'seo', 'name_es': 'SEO', 'name_en': 'SEO', 'category': 'herramienta'},
                {'slug': 'wordpress', 'name_es': 'WordPress', 'name_en': 'WordPress', 'category': 'herramienta'},
                {'slug': 'semrush', 'name_es': 'Semrush', 'name_en': 'Semrush', 'category': 'herramienta'},
            ],
            'renderizado': [
                {'slug': 'blender', 'name_es': 'Blender', 'name_en': 'Blender', 'category': 'herramienta'},
                {'slug': 'v-ray', 'name_es': 'V-Ray', 'name_en': 'V-Ray', 'category': 'herramienta'},
                {'slug': 'autocad', 'name_es': 'AutoCAD', 'name_en': 'AutoCAD', 'category': 'herramienta'},
                {'slug': 'unreal-engine-5', 'name_es': 'Unreal Engine 5', 'name_en': 'Unreal Engine 5', 'category': 'herramienta'},
            ],
            'product-design': [
                {'slug': 'figma', 'name_es': 'Figma', 'name_en': 'Figma', 'category': 'herramienta'},
                {'slug': 'sketch', 'name_es': 'Sketch', 'name_en': 'Sketch', 'category': 'herramienta'},
                {'slug': 'adobe-xd', 'name_es': 'Adobe XD', 'name_en': 'Adobe XD', 'category': 'herramienta'},
            ],
            'uci': [
                {'slug': 'triaje', 'name_es': 'Triaje', 'name_en': 'Triage', 'category': 'soft_skill'},
                {'slug': 'soporte-vital', 'name_es': 'Soporte Vital Avanzado', 'name_en': 'Advanced Life Support', 'category': 'soft_skill'},
                {'slug': 'rcp', 'name_es': 'RCP', 'name_en': 'CPR', 'category': 'soft_skill'},
            ],
            'general': [
                {'slug': 'diagnostico', 'name_es': 'Diagnóstico', 'name_en': 'Diagnosis', 'category': 'soft_skill'},
                {'slug': 'farmacologia', 'name_es': 'Farmacología', 'name_en': 'Pharmacology', 'category': 'soft_skill'},
            ],
            'corporativo': [
                {'slug': 'power-bi-fin', 'name_es': 'Power BI', 'name_en': 'Power BI', 'category': 'herramienta'},
                {'slug': 'sap', 'name_es': 'SAP', 'name_en': 'SAP', 'category': 'herramienta'},
            ],
            'fiscal': [
                {'slug': 'conciliacion', 'name_es': 'Conciliación', 'name_en': 'Reconciliation', 'category': 'soft_skill'},
                {'slug': 'impuestos', 'name_es': 'Impuestos', 'name_en': 'Taxes', 'category': 'soft_skill'},
                {'slug': 'auditoria', 'name_es': 'Auditoría', 'name_en': 'Audit', 'category': 'soft_skill'},
            ],
        }

        for spec_slug, tag_list in tags_data.items():
            for data in tag_list:
                tag, _ = Tag.objects.update_or_create(
                    slug=data['slug'],
                    defaults={
                        'name_es': data['name_es'],
                        'name_en': data['name_en'],
                        'category': data['category'],
                        'especialidad': specialties[spec_slug],
                    }
                )
                self.stdout.write(f'  Tag: {tag.name_es}')

        self.stdout.write(self.style.SUCCESS('Tag dictionary populated successfully!'))
