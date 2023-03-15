
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostGetSerializer, PostPostSerializer
from apps.post.models import Post
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY, 
                            description="depth", 
                            type=openapi.TYPE_BOOLEAN)

PERIOD = "period"
period = openapi.Parameter(PERIOD, openapi.IN_QUERY,
                           description="period",
                           type=openapi.TYPE_STRING)

boolean_mapping = {
    "true": True,
    "false": False
}


class ListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostPostSerializer

    @swagger_auto_schema(manual_parameters=[depth, period])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Post.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_period(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        self.serializer_class = PostGetSerializer if depth else PostPostSerializer
        return queryset

    def get_period(self, queryset):
        period = self.request.query_params.get(PERIOD)
        if not period:
            return queryset
        if period is not None:
            queryset = queryset.filter(
                period__id=period)
        return queryset


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostPostSerializer
