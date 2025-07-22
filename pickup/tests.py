from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime
from django.utils.timezone import make_aware

from pickup.models import Pickup
from material.models import Material
from users.models import User
from api.serializers import PickupSerializer  

class PickupAPITestCase(APITestCase):
    def setUp(self):
        self.material = Material.objects.create(
            material_type="Plastic",
            price_per_kg=10.50
        )
        self.user = User.objects.create(
            name="Faith ",
            email="faith@gmail.com",
            phone_number="072345432",
            user_type="Trader",
            password="ertyhgr5"
        )
        self.pickup = Pickup.objects.create(
            material=self.material,
            user_id=self.user,
            market_location="Gikomba",
            market_latitude=1.234567,
            market_longitude=2.345678,
            pickup_status="Pending",
            
        )
        self.list_url = reverse('pickup-list')

    def test_get_pickup_list(self):
        response = self.client.get(self.list_url)
        pickups = Pickup.objects.all()
        serializer = PickupSerializer(pickups, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_pickup(self):
        data = {
            "material": self.material.material_id,
            "user_id": self.user.user_id,
            "market_location": "New Market",
            "market_latitude": 3.456789,
            "market_longitude": 4.567890,
            "pickup_status": "Confirmed",
            
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pickup.objects.count(), 2)
        self.assertEqual(Pickup.objects.get(request_id=response.data['request_id']).market_location, "New Market")

    def test_get_single_pickup(self):
        url = reverse('pickup-detail', args=[self.pickup.request_id])
        response = self.client.get(url)
        serializer = PickupSerializer(self.pickup)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

def test_update_pickup(self):
    url = reverse('pickup-detail', args=[self.pickup.request_id])
    data = {
        "material": self.material.material_id,
        "user": self.user.user_id,
        "market_location": "Updated Market",
        "market_latitude": 1.234567,
        "market_longitude": 2.345678,
        "pickup_status": "Confirmed",
    }
    response = self.client.put(url, data, format='json')
    print("Update response status:", response.status_code)
    print("Update response data:", response.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    self.pickup.refresh_from_db()
    self.assertEqual(self.pickup.market_location, "Updated Market")
    self.assertEqual(self.pickup.pickup_status, "Confirmed")
    

    def test_delete_pickup(self):
        url = reverse('pickup-detail', args=[self.pickup.request_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pickup.objects.count(), 0)
