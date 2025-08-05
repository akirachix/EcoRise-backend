from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from feedback.views import FeedbackViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .views import PickupViewSet, UserViewSet, MaterialViewSet, ProductViewSet, STKPushView, daraja_callback, PaymentViewSet, RewardViewSet

router = DefaultRouter()
router.register(r'pickups', PickupViewSet, basename='pickup')
router.register(r'users', UserViewSet)
router.register(r'material', MaterialViewSet)
router.register(r'product', ProductViewSet)
router.register(r'payment', PaymentViewSet, basename='payment')
router.register(r'reward', RewardViewSet, basename='reward')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
   path('', include(router.urls)),
   path('daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
   path('daraja/callback/', daraja_callback, name='daraja-callback'),
   path('login/', obtain_auth_token), 
   
    
]
