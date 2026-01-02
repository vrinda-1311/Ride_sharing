from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import AllowAny,IsAuthenticated

from userapp.serializers import RegisterSeiralizers

from rest_framework import status

from rest_framework.authentication import BasicAuthentication

from rest_framework.authtoken.models import Token

# Create your views here.


class UserregisterView(APIView):

    permission_classes = [AllowAny]

    def post(self,request):

        user_serializer = RegisterSeiralizers(data= request.data)

        if user_serializer.is_valid():

            user = user_serializer.save()

            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):

    permission_classes = [IsAuthenticated]

    authentication_classes = [BasicAuthentication]

    def post(self,request):

        user = request.user

        token,created = Token.objects.get_or_create(user = request.user)

        return Response({"message":"login successfuly","token":token.key},status=status.HTTP_200_OK)
