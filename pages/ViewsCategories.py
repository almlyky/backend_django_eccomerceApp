# from rest_framework import viewsets
from .models import *
from django.http import HttpRequest
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status,generics,mixins,viewsets
from rest_framework.permissions import IsAuthenticated


# @api_view(['GET'])
# def getAllCategories(request):
#     categories=Categories.objects.all()
#     serialize=CategoriesSerializer(categories,many=True)
#     return Response(serialize.data)

# @api_view(['POST'])
# def createCategories(request):
#     serializer = CategoriesSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # 4. تحديث منتج
# @api_view(['PUT'])
# def Categories_update(request, pk):
#     try:
#         Categories = Categories.objects.get(pk=pk)
#     except Categories.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = CategoriesSerializer(Categories, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # 5. حذف منتج
# @api_view(['DELETE'])
# def Categories_delete(request, pk):
#     try:
#         Categories = Categories.objects.get(pk=pk)
#     except Categories.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     Categories.delete()
#     return Response(status=status.HTTP_401_UNAUTHORIZED)

# class cat_list(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Categories.objects.all()
#     serializer_class=CategoriesSerializer

#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
    
# class categories_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Categories.objects.all()
#     serializer_class=CategoriesSerializer

#     def get(self,request,pk):
#         return self.retrieve(request)
#     def put(self,request,pk):
#         return self.update(request)
#     def delete(self,request,pk):
#         return self.destroy(request)

class Cat_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer
    permission_classes=[IsAuthenticated]
    
class Cat_list(generics.ListCreateAPIView):
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer
    # permission_classes=[IsAuthenticated]