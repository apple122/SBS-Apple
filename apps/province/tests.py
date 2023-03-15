from django.test import TestCase
from django.urls import path, reverse, include, resolve
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework import status
import json
from .api.v1.views import ListCreateAPIView


class ProvinceTestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ListCreateAPIView.as_view()
        self.url = reverse("province_list")

    def test_create(self):
        data = {"province": "pakse", "is_active": "true"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_province(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)
        self.assertEqual(response.data['results'], [])

    def test_get_one_province(self):
        response = self.client.get(reverse('province_detail', kwargs={'pk': 1}))
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ListProviderTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ListCreateAPIView.as_view()
        self.url = reverse("province_detail")

    def test_update(self):
        response = self.client.put(reverse('province_detail', kwargs={'pk': 1}), {"province": "ນະຄອນຫລວງ", "is_active": "true"})
        print('data',response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {"province": "ນະຄອນຫລວງ", "is_active": "true"})


    def test_delete(self):
        response = self.client.delete(reverse('province_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(json.loads(response.content), {"detail": "Not found."})