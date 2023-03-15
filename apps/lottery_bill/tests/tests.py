from rest_framework.test import APITestCase
from rest_framework import status
import io
from PIL import Image


class TestCasesLotteryBill(APITestCase):
    def setUp(self):
        self.test_test_url = '/api/v1/lottery_bill'

    # def test_create(self):
    #     photo = self.generate_photo()
    #     data = {
    #         'candidate': 1,
    #         'period': 1,
    #         'bill_number': '556',
    #         'seller_number': "2412",
    #         'total_cost': 556466,
    #         "image": photo,
    #         'is_draw': "true"
    #     }
    #     response = self.client.post(
    #         self.test_test_url, data, format='multipart')
    #     print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def generate_photo(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_get(self):
        response = self.client.get(self.test_test_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_id(self):
        response = self.client.get(self.test_test_url, kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
