from rest_framework.test import APITestCase
from django.urls import reverse


class DrugsAPITestCase(APITestCase):

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)