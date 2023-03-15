
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProvinceSerializer
from apps.province.models import Province


class ListCreateAPIView(ListCreateAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
