from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Message, Room, User
import json

# Create your tests here.

class RoomTestCase(APITestCase):
  def test_room_create(self):
    data = {'name': 'Test Room'}
    response = self.client.post(
      '/create_room/',
      content_type='application/json',
      data=json.dumps(data),
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_room_bad_create(self):
    data = {}
    response = self.client.post(
      '/create_room/',
      content_type='application/json',
      data=json.dumps(data),
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
