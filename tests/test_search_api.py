"""Service area api ralated test cases.
"""

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from tests.factory import ProviderFactory, ServiceAreaFactory


class ServiceApiTestCase(APITestCase):
    """Search service area api testcases.
    """

    def test_search_service_area_list(self):
        """
        List the service area objects intersected with the point.
        """
        search_point = {
            'lat': 14.57,
            'lng': 78.6
        }
        provider = ProviderFactory.create()
        # Creating 18 providers for listing and testing pagination.
        for num in range(18):
            ServiceAreaFactory.create(provider=provider)

        url = reverse('search', kwargs=search_point)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], 18)
        # Page 1 should contain only 10 results, because of pagination
        self.assertEqual(len(data['results']), 10)
        self.assertIsNotNone(data['next'])

        response = self.client.get(data['next'])
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Page 2 should contain only 8 results
        self.assertEqual(len(data['results']), 8)
        self.assertIsNone(data['next'])
