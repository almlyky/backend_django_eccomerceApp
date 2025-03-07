from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from django.db.models import Case, When, Value, IntegerField


@api_view(['GET','POST'])
def adsView(request):
    if request.method == 'GET':
        adds=Adds.objects.all()
        serialize=AddsSerializer(adds,many=True,context={'request': request})
        return Response(serialize.data)
    elif request.method == 'POST':
        # ads=Adds.objects.filter()
        serializer = AddsSerializer(data=request.data,context={'request': request})
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','PUT'])
def adsViewPk(request,pk):
    if request.method == 'DELETE':
        try:
            adds=Adds.objects.get(pk=pk)
        except Adds.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        adds.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            adds=Adds.objects.get(pk=pk)
        except Adds.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AddsSerializer(adds, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)