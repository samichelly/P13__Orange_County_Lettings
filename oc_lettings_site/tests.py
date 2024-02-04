from django.test import TestCase
from django.urls import reverse


class IndexTests(TestCase):
    """
    TestCase class for testing the index view of the oc_lettings_site app.

    Methods:
        test_index_page_status_code: Test the status code of the index page.
    """

    def test_index_page_status_code(self):
        """
        Test the status code of the index page.

        Asserts that the response status code is 200 for the index page.
        """
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
