from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SlideSerializer
from apps.slide.models import Slide


class ListCreateAPIView(ListCreateAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer