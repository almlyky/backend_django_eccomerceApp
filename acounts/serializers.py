from typing import Literal
from djoser.serializers import UserCreateSerializer

from django.contrib.auth.models import User
from rest_framework import serializers

class Myserializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields=['email','username','password']

        
class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        
        extra_kwargs = {
            'username': {'required':True ,'allow_blank':False},
            'email' : {'required':True ,'allow_blank':False},
            'password' : {'required':True ,'allow_blank':False,'min_length':5}
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','email', 'username']