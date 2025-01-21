from rest_framework import serializers
from app.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'

    
class loginSerializer(serializers.ModelSerializer):
    tokens=serializers.SerializerMethodField()
    class Meta:
        model=CustomUser
        fields=['email','password','tokens']
    def get_token(self,obj):
        user=CustomUser.objects.get(obj=obj['email'])
        return {
            ' refresh':user.tokens()['refresh'],
            'access':user.objects()['access']
        }

    
    




