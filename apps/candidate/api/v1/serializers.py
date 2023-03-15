from rest_framework import serializers
from apps.candidate.models import Candidate


class CandidateGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = "__all__"
        depth = 3


class CandidatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = "__all__"
