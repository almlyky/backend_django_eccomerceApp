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
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    fav = serializers.IntegerField()
    class Meta:
        model = Product
        fields = '__all__'

        def get_image_url(self, obj):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.pr_image.url) if obj.pr_image else None

class ProductSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
    product=ProductSubSerializer(read_only=True)
    class Meta:
        model=Offer
        fields='__all__'

class CategoriesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Categories
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
     pr_fk = ProductSubSerializer(read_only=True)
     class Meta:
        model =Favorite
        fields ='__all__'

        def get_image_url(self, obj):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.pr_fk.pr_image.url) if obj.pr_fk.pr_image else None
        


class FavoriteSubSerializer(serializers.ModelSerializer):
     class Meta:
        model =Favorite
        fields ='__all__'

class CartSerializers(serializers.ModelSerializer):
     pr_fk = ProductSubSerializer(read_only=True)
     class Meta:
        model =Cart
        fields ='__all__'

        def get_image_url(self, obj):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.pr_fk.pr_image.url) if obj.pr_fk.pr_image else None

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model=Order
        fields='__all__'
        
        
class OrderItemSerializer(serializers.ModelSerializer):
    product=ProductSubSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product') 
    class Meta:
        model=OrderItem
        fields='__all__'  

class AddsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Adds
        fields='__all__'
        def get_image_url(self, obj):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.iamge.url) if obj.iamge else None
           
# class UsersSerializer(serializers.ModelSerializer):
#      class Meta:
#         model =User
#         fields = '__all__'  
        