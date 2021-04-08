from rest_framework import serializers
from historiarum.models import Fabula


class FabulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabula
        fields = ["titulus", "contentus", "timestamp", "user"]
