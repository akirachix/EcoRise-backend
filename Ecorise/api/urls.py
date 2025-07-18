from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from feedback.views import FeedbackViewSet

from .views import (
    PickupViewSet, UserViewSet, MaterialViewSet, ProductViewSet,
    PaymentViewSet, RewardViewSet, b2c_payment, b2c_result, b2c_timeout
)




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
    path('api/daraja/b2c/', b2c_payment, name='b2c_payment'),
    path('api/daraja/b2c/result/', b2c_result, name='b2c_result'),
    path('api/daraja/b2c/timeout/', b2c_timeout, name='b2c_timeout'),
    
]
