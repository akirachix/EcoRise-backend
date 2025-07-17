from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PickupSerializer
from pickup.models import Pickup


class PickupViewSet(viewsets.ModelViewSet):
    queryset=Pickup.objects.all()
    serializer_class=PickupSerializer


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



from .serializers import PaymentSerializer, RewardSerializer, B2CPaymentSerializer
from payment.models import Payment
from reward.models import Reward




class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer



import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import B2CPaymentSerializer
from .daraja import DarajaAPI


logger = logging.getLogger(__name__)

@api_view(['POST'])
def b2c_payment(request):
    serializer = B2CPaymentSerializer(data=request.data)
    if serializer.is_valid():
        try:
            logger.debug(f"B2C request payload: {request.data}")
            phone_number = serializer.validated_data['phone_number']
            amount = serializer.validated_data['amount']
            remarks = serializer.validated_data.get('remarks', '')
            command_id = serializer.validated_data.get('command_id', 'BusinessPayment')

            daraja_api = DarajaAPI()
            response = daraja_api.b2c(
                phone_number=phone_number,
                amount=amount,
                remarks=remarks,
                command_id=command_id
            )
            logger.debug(f"B2C response: {response}")
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"B2C payment failed: {str(e)}")
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    logger.error(f"Invalid request data: {serializer.errors}")
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def b2c_result(request):
    logger.debug(f"B2C result callback: {request.data}")
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def b2c_timeout(request):
    logger.debug(f"B2C timeout callback: {request.data}")
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)


# Create your views here.



from rest_framework import viewsets
from users.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

