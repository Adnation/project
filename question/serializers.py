from rest_framework import serializers
from .models import Question

class QustionSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Question