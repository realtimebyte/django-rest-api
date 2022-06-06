from django.contrib.auth.models import User
from rest_framework import serializers

class ShipmentSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'productName',
            'type',
            'company',
            'departureAddress',
            'arrivalDate'
        ]