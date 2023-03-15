from rest_framework.test import APITestCase
from rest_framework import status


class CreateTestPeriod(APITestCase):

    def setUp(self):
        self.test_test_url = '/api/v1/period'

    def test_create(self):
        data = {
            'open_date': "2006-10-25",
            'close_date': '2006-10-25',
            'prize_id': 1,
            'period': "2023021"
        }
        response = self.client.post(self.test_test_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create(self):
        response = self.client.get(self.test_test_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_id(self):
        response = self.client.get(self.test_test_url, kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
