from django.urls import path,include
from rest_framework.routers  import DefaultRouter
from .views import PickupViewSet

router=DefaultRouter()
router.register(r'pickups', PickupViewSet,basename="pickup")
urlpatterns=[
    path("",include(router.urls)),
]