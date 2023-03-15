from django.urls import path
from .views import ListCreateAPIView, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/footer', ListCreateAPIView.as_view(), name='footer'),
    path('api/v1/footer/<int:pk>',
         RetrieveUpdateDestroyAPIView.as_view(), name='footer'),
]
