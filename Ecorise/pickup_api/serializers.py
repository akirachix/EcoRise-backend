from rest_framework import serializers
from pickup.models import Pickup ,Material, User
class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pickup
        fields='__all__'