"""
Faqctory classes for test data.
"""

import json

from django.contrib.gis.geos import GEOSGeometry
from django.utils.crypto import get_random_string

from factory import LazyAttribute, Sequence
from factory.django import DjangoModelFactory

from service_areas_api.models import Provider, ServiceArea


TEST_POLYGON = {
    "type": "Polygon",
    "coordinates": [
        [
            [78.001, 14.0122],
            [77.00212, 15.0001],
            [78.0233, 16.0111],
            [80.0323, 16.00202],
            [80.0023, 14.0022],
            [78.001, 14.0122]
        ]
    ]
}

TEST_SERVICE_AREA = {
    'name': 'Andhra Pradesh',
    'area': TEST_POLYGON,
    'price': 1111.111,
    'provider': None,
}


class ProviderFactory(DjangoModelFactory):
    name = LazyAttribute(lambda s: get_random_string(20))
    email = LazyAttribute(
        lambda provider: '{0}@test.com'.format(provider.name).lower()
    )
    phone_number = Sequence(lambda n: '+91910918%04d' % n)
    language = 'English'
    currency = 'USD'

    class Meta:
        model = Provider


class ServiceAreaFactory(DjangoModelFactory):

    name = LazyAttribute(lambda s: get_random_string(20))
    price = 111.111
    area = LazyAttribute(
        lambda area: GEOSGeometry(json.dumps(TEST_POLYGON))
    )

    class Meta:
        model = ServiceArea
