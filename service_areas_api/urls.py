"""
Service area app urls.
"""

from django.urls import include, path
from rest_framework import routers

from service_areas_api import views


router = routers.DefaultRouter()
router.register(r'service_area', views.ServiceAreaViewSet, 'service_area')
router.register(r'provider', views.ProviderViewSet, 'provider')


urlpatterns = [
    path('', include(router.urls)),
]
