# from rest_framework import viewsets
from django.db.models.manager import BaseManager
from .models import *
from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .filterset import ProductFilter
from rest_framework.decorators import api_view
from django.db.models import Q,Value,IntegerField
from django.db.models import Case, When, Value, IntegerField
from rest_framework import status,generics,mixins,viewsets


@api_view(['GET'])
def getAllProductfav(request,cat_fk,user_id):
    pr_fav=Favorite.objects.filter(user_fk=user_id).values('pr_fk')
    product=Product.objects.filter(cat_fk=cat_fk)
    product_filter = ProductFilter(request.GET, queryset=product)

    products = product_filter.qs.annotate(
        fav=Case(
            When(pr_id__in=pr_fav, then=Value(1)),
            default=Value(0),
            output_field=IntegerField()
        )
    )
    serialize=ProductSerializer(products,many=True,context={'request': request})
    return Response(serialize.data)

@api_view(['GET'])
def getAllProduct(request,user_id):
    pr_fav=Favorite.objects.filter(user_fk=user_id).values('pr_fk')
    product=Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product)

    products = product_filter.qs.annotate(
        fav=Case(
            When(pr_id__in=pr_fav, then=Value(1)),
            default=Value(0),
            output_field=IntegerField()
        )
    )
    serialize=ProductSerializer(products,many=True,context={'request': request})
    return Response(serialize.data)

@api_view(['GET'])
def getSearch2(request, user_id):
    # جلب المفضلات
    pr_fav_ids = Favorite.objects.filter(user_fk=user_id).values_list('pr_fk',flat=True)
    print(pr_fav_ids)
    # تصفية المنتجات باستخدام cat_fk وتحديد المفضلة من عدمها
    product_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = product_filter.qs.annotate(
        fav=Case(
            When(pr_id__in=pr_fav_ids, then=Value(1)),
            default=Value(0),
            output_field=IntegerField()
        )
    )
    # تسلسل البيانات وإرجاعها
    serialize = ProductSerializer(products, many=True,context={'request': request})
    return Response(serialize.data)


@api_view(['DELETE'])
def deletfav(request,pr_id,user_id):
    try:
        pr_fav=Favorite.objects.get(Q(pr_fk=pr_id) & Q(user_fk=user_id))
    except Favorite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    pr_fav.delete()
    return Response({"status":"succes"},status=status.HTTP_200_OK)

@api_view(['POST'])
def insert(request):
    data=request.data
    user = get_object_or_404(User, id=data['user_fk'])
    product = get_object_or_404(Product, pr_id=data['pr_fk'])
    # serializer = FavoriteSerializer(data=request.data)
    favorite, created = Favorite.objects.get_or_create(user_fk=user, pr_fk=product)
    if created:
        serializer =FavoriteSerializer(favorite,context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

    # if serializer.is_valid():
    #     # pr_fav=Favorite.objects.get(Q(user_fk=data['user_fk']) & Q(pr_fk=data['pr_fk']))
    #     # pr_fk=FavoriteSerializer(pr_fav)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    # return Response(status=status.HTTP_400_BAD_REQUEST)



class viewsets_fav(viewsets.ModelViewSet):
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer 

@api_view(['GET'])
def getfavorite(request,userid):
    pr_fav=Favorite.objects.filter(user_fk=userid)
    serializer=FavoriteSerializer(pr_fav,many=True, context={'request': request})
    return Response(serializer.data)
