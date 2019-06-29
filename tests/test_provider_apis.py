"""Provider api related test cases.
"""

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from service_areas_api.models import Provider
from tests.factory import ProviderFactory


PROVIDER_DATA = {
    'email': 'test@test.com',
    'name': 'Test Name',
    'phone_number': '+911234567891',
    'language': 'Telugu',
    'currency': 'INR'
}


class ProviderApiTestCase(APITestCase):

    def purgeProviders(self):
        """
        Purge is to delete objects to keep data consistent between test cases.
        """
        Provider.objects.all().delete()

    def test_provider_post(self):
        """
        Ensure we can create a new provider object.
        """

        url = reverse('provider-list')
        response = self.client.post(url, PROVIDER_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(Provider.objects.get().name, 'Test Name')

        # Purge data, so that it won't effect other tests.
        self.purgeProviders()

    def test_provider_put(self):
        """
        Ensure we can create a new provider object.
        """
        provider = ProviderFactory.create()
        self.assertEqual(Provider.objects.get().name, provider.name)

        # Update the provider object
        url = reverse('provider-detail', args=[provider.id])
        response = self.client.put(url, PROVIDER_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Provider.objects.get().name, 'Test Name')

        # Purge data, so that it won't effect other tests.
        self.purgeProviders()

    def test_provider_get_pk(self):
        """
        Ensure we get a provider object for a given id.
        """
        provider = ProviderFactory.create()
        url = reverse('provider-detail', args=[provider.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(Provider.objects.get().name, provider.name)
        self.purgeProviders()

    def test_provider_get_pk_failure(self):
        """
        Ensure no provider exist with unknow id.
        """
        url = reverse('provider-detail', args=[111])
        response = self.client.get(url)

        # Provider should not be found, status should be 404
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Purge data, so that it won't effect other tests.
        self.purgeProviders()

    def test_provider_list(self):
        """
        List the provider objects with pagination.
        """
        # Creating 18 providers for listing and testing pagination.
        for num in range(18):
            ProviderFactory.create()

        url = reverse('provider-list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], 18)
        self.assertEqual(len(data['results']), 10)
        self.assertIsNotNone(data['next'])

        response = self.client.get(data['next'])
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], 18)
        self.assertEqual(len(data['results']), 8)
        self.assertIsNone(data['next'])
