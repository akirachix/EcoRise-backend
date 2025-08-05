from rest_framework import serializers
from users.models import User
from payment.models import Payment
from reward.models import Reward
from material.models import Material
from pickup.models import Pickup
from product.models import Product
from pickup.utils import get_coordinates
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")
    password = serializers.CharField(label="Password", style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        from django.contrib.auth import authenticate
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                               email=email, password=password)
            if not user:
                raise serializers.ValidationError('Unable to log in with provided credentials.', code='authorization')
        else:
            raise serializers.ValidationError('Must include "email" and "password".', code='authorization')
        attrs['user'] = user
        return attrs

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'phone_number', 'user_type', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data.get('phone_number', ''),
            user_type=validated_data.get('user_type', 'Trader'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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