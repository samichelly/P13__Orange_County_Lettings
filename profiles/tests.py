from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class ProfilesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser", password="password890", email="test_user@mail.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Rio")

    def test_profiles_index(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b"<title>Profiles</title>")

    def test_profile_detail(self):
        response = self.client.get(reverse("profiles:profile", args=["TestUser"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b"<title>TestUser</title>")
