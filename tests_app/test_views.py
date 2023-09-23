import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from Littlelemon_Restaurant.views import *


class testmenuitems(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.menu_data = {'Title': 'Test_Item', 'Price': 10, 'Inventory':20}

    def test_get_method(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_mentod(self):
        self.client.login(username='testuser', password='testpassword')
        response  = self.client.post('http://127.0.0.1:8000/restaurant/menu-items/',self.menu_data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




        
        

