# # products/serializers.py

# from django.apps import apps
# from rest_framework import serializers

# # الحصول على جميع النماذج من قاعدة البيانات
# models = apps.get_models()

# # إنشاء Serializers لكل نموذج
# serializers_dict = {}

# for model in models:
#     class Meta:
#         model = model
#         fields = '__all__'
    
#     serializer = type(f'{model.__name__}Serializer', (serializers.ModelSerializer,), {'Meta': Meta})
#     serializers_dict[model.__name__] = serializer

# يمكن استخدام `serializers_dict` لاختيار الـ Serializer المناسب للنموذج المطلوب


# products/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    fav = serializers.IntegerField()
    class Meta:
        model = Product
        fields = '__all__'

class ProductSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Categories
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
     pr_fk = ProductSubSerializer(read_only=True)
     class Meta:
        model =Favorite
        fields ='__all__'

class FavoriteSubSerializer(serializers.ModelSerializer):
     class Meta:
        model =Favorite
        fields ='__all__'

class CartSerializers(serializers.ModelSerializer):
     pr_fk = ProductSubSerializer(read_only=True)
     class Meta:
        model =Cart
        fields ='__all__'

# class UsersSerializer(serializers.ModelSerializer):
#      class Meta:
#         model =User
#         fields = '__all__'  
        