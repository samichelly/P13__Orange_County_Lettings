from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class ProfilesTest(TestCase):
    """
    TestCase class for testing the views of the profiles app.

    Methods:
        setUp: Set up initial data for the tests.
        test_profiles_index: Test the status code and content of the profiles index page.
        test_profile_detail: Test the status code and content of the profile detail page.
    """

    def setUp(self):
        """
        Set up initial data for the tests.

        Creates a test user and a profile associated with the user.
        """
        self.user = User.objects.create_user(
            username="TestUser", password="password890", email="test_user@mail.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Rio")

    def test_profiles_index(self):
        """
        Test the status code and content of the profiles index page.

        Asserts that the response status code is 200 and contains the expected title for the profiles index page.
        """
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b"<title>Profiles</title>")

    def test_profile_detail(self):
        """
        Test the status code and content of the profile detail page.

        Asserts that the response status code is 200 and contains the expected title for the profile detail page.
        """
        response = self.client.get(reverse("profiles:profile", args=["TestUser"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b"<title>TestUser</title>")
