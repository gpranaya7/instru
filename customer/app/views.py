from django.shortcuts import render
from app.serializers import *
from rest_framework.decorators import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from app.models import *
# Create your views here.
class UserRegister(APIView):
    def post(self,request):
        data=request.data
        uso=UserSerializer(data=data)
        CustomUser.objects.create_user(**uso.initial_data)
        return Response(uso.initial_data)
class user_login(APIView):
    def post(self,request):
        data=request.data
        