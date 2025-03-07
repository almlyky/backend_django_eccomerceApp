from typing import Literal
from djoser.serializers import UserCreateSerializer
# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser

class Myserializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields=['email','username','password']

        
class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','email','password','is_active','pk']

        # extra_kwargs = {
        #     'username': {'required':True ,'allow_blank':False},
        #     'email' : {'required':True ,'allow_blank':False},
        #     'password' : {'required':True ,'allow_blank':False,'min_length':5}
        # }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk','email', 'username','is_active','is_staff']