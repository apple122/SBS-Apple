
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import FooterSerializer
from apps.footer.models import Footer


class ListCreateAPIView(ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
