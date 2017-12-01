from rest_framework import serializers
from .models import List, Card

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List

class CardSerializar(serializers.ModelSerializer):
    class Meta:
        model = Card