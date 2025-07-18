from rest_framework import serializers
from material.models import Material
from pickup.models import Pickup ,Material, User
from pickup.utils import get_coordinates 
from product.models import Product
from users.models import User
from payment.models import Payment
from reward.models import Reward

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
    class Meta:
        model = User
        fields = '__all__'




class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

class B2CPaymentSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12, required=True, help_text="Recipient phone number in format 2547XXXXXXXX")
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=1, required=True, help_text="Amount to send (minimum 1)")
    remarks = serializers.CharField(max_length=100, required=True, help_text="Transaction remarks")
    command_id = serializers.ChoiceField(choices=['BusinessPayment', 'SalaryPayment', 'PromotionPayment'], required=True, help_text="B2C command ID")

    def validate_phone_number(self, value):
        if not value.startswith('254') or len(value) != 12 or not value[3:].isdigit():
            raise serializers.ValidationError("Phone number must be in the format 2547XXXXXXXX")
        return value

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value



