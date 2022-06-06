from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from djangoDemo.serializers import ShipmentSerializer

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = ShipmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    