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


# @api_view(['GET'])
# def getfavorite(request,userid):
#     pr_fav=Favorite.objects.filter(user_fk=userid)
#     serializer=FavoriteSerializer(pr_fav,many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def cartList(request,userid):
        cart=Cart.objects.filter(user_fk=userid)
        serializer=CartSerializers(cart,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def cartinsert(request):
        data=request.data
        user = get_object_or_404(User, id=data['user_fk'])
        product = get_object_or_404(Product, pr_id=data['pr_fk'])
        # cart_exists = Cart.objects.filter(Q(user_fk=user) & Q(pr_fk=product)).exists()
        # if cart_exists:
        #     return Response({"error": "Product is already in cart."})
        cartdata, created = Cart.objects.get_or_create(user_fk=user, pr_fk=product,quantity=data['quantity'])
        if created:
            serializer =CartSerializers(cartdata)
            return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def cartdelete(request,pr_id,user_id):
    try:
        cart=Cart.objects.get(Q(pr_fk=pr_id) & Q(user_fk=user_id))
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    cart.delete()
    return Response({"status":"succes delete"},status=status.HTTP_200_OK)

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
         
    
    # try:
    #     cart=Cart.objects.get(Q(pr_fk=pr_id) & Q(user_fk=user_id))
    # except Cart.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    # cart.delete()
    # return Response({"status":"succes delete"},status=status.HTTP_200_OK)