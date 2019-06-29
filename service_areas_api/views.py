"""
Service area related api's.
"""

from django.contrib.gis.geos import Point

from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from mozio.pagination import StandardResultsSetPagination

from service_areas_api.models import Provider, ServiceArea
from service_areas_api.serializers import (
    ProviderSerializer, ServiceAreaSerializer, SearchSearviceAreaSerializer
)


HTTP_METHODS_ALLOWED = [
    'get',
    'post',
    'put',
    'delete'
]


class ProviderViewSet(viewsets.ModelViewSet):
    """
    Provider related api handler.

    Four http methods are allowed to act on providers.

    GET    -> To get the providers list with pagination enabled.
    POST   -> Add a new provider.
    PUT    -> Update the existing provider.
    DELETE -> Delete the existing provider.
    """

    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

    # pagination_class enables the pagination for GET list of providers.
    pagination_class = StandardResultsSetPagination
    http_method_names = HTTP_METHODS_ALLOWED


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    Service area related api handler.

    Four http methods are allowed to act on service areas.

    GET    -> To get the service areas list with pagination enabled.
    POST   -> Add a new service area.
    PUT    -> Update the existing service area.
    DELETE -> Delete the existing service area.
    """

    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

    # pagination_class enables the pagination for GET list of providers.
    pagination_class = StandardResultsSetPagination
    http_method_names = HTTP_METHODS_ALLOWED


class SearchServiceAreaViewSet(ListAPIView):
    """
    Service area search related api handler.

    GET    -> To get the service areas list with pagination enabled.
    """
    model = ServiceArea
    serializer_class = SearchSearviceAreaSerializer

    # pagination_class enables the pagination for GET list of providers.
    pagination_class = StandardResultsSetPagination
    http_method_names = ['get']

    def get_queryset(self):
        point = Point(float(self.kwargs['lng']), float(self.kwargs['lat']))
        return ServiceArea.objects.filter(area__contains=point)
