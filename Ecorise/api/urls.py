from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import MaterialViewSet, ProductViewSet
router=DefaultRouter()
router.register(r'material', MaterialViewSet)
router.register(r'product', ProductViewSet)
urlpatterns=[
    path('', include(router.urls)),
]

from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from .views import PaymentViewSet, RewardViewSet, b2c_payment, b2c_result, b2c_timeout
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Ecorise API", status=200)



from . import views
router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')
router.register(r'reward', RewardViewSet, basename='reward')

urlpatterns = [
    path('', include(router.urls)),
        path('api/daraja/b2c/', b2c_payment, name='b2c_payment'),
    path('api/daraja/b2c/result/', b2c_result, name='b2c_result'),
    path('api/daraja/b2c/timeout/', b2c_timeout, name='b2c_timeout'),
    path('', home, name='home'),
    
]

