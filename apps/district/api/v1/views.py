
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DistrictGetSerializer, DistrictPostSerializer
from apps.district.models import District
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY, 
                            description="depth", 
                            type=openapi.TYPE_BOOLEAN)

PROVINCE = "province"
province = openapi.Parameter(PROVINCE, openapi.IN_QUERY,
                           description="province",
                           type=openapi.TYPE_STRING)

boolean_mapping = {
    "true": True,
    "false": False
}


class ListCreateAPIView(ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictPostSerializer

    @swagger_auto_schema(manual_parameters=[depth, province])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = District.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_province(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        self.serializer_class = DistrictGetSerializer if depth else DistrictPostSerializer
        return queryset

    def get_province(self, queryset):
        province = self.request.query_params.get(PROVINCE)
        if not province:
            return queryset
        if province is not None:
            queryset = queryset.filter(
                province__id=province)
        return queryset


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictPostSerializer
