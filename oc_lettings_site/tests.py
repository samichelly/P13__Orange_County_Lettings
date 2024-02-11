from django.test import TestCase
from django.urls import reverse


class IndexTests(TestCase):
    def test_index_page_status_code(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
