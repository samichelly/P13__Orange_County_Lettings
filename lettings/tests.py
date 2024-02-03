from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsTest(TestCase):
    def setUp(self):
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
        response = self.client.get(reverse("lettings:index"))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def test_letting_detail(self):
        response = self.client.get(reverse("lettings:letting", args=[1]))
        assert response.status_code == 200
        assert b"<title>Test Domain Versailles</title>" in response.content
