
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PrizeTypeSerializer
from apps.prize_type.models import PrizeType


class ListCreateAPIView(ListCreateAPIView):
    queryset = PrizeType.objects.all()
    serializer_class = PrizeTypeSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PrizeType.objects.all()
    serializer_class = PrizeTypeSerializer
