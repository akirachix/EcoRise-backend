from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PickupSerializer
from pickup.models import Pickup


class PickupViewSet(viewsets.ModelViewSet):
    queryset=Pickup.objects.all()
    serializer_class=PickupSerializer