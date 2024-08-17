from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NumbersSerializer

class AddNumbersView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NumbersSerializer(data=request.data)
        if serializer.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']
            result = number1 + number2
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaticDataView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "message": "Haftanın Günleri",
            "data": ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
        }
        return Response(data, status=status.HTTP_200_OK)
    

class SampleDataView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "message": "Rakamlar",
            "data": [0,1,2,3,4,5,6,7,8,9]
        }
        return Response(data, status=status.HTTP_200_OK)