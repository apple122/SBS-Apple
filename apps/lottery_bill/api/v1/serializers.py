from rest_framework import serializers
from apps.lottery_bill.models import LotteryBill


class LotteryGetBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryBill
        fields = '__all__'
        depth = 3


class LotteryPostBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryBill
        fields = '__all__'
