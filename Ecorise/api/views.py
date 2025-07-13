from django.shortcuts import render
from rest_framework import viewsets
from payment.models import Payment
from reward.models import Reward
from .serializers import RewardSerializer, PaymentSerializer
# from .serializers import PaymentSerializer
class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class RewardViewSet(viewsets.ModelViewSet):
    queryset=Reward.objects.all()
    serializer_class=RewardSerializer

# Create your views here.
