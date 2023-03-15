from rest_framework.test import APITestCase
from rest_framework import status


class CreateTestCandidate(APITestCase):

    def setUp(self):
        self.test_test_url = '/api/v1/candidate'
        print("self url", self)

    def test_create(self):
        data = {
            'province': 2,
            'full_name': 'testing name',
            'phone_number': '2098959694',
            'seller_number': "1234",
            'is_active': "false"
        }
        response = self.client.post(self.test_test_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create(self):
        response = self.client.get(self.test_test_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_id(self):
        response = self.client.get(self.test_test_url, kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
