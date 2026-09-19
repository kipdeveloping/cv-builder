from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from .models import UserProfile, RecruiterProfile, SectorTag


class RegistrationTest(TestCase):
    def setUp(self):
        self.sector = SectorTag.objects.create(
            name_es='Tecnología',
            name_en='Technology',
            slug='tecnologia'
        )

    def test_candidate_registration_success(self):
        response = self.client.post(reverse('register'), {
            'role': 'candidate',
            'email': 'candidato@example.com',
            'first_name': 'Ana',
            'last_name': 'Perez',
            'sector': 'tecnologia',
            'password1': 'Contraseña1!',
            'password2': 'Contraseña1!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='candidato@example.com').exists())

        user = User.objects.get(email='candidato@example.com')
        self.assertIsNotNone(user.profile)
        self.assertEqual(user.first_name, 'Ana')
        self.assertEqual(user.last_name, 'Perez')
        self.assertEqual(user.profile.role, 'candidate')
        self.assertEqual(user.profile.sector, self.sector)

    def test_recruiter_registration_success(self):
        response = self.client.post(reverse('register'), {
            'role': 'recruiter',
            'email': 'recruiter@corporation.com',
            'first_name': 'Carlos',
            'last_name': 'Gomez',
            'company_name': 'Acme Corp',
            'company_type': 'empresa',
            'work_modality': 'remote',
            'sector': 'tecnologia',
            'password1': 'Contraseña1!',
            'password2': 'Contraseña1!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='recruiter@corporation.com').exists())

        user = User.objects.get(email='recruiter@corporation.com')
        self.assertEqual(user.profile.role, 'recruiter')
        self.assertTrue(hasattr(user, 'recruiter_profile'))
        self.assertEqual(user.recruiter_profile.company_name, 'Acme Corp')
        self.assertEqual(user.recruiter_profile.company_sector, self.sector)
        self.assertEqual(user.recruiter_profile.work_modality, 'remote')

    def test_recruiter_blocked_email_domain(self):
        response = self.client.post(reverse('register'), {
            'role': 'recruiter',
            'email': 'recruiter@gmail.com',
            'first_name': 'Carlos',
            'last_name': 'Gomez',
            'company_name': 'Acme Corp',
            'sector': 'tecnologia',
            'password1': 'Contraseña1!',
            'password2': 'Contraseña1!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'correo corporativo')
        self.assertFalse(User.objects.filter(email='recruiter@gmail.com').exists())

    def test_recruiter_missing_company_name(self):
        response = self.client.post(reverse('register'), {
            'role': 'recruiter',
            'email': 'recruiter@corporation.com',
            'first_name': 'Carlos',
            'last_name': 'Gomez',
            'company_name': '',
            'sector': 'tecnologia',
            'password1': 'Contraseña1!',
            'password2': 'Contraseña1!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'nombre de la empresa es obligatorio')
        self.assertFalse(User.objects.filter(email='recruiter@corporation.com').exists())

    def test_candidate_missing_sector(self):
        response = self.client.post(reverse('register'), {
            'role': 'candidate',
            'email': 'candidato2@example.com',
            'first_name': 'Ana',
            'last_name': 'Perez',
            'sector': '',
            'password1': 'Contraseña1!',
            'password2': 'Contraseña1!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'selecciona un sector')
        self.assertFalse(User.objects.filter(email='candidato2@example.com').exists())

    def test_register_duplicate_email_rejected(self):
        User.objects.create_user(username='a@example.com', email='a@example.com', password='x2Qw!asd8')
        response = self.client.post(reverse('register'), {
            'role': 'candidate',
            'email': 'a@example.com',
            'first_name': 'Ana',
            'last_name': 'Perez',
            'sector': 'tecnologia',
            'password1': 'Contraseña1!',
            'password2': 'Contraseña1!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ya está registrado')


class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user@example.com', email='user@example.com', password='Contraseña1!'
        )

    def test_login_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'user@example.com',
            'password': 'Contraseña1!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.id)

    def test_login_wrong_password(self):
        response = self.client.post(reverse('login'), {
            'username': 'user@example.com',
            'password': 'incorrecta',
        })
        self.assertEqual(response.status_code, 200)


class PasswordChangeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user@example.com', email='user@example.com',
            password='Contraseña1!', first_name='Ana', last_name='Perez'
        )
        self.client.login(username='user@example.com', password='Contraseña1!')

    def test_password_change_form_reachable(self):
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.status_code, 200)

    def test_password_change_works(self):
        response = self.client.post(reverse('password_change'), {
            'old_password': 'Contraseña1!',
            'new_password1': 'NuevaContraseña2!',
            'new_password2': 'NuevaContraseña2!',
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('NuevaContraseña2!'))


class PasswordResetTest(TestCase):
    def test_reset_email_sent(self):
        User.objects.create_user(
            username='user@example.com', email='user@example.com', password='Contraseña1!'
        )
        response = self.client.post(reverse('password_reset'), {
            'email': 'user@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('user@example.com', mail.outbox[0].to)

    def test_reset_form_reachable(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)


class ProfilePreferencesTest(TestCase):
    def test_employment_display(self):
        user = User.objects.create_user(username='p@example.com', email='p@example.com', password='Contraseña1!')
        profile = user.profile
        profile.employment_type = ['full_time', 'freelance']
        profile.save()
        self.assertIn('Full-time', profile.get_employment_types_display())
        self.assertIn('Freelance', profile.get_employment_types_display())

    def test_update_profile_preferences(self):
        user = User.objects.create_user(
            username='p@example.com', email='p@example.com',
            password='Contraseña1!', first_name='Ana', last_name='Perez'
        )
        self.client.login(username='p@example.com', password='Contraseña1!')
        response = self.client.post(reverse('update_profile_fields'), data={
            'willing_to_relocate': 'yes',
            'travel_availability': 'occasional',
            'employment_type': ['contract', 'part_time'],
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.willing_to_relocate, 'yes')
        self.assertEqual(profile.employment_type, ['contract', 'part_time'])


class PublicProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='cand@example.com', email='cand@example.com',
            password='Contraseña1!', first_name='Carla', last_name='Diaz'
        )
        self.profile = self.user.profile
        self.profile.headline = 'Desarrolladora Web'
        self.profile.is_public = True
        self.profile.save()

    def test_profile_page_reachable_anonymously(self):
        response = self.client.get(reverse('profile', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Desarrolladora Web')

    def test_nonexistent_user_returns_404(self):
        response = self.client.get(reverse('profile', args=[99999]))
        self.assertEqual(response.status_code, 404)

    def test_owner_sees_dashboard_link(self):
        self.client.login(username='cand@example.com', password='Contraseña1!')
        response = self.client.get(reverse('profile', args=[self.user.id]))
        self.assertContains(response, 'Ir al Dashboard')


class ContactEmailTest(TestCase):
    def setUp(self):
        self.candidate = User.objects.create_user(
            username='cand@example.com', email='cand@example.com', password='Contraseña1!'
        )

    def test_contact_anonymous_visitor_sends_email(self):
        response = self.client.post(reverse('contact_email', args=[self.candidate.id]), data={
            'name': 'Juan',
            'email': 'juan@example.com',
            'message': 'Hola, me interesa tu perfil.',
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('cand@example.com', mail.outbox[0].to)
        self.assertIn('Juan', mail.outbox[0].body)

    def test_contact_missing_fields_rejected(self):
        response = self.client.post(reverse('contact_email', args=[self.candidate.id]), data={
            'name': '',
            'email': 'juan@example.com',
            'message': '',
        }, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(mail.outbox), 0)

    def test_contact_invalid_email_rejected(self):
        response = self.client.post(reverse('contact_email', args=[self.candidate.id]), data={
            'name': 'Juan',
            'email': 'no-es-un-email',
            'message': 'Hola',
        }, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(mail.outbox), 0)


class LanguageSwitchTest(TestCase):
    def test_switch_to_english(self):
        # Post to set_language to switch to 'en'
        response = self.client.post(reverse('set_language'), {
            'language': 'en',
            'next': reverse('landing')
        })
        self.assertEqual(response.status_code, 302)
        # Verify django_language cookie or session is set
        self.assertIn('django_language', self.client.cookies)
        self.assertEqual(self.client.cookies['django_language'].value, 'en')

        # Request a page and verify English translation is served
        page = self.client.get(reverse('landing'))
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, 'lang="en"')

    def test_switch_to_french(self):
        response = self.client.post(reverse('set_language'), {
            'language': 'fr',
            'next': reverse('landing')
        })
        self.assertEqual(response.status_code, 302)
        page = self.client.get(reverse('landing'))
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, 'lang="fr"')


class MediaUploadTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='mediauser@example.com', email='mediauser@example.com', password='Contraseña1!'
        )
        self.client.login(username='mediauser@example.com', password='Contraseña1!')

    def test_upload_valid_image(self):
        # 1x1 transparent PNG
        png_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\rIDATx\x9cc`\x00\x00\x00\x02\x00\x01H\xaf\xa4q\x00\x00\x00\x00IEND\xaeB`\x82'
        uploaded = SimpleUploadedFile('test.png', png_data, content_type='image/png')
        response = self.client.post(reverse('upload_media'), {'image': uploaded})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'ok')
        self.assertIn('media_items/', data['url'])

    def test_upload_without_file_fails(self):
        response = self.client.post(reverse('upload_media'), {})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')

    def test_upload_invalid_mime_fails(self):
        bad_file = SimpleUploadedFile('script.sh', b'echo hello', content_type='text/plain')
        response = self.client.post(reverse('upload_media'), {'image': bad_file})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['status'], 'error')

