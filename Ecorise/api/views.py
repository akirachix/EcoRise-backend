from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MaterialSerializer, ProductSerializer
from material.models import Material
from product.models import Product
class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class= MaterialSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# Create your views here.
