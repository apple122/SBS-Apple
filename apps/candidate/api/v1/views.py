
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.candidate.models import Candidate
from .serializers import CandidateGetSerializer, CandidatePostSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

boolean_mapping = {
    "true": True,
    "false": False
}

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY,
                          description="depth",
                          type=openapi.TYPE_BOOLEAN)


class ListCreateAPIView(ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateGetSerializer

    @swagger_auto_schema(manual_parameters=[depth])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Candidate.objects.all()
        queryset = self.get_depth(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        if (depth):
            self.serializer_class = CandidateGetSerializer
        else:
            self.serializer_class = CandidatePostSerializer
        return queryset


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidatePostSerializer
