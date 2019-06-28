"""
Service area api related serializers.
"""

from rest_framework import serializers

from service_areas_api.models import Provider


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
