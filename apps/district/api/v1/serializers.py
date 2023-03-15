from rest_framework import serializers
from apps.district.models import District


class DistrictGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = "__all__"
        depth = 1


class DistrictPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = District
        fields = "__all__"