from rest_framework import serializers
from payment.models import Payment
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields= '__all__'
from reward.models import Reward
class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields= '__all__'