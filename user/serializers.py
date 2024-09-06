from rest_framework import serializers
from .models import Categories

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["email"]