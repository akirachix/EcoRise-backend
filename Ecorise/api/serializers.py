from rest_framework import serializers
from material.models import Material
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model= Material
        fields='__all__'
from product.models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'