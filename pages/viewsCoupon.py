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
from datetime import datetime, timedelta,timezone
from dateutil import parser

@api_view(['POST'])
def checCoupon(request):
    coName=request.data['co_name']
    coupon=Coupon.objects.filter(co_name=coName).first()
    date=datetime.now().strftime('%Y-%m-%d')

    
    if coupon :
        expiry_date = coupon.co_expiredate.strftime('%Y-%m-%d')
        count=coupon.co_count
        # # جعل `expiry_date` واعياً بالمناطق الزمنية إذا لم يكن كذلك
        # if timezone.is_naive(expiry_date):
        #     expiry_date = timezone.make_aware(expiry_date)
        # # print(coupon.co_expiredate.date)

        if expiry_date > date and count>0:
            # print(coupon.co_expiredate)
            serializer=CouponSerializer(coupon,many=False)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
    return Response({"status":"error","message":"the coupon not found or expired !"},status=status.HTTP_404_NOT_FOUND)