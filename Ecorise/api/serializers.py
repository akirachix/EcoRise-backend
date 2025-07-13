from rest_framework import serializers
from pickup.models import Pickup ,Material, User
from pickup.utils import get_coordinates 
class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pickup
        fields = '__all__'

    def create(self, validated_data):
        location = validated_data.get('market_location')
        lat, lon = get_coordinates(location)
        validated_data['market_latitude'] = lat
        validated_data['market_longitude'] = lon
        return super().create(validated_data)

    def update(self, instance, validated_data):
        location = validated_data.get('market_location', instance.market_location)
        lat, lon = get_coordinates(location)
        validated_data['market_latitude'] = lat
        validated_data['market_longitude'] = lon
        return super().update(instance, validated_data)