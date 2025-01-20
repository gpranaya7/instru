from rest_framework import serializers
from app.models import *
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=100,write_only=True)
    class Meta:
        model=CustomUser
        fields='__all__'

    
    



