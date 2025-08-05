from rest_framework import serializers
from material.models import Material
from pickup.models import Pickup ,Material
from pickup.utils import get_coordinates 
from product.models import Product
from users.models import User
from payment.models import Payment
from reward.models import Reward
from rest_framework import serializers
from users.models  import Profile

class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pickup
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_staff:
            validated_data.pop('pickup_status', None) 
        location = validated_data.get('market_location')
        lat, lon = get_coordinates(location)
        validated_data['market_latitude'] = lat
        validated_data['market_longitude'] = lon
        return super().create(validated_data)

    def update(self, instance, validated_data):
       
        user = self.context['request'].user
        if not user.is_staff:
         validated_data.pop('pickup_status', None)        
        location = validated_data.get('market_location', instance.market_location)
        lat, lon = get_coordinates(location)
        validated_data['market_latitude'] = lat
        validated_data['market_longitude'] = lon
        return super().update(instance, validated_data)




class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model= Material
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone_number', 'user_type', 'password']  # no 'user' or 'username'

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.get('email')
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        profile = Profile.objects.create(user=user, **validated_data)
        return profile



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'



class STKPushSerializer(serializers.Serializer):
   phone_number = serializers.CharField()
   amount = serializers.DecimalField(max_digits=10, decimal_places=2)
   account_reference = serializers.CharField()
   transaction_desc = serializers.CharField()


