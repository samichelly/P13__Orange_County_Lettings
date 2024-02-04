from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsTest(TestCase):
    """
    TestCase class for testing Lettings app functionality.

    Methods:
        setUp: Set up initial data for tests.
        test_lettings_index: Test the index view of the Lettings app.
        test_letting_detail: Test the detail view of a letting in the Lettings app.
    """

    def setUp(self):
        """
        Set up initial data for tests.

        Creates an Address and a Letting for testing.
        """
        self.address = Address.objects.create(
            number=20,
            street="rue des Merisiers",
            city="Versailles",
            state="Yvelines",
            zip_code=78000,
            country_iso_code="FRA",
        )
        self.letting = Letting.objects.create(
            title="Test Domain Versailles", address=self.address
        )

    def test_lettings_index(self):
        """
        Test the index view of the Lettings app.

        Asserts that the response status code is 200 and contains the expected title.
        """
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b"<title>Lettings</title>")

    def test_letting_detail(self):
        """
        Test the detail view of a letting in the Lettings app.

        Asserts that the response status code is 200 and contains the expected title.
        """
        response = self.client.get(reverse("lettings:letting", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, b"<title>Test Domain Versailles</title>")
