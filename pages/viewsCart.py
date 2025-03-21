# from rest_framework import viewsets
from django.db.models.manager import BaseManager
from .models import *
from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view
from django.db.models import Q,Value,IntegerField,F
from django.db.models import Subquery, OuterRef
from rest_framework import status,generics,mixins,viewsets
from acounts.models import CustomUser


# @api_view(['GET'])
# def getfavorite(request,userid):
#     pr_fav=Favorite.objects.filter(user_fk=userid)
#     serializer=FavoriteSerializer(pr_fav,many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def cartList(request,userid):
        cart=Cart.objects.filter(user_fk=userid)
        serializer=CartSerializers(cart,many=True,context={'request': request})
        return Response(serializer.data)

# @api_view(['POST'])
# def cartinsert(request):
#         data=request.data
#         user = get_object_or_404(User, id=data['user_fk'])
#         product = get_object_or_404(Product, pr_id=data['pr_fk'])
#         cartdata, created = Cart.objects.get_or_create(user_fk=user, pr_fk=product,quantity=data['quantity'])
#         if created:
#             serializer =CartSerializers(cartdata)
#             return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cartinsert(request):
    data = request.data
    user = get_object_or_404(CustomUser, id=data['user_fk'])
    product = get_object_or_404(Product, pr_id=data['pr_fk'])

    # تحقق إذا كان المنتج موجودًا بالفعل في السلة لهذا المستخدم
    cart_item = Cart.objects.filter(user_fk=user, pr_fk=product).first()

    if cart_item:
        q=int(data['quantity'])
        # إذا كان المنتج موجودًا، قم بزيادة الكمية
        cart_item.quantity += 1
        cart_item.save()
        serializer = CartSerializers(cart_item)
        return Response({"status":"exist","data": serializer.data}, status=status.HTTP_200_OK)
    else:
        # إذا لم يكن موجودًا، قم بإنشاء سجل جديد في السلة
        cartdata = Cart.objects.create(user_fk=user, pr_fk=product, quantity=data['quantity'])
        serializer = CartSerializers(cartdata,context={'request': request})
        return Response({"status":"success","data": serializer.data}, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def cartdelete(request,cartId):
    try:
        cart=Cart.objects.get(cart_id=cartId)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    cart.delete()
    return Response({"status":"succes delete"},status=status.HTTP_200_OK)

@api_view(['DELETE'])
def cartdeleteall(request,user_id):
    try:
        cart=Cart.objects.filter(user_fk=user_id)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    cart.delete()
    return Response({"status":"succes delete all"},status=status.HTTP_200_OK)

@api_view(['PUT'])
def updatequantity(request,cart_id):
    data=request.data
    cart=Cart.objects.get(cart_id=cart_id)
    if data['action']=="plus":
        cart.quantity = F('quantity') + 1
        cart.save()
    elif data['action']=="minus":
        if cart.quantity>1:
            cart.quantity = F('quantity') - 1
            cart.save()
    # ser=CartSerializers(cart)
    return Response({"status":"succes updated quantity"},status=status.HTTP_200_OK)

@api_view(['PUT'])
def updatecart(request,cart_id):
    data=request.data
    cart=Cart.objects.get(cart_id=cart_id)
    cart.order=data['order']
    cart.save()
    # ser=CartSerializers(cart)
    return Response({"status":"succes updated cart"},status=status.HTTP_200_OK)
    
    # try:
    #     cart=Cart.objects.get(Q(pr_fk=pr_id) & Q(user_fk=user_id))
    # except Cart.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    # cart.delete()
    # return Response({"status":"succes delete"},status=status.HTTP_200_OK)