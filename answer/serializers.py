from rest_framework import serializers
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Answer