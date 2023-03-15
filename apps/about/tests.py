from django.test import TestCase
from django.urls import path, reverse, include, resolve
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import os
import io
from PIL import Image

# Create your tests here.
class TestCaseAbout(APITestCase):

    url = ("/api/v1/about")

    def test_create_about(self):
        photo_file = self.generate_photo_file()
        data = {
            'title': 'test title',
            'description': 'test content',
            "image": photo_file,
            'is_active': "true"
        }
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_get_about(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
