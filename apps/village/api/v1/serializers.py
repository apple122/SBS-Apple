from rest_framework import serializers
from apps.village.models import Village


class VillageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'
        depth = 1

class VillagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'
