from rest_framework import serializers
from app.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'

    def create_user(self,email,username,first_name,last_name,password):
        if not email:
            raise ValueError('email is not given')
        nemail=self.normalize_email(email)
        uo=self.model(email=nemail,username=username,first_name=first_name,last_name=last_name)
        uo.set_password(password)
        uo.save()
        return uo

    
    




