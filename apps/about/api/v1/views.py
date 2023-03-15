from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AboutSerializer
from apps.about.models import About
# import django_filters.rest_framework


class ListCreateAPIView(ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # def get_queryset(self):
    #     title = self.request.title
    #     return About.objects.filter(title=title)


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
