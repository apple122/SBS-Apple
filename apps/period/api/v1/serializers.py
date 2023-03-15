from rest_framework import serializers
from apps.period.models import Period


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = "__all__"
