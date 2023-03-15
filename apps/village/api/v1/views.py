
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import VillageGetSerializer, VillagePostSerializer
from apps.village.models import Village
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY, 
                            description="depth", 
                            type=openapi.TYPE_BOOLEAN)

DISTRICT = "district"
district = openapi.Parameter(DISTRICT, openapi.IN_QUERY,
                           description="district",
                           type=openapi.TYPE_STRING)

boolean_mapping = {
    "true": True,
    "false": False
}


class ListCreateAPIView(ListCreateAPIView):
    queryset = Village.objects.all()
    serializer_class = VillagePostSerializer

    @swagger_auto_schema(manual_parameters=[depth, district])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Village.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_district(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        self.serializer_class = VillageGetSerializer if depth else VillagePostSerializer
        return queryset

    def get_district(self, queryset):
        district = self.request.query_params.get(DISTRICT)
        if not district:
            return queryset
        if district is not None:
            queryset = queryset.filter(
                district__id=district)
        return queryset


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Village.objects.all()
    serializer_class = VillagePostSerializer
