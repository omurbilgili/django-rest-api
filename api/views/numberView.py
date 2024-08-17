from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import NumbersSerializer

class AddNumbersView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NumbersSerializer(data=request.data)
        if serializer.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']
            result = number1 + number2
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)