from rest_framework.test import APITestCase
from rest_framework import status


class CreateTestPrize(APITestCase):

    def setUp(self):
        self.test_test_url = '/api/v1/lottery_bill'
        print("self url", self)

    def test_create(self):
        data = {
            'prize': "1st",
            'total_cost': 1000000,
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
