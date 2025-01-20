from django.shortcuts import render
from app.serializers import *
from rest_framework.decorators import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from app.models import *
# Create your views here.
class UserRegister(APIView):
    serializer_class=UserSerializer
    def post(self,request):
        data=request.data
        uso=self.serializer_class(data=data)
        print(uso.initial_data)
        if uso.is_valid():
            uso.save()
        
            return Response(uso.data)
    