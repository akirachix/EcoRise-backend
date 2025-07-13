from django.urls import path, include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from .views import PaymentViewSet, RewardViewSet

router=DefaultRouter()
router.register(r'Payment', PaymentViewSet)
router.register(r'reward', RewardViewSet)
urlpatterns=[
    path('', include(router.urls)),
]



