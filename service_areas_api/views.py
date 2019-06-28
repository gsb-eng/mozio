"""
Service area related api's.
"""

from rest_framework import viewsets
from mozio.pagination import StandardResultsSetPagination
from service_areas_api.models import Provider
from service_areas_api.serializers import ProviderSerializer


HTTP_METHODS_ALLOWED = ['get', 'post', 'put', 'delete']


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
