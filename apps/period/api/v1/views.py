
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.period.models import Period
from .serializers import PeriodSerializer


boolean_mapping = {
    "true": True,
    "false": False
}


class ListCreateAPIView(ListCreateAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
