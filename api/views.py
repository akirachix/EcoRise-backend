from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from .serializers import PickupSerializer
from pickup.models import Pickup
from rest_framework import viewsets
from users.models import User
from .serializers import UserSerializer
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import STKPushSerializer
from .daraja import DarajaAPI
from .serializers import MaterialSerializer, ProductSerializer
from material.models import Material
from product.models import Product
from .serializers import PaymentSerializer, RewardSerializer
from payment.models import Payment
from reward.models import Reward
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework import generics
from .serializers import UserRegistrationSerializer
from users.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    




class PickupViewSet(viewsets.ModelViewSet):
    queryset=Pickup.objects.all()
    serializer_class=PickupSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class= MaterialSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class STKPushView(APIView):
   def post(self, request):
       serializer = STKPushSerializer(data=request.data)
       if serializer.is_valid():
           data = serializer.validated_data
           daraja = DarajaAPI()
           response = daraja.stk_push(
               phone_number=data['phone_number'],
               amount=data['amount'],
               account_reference=data['account_reference'],
               transaction_desc=data['transaction_desc']
           )
           return Response(response)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def daraja_callback(request):
   print("Daraja Callback Data:", request.data)
   return Response({"ResultCode": 0, "ResultDesc": "Accepted"})

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer






logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

    def post(self,request):
        name = request.data.get('name')
        password = request.data.get('password')

        user = authenticate(name = name,password = password)
        if user:
            token,created = Token.objects.get_or_create(user=user)