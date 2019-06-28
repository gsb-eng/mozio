"""
Service area api related serializers.
"""

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from service_areas_api.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    """
    Provider model serializer.

    We are allowing all the fields to get serialized.
    """

    class Meta:
        """
        Serializer meta definitions.
        """
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    """
    Service area serializer.
    """

    class Meta:
        """
        Serializer meta definitions.
        """
        model = ServiceArea
        fields = '__all__'
        geo_field = 'area'
