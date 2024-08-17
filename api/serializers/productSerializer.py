from rest_framework import serializers
from api.serializers.categorySerializer import CategorySerializer

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    count = serializers.CharField(max_length=10)
    categories = CategorySerializer(many=True)
