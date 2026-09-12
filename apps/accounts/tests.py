from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from .models import UserProfile


class RegistrationTest(TestCase):
    def test_register_creates_user_and_profile(self):
        response = self.client.post(reverse('register'), {
            'email': 'nuevo@example.com',
            'first_name': 'Ana',
            'last_name': 'Perez',
            'password1': 'Contraseña1!',
            'password2': 'Contraseña1!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='nuevo@example.com').exists())

        user = User.objects.get(email='nuevo@example.com')
        self.assertIsNotNone(user.profile)
        self.assertEqual(user.first_name, 'Ana')

    def test_register_duplicate_email_rejected(self):
        User.objects.create_user(username='a@example.com', email='a@example.com', password='x2Qw!asd8')
        response = self.client.post(reverse('register'), {
            'email': 'a@example.com',
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

    def test_no_published_cv_shows_message(self):
        response = self.client.get(reverse('profile', args=[self.user.id]))
        self.assertContains(response, 'no tiene CVs publicados')


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
