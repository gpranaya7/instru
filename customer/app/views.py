from django.shortcuts import render
from app.serializers import *
from rest_framework.decorators import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from app.models import *
from django.contrib.auth  import authenticate
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
        lso=loginSerializer(data=data)
        email=request.data.get('email')
        password=request.data.get('password')
        auo=authenticate(email=email,password=password)
        if auo:
            if auo.is_active:
                return {
                    'email':auo.email,
                    'passowrd':auo.password,
                    'tokens':auo.tokens()
                }
            else:
                return HttpResponse('user is not active')
        else:
            return HttpResponse('user credentials are incorrect')
        