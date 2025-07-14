from django.test import TestCase


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from  users.models import User

class UserAPITests(APITestCase):

    def setUp(self):
        self.user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "phone_number": "1234567890",
            "user_type": "Trader",
            "password": "pass1234"
        }
        self.user = User.objects.create(**self.user_data)

    def test_list_users(self):
        url = reverse('user-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_user(self):
        url = reverse('user-list')
        data = {
            "name": "Amuor",
            "email": "mangaramuor@gmail.com",
            "phone_number": "0987654321",
            "user_type": "Trader",
            "password": "recyclingapp"
        }
        response = self.client.post(url, data)
        print("RESPONSE DATA:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_retrieve_user(self):
        url = reverse('user-detail', args={self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

# Create your tests here.

