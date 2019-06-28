"""
Service area app models.
"""

from django.db import models
from django.contrib.gis.db import models as gis_models

from phonenumber_field.modelfields import PhoneNumberField


class Provider(models.Model):
    """
    Provider model.
    """
    email = models.EmailField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=50, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    language = models.CharField(
        null=False, blank=False, default='English', max_length=30
    )
    currency = models.CharField(
        null=False, blank=False, max_length=3, default='USD'
    )

    class Meta:
        verbose_name = 'provider'
        verbose_name_plural = 'providers'
        db_table = 'provider'


class ServiceArea(gis_models.Model):
    name = gis_models.CharField(max_length=250)
    area = gis_models.PolygonField()
    price = gis_models.DecimalField(max_digits=13, decimal_places=4)
    provider = gis_models.ForeignKey(
        Provider,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'service_area'
        verbose_name_plural = 'service_areas'
        db_table = 'service_area'
