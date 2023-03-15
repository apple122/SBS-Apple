
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PeriodTypeSerializer
from apps.period_type.models import PeriodType


class ListCreateAPIView(ListCreateAPIView):
    queryset = PeriodType.objects.all()
    serializer_class = PeriodTypeSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PeriodType.objects.all()
    serializer_class = PeriodTypeSerializer
