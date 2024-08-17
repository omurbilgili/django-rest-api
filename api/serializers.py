from rest_framework import serializers
from .models import ProductData,CategoryData

class NumbersSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    count = serializers.CharField(max_length=10)
    categories = CategorySerializer(many=True)
