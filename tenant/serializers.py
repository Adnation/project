from rest_framework import serializers
from .models import Tenant

class TenantSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Tenant