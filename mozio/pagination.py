"""Pagenation customization
"""

from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """Custom pagenation.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
