from django.test import TestCase
from django.contrib.auth.models import User
from apps.accounts.models import Skill, UserSkill
from apps.resumes.models import Resume
from apps.resumes.views import sync_skills_from_resume


class SyncSkillsFromResumeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.profile = self.user.profile

    def test_single_resume_skills_sync(self):
        Resume.objects.create(
            user=self.user,
            content={'skills': ['Python', 'Django', 'JavaScript']}
        )
        sync_skills_from_resume(self.user, ['Python', 'Django', 'JavaScript'])

        user_skills = UserSkill.objects.filter(user=self.profile)
        self.assertEqual(user_skills.count(), 3)
        skill_names = {us.skill.name for us in user_skills}
        self.assertEqual(skill_names, {'Python', 'Django', 'JavaScript'})

    def test_multiple_resumes_union_skills(self):
        Resume.objects.create(
            user=self.user,
            content={'skills': ['Python', 'Django']}
        )
        Resume.objects.create(
            user=self.user,
            content={'skills': ['JavaScript', 'React']}
        )
        sync_skills_from_resume(self.user, ['Python', 'Django'])

        user_skills = UserSkill.objects.filter(user=self.profile)
        self.assertEqual(user_skills.count(), 4)
        skill_names = {us.skill.name for us in user_skills}
        self.assertEqual(skill_names, {'Python', 'Django', 'JavaScript', 'React'})

    def test_removes_skills_no_longer_in_any_resume(self):
        Resume.objects.create(
            user=self.user,
            content={'skills': ['Python', 'Django']}
        )
        sync_skills_from_resume(self.user, ['Python', 'Django'])

        self.assertEqual(UserSkill.objects.filter(user=self.profile).count(), 2)

        Resume.objects.filter(user=self.user).update(
            content={'skills': ['Python']}
        )
        sync_skills_from_resume(self.user, ['Python'])

        user_skills = UserSkill.objects.filter(user=self.profile)
        self.assertEqual(user_skills.count(), 1)
        self.assertEqual(user_skills.first().skill.name, 'Python')

    def test_preserves_is_primary_flag(self):
        Resume.objects.create(
            user=self.user,
            content={'skills': ['Python', 'Django']}
        )
        sync_skills_from_resume(self.user, ['Python', 'Django'])

        python_skill = Skill.objects.get(name='Python')
        user_python = UserSkill.objects.get(user=self.profile, skill=python_skill)
        user_python.is_primary = True
        user_python.save()

        Resume.objects.filter(user=self.user).update(
            content={'skills': ['Python', 'Django', 'JavaScript']}
        )
        sync_skills_from_resume(self.user, ['Python', 'Django', 'JavaScript'])

        user_python = UserSkill.objects.get(user=self.profile, skill=python_skill)
        self.assertTrue(user_python.is_primary)

    def test_empty_skills_list(self):
        Resume.objects.create(user=self.user, content={'skills': []})
        sync_skills_from_resume(self.user, [])

        self.assertEqual(UserSkill.objects.filter(user=self.profile).count(), 0)

    def test_skills_with_whitespace(self):
        Resume.objects.create(
            user=self.user,
            content={'skills': ['  Python  ', '  Django  ']}
        )
        sync_skills_from_resume(self.user, ['  Python  ', '  Django  '])

        user_skills = UserSkill.objects.filter(user=self.profile)
        self.assertEqual(user_skills.count(), 2)
        skill_names = {us.skill.name for us in user_skills}
        self.assertEqual(skill_names, {'Python', 'Django'})
