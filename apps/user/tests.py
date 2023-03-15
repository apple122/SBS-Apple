# from rest_framework.test import APITestCase
# from rest_framework import status


# class CreateTestLotteryBill(APITestCase):

#     def setUp(self):
#         self.test_test_url = 'api/v1/user/register_staff'
#         print("self url", self)

#     def test_create(self):
#         data = {
#             'username': 'Pern',
#             'password': '12341234',
#             'is_staff': 'true',
#             'is_active': 'true'
#         }
#         response = self.client.post(self.test_test_url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# #     # def test_create(self):
# #     #     response = self.client.get(self.test_test_url)
# #     #     self.assertEqual(response.status_code, status.HTTP_200_OK)

# #     # def test_get_by_id(self):
# #     #     response = self.client.get(self.test_test_url, kwargs={'pk': 1})
# #     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
