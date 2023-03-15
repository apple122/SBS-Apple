
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import LotteryGetBillSerializer, LotteryPostBillSerializer
from apps.lottery_bill.models import LotteryBill

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

DEPTH = "depth"
depth = openapi.Parameter(DEPTH, openapi.IN_QUERY,
                          description="depth",
                          type=openapi.TYPE_BOOLEAN)

boolean_mapping = {
    "true": True,
    "false": False
}

PERIOD = "period"
period = openapi.Parameter(PERIOD, openapi.IN_QUERY,
                           description="period",
                           type=openapi.TYPE_STRING)

DRAW = "is_draw"
is_draw = openapi.Parameter(DRAW, openapi.IN_QUERY,
                            description="is draw",
                            type=openapi.TYPE_BOOLEAN)


class ListCreateAPIView(ListCreateAPIView):
    queryset = LotteryBill.objects.all()
    serializer_class = LotteryGetBillSerializer

    @swagger_auto_schema(manual_parameters=[depth, period, is_draw])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = LotteryBill.objects.all()
        queryset = self.get_depth(queryset)
        queryset = self.get_period(queryset)
        queryset = self.get_is_draw(queryset)
        return queryset

    def get_depth(self, queryset):
        raw_depth = self.request.query_params.get(DEPTH)
        if not raw_depth:
            return queryset
        depth = boolean_mapping[raw_depth]
        if (depth):
            self.serializer_class = LotteryGetBillSerializer
        else:
            self.serializer_class = LotteryPostBillSerializer
        return queryset

    def get_period(self, queryset):
        is_draw = self.request.query_params.get(DRAW)
        if not is_draw:
            return queryset
        is_draw = boolean_mapping[is_draw]
        if is_draw is not None:
            queryset = queryset.filter(is_draw=is_draw)
        return queryset

    def get_is_draw(self, queryset):
        period_id = self.request.query_params.get(PERIOD)
        if not period_id:
            return queryset
        if period_id is not None:
            queryset = queryset.filter(
                period__id=period_id)
        return queryset


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LotteryBill.objects.all()
    serializer_class = LotteryPostBillSerializer
