from django.shortcuts import render
from rest_framework import viewsets
from pickup.models import Pickup
from .serializers import PickupSerializer

class PickupViewSet(viewsets.ModelViewSet):
    queryset=Pickup.objects.all()
    serializer_class=PickupSerializer
