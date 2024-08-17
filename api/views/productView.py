from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import ProductSerializer
from .services import get_static_data

class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        product = get_static_data()
        serializer = ProductSerializer(product)
        return Response(serializer.data)