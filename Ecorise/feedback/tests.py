from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from .models import Feedback

class FeedbackAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='testuser@example.com',
            phone_number='1234567890',
            user_type='Trader',
            password='testpassword123'
        )
        
        self.feedback = Feedback.objects.create(
            user=self.user,
            user_type='Trader',
            feedback='This is a test feedback'
        )
    
    def test_feedback_list(self):
        url = reverse('feedback-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertTrue(any(f['feedback_id'] == self.feedback.feedback_id for f in response.data))
    
    def test_feedback_detail(self):
        url = reverse('feedback-detail', kwargs={'pk': self.feedback.feedback_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['feedback_id'], self.feedback.feedback_id)
        self.assertEqual(response.data['feedback'], self.feedback.feedback)
    
    def test_feedback_create(self):
        url = reverse('feedback-list')
        data = {
            'user': self.user.user_id,
            'user_type': 'Trader',
            'feedback': 'New feedback from test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['feedback'], data['feedback'])
        self.assertEqual(response.data['user'], self.user.user_id)
    
    def test_feedback_update(self):
        url = reverse('feedback-detail', kwargs={'pk': self.feedback.feedback_id})
        data = {
            'user': self.user.user_id,
            'user_type': 'Trader',
            'feedback': 'Updated feedback content'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['feedback'], data['feedback'])
    
    def test_feedback_partial_update(self):
        url = reverse('feedback-detail', kwargs={'pk': self.feedback.feedback_id})
        data = {
            'feedback': 'Partially updated feedback'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['feedback'], data['feedback'])
    
    def test_feedback_delete(self):
        url = reverse('feedback-detail', kwargs={'pk': self.feedback.feedback_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
