"""Service area api ralated test cases.
"""

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from service_areas_api.models import Provider, ServiceArea
from tests.factory import (
    ProviderFactory, ServiceAreaFactory, TEST_SERVICE_AREA
)


class ServiceApiTestCase(APITestCase):

    def purgeData(self):
        """
        Purge is to delete objects to keep data consistent between test cases.
        """
        ServiceArea.objects.all().delete()
        Provider.objects.all().delete()

    def test_service_area_post(self):
        """
        Ensure we can create a new provider object.
        """
        provider = ProviderFactory.create()

        TEST_SERVICE_AREA['provider'] = provider.id

        url = reverse('service_area-list')
        response = self.client.post(url, TEST_SERVICE_AREA, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(
            ServiceArea.objects.get().name, TEST_SERVICE_AREA['name']
        )
        self.purgeData()

    def test_service_area_put(self):
        """
        Ensure we can create a new provider object.
        """
        test_name = 'TESTXYZ'
        provider = ProviderFactory.create()
        service_area = ServiceAreaFactory.create(provider=provider)
        self.assertEqual(ServiceArea.objects.get().name, service_area.name)

        # Updated data.
        TEST_SERVICE_AREA['name'] = test_name
        TEST_SERVICE_AREA['provider'] = provider.id

        url = reverse('service_area-detail', args=[service_area.id])
        response = self.client.put(url, TEST_SERVICE_AREA, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(
            ServiceArea.objects.get().name, test_name
        )
        self.purgeData()

    def test_service_area_list(self):
        """
        List the service area objects with pagination.
        """
        # Creating 18 providers for listing and testing pagination.
        provider = ProviderFactory.create()
        for num in range(18):
            ServiceAreaFactory.create(provider=provider)

        url = reverse('service_area-list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], 18)
        self.assertIsNotNone(data['next'])

        response = self.client.get(data['next'])
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], 18)
        self.assertIsNone(data['next'])
        self.purgeData()

    def test_service_area_get_pk(self):
        """
        Ensure we get a provider object for a given id.
        """
        provider = ProviderFactory.create()
        service_area = ServiceAreaFactory.create(provider=provider)
        url = reverse('service_area-detail', args=[service_area.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(ServiceArea.objects.get().name, service_area.name)
        self.purgeData()

    def test_service_area_get_pk_failure(self):
        """
        Ensure we get a provider object for a given id.
        """
        url = reverse('service_area-detail', args=[211])
        response = self.client.get(url)
        # Service shouldn't be there.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.purgeData()
