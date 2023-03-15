from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/lottery_bill', ListCreateAPIView.as_view(), name='lottery_bill'),
    path('api/v1/lottery_bill/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='lottery_bill'),
]
