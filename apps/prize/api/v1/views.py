
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PrizeSerializer
from apps.prize.models import Prize


class ListCreateAPIView(ListCreateAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
