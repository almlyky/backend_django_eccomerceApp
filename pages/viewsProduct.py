# from rest_framework import viewsets
from .models import Product,Categories
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status,mixins,generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from rest_framework.decorators import api_view
from django.db.models import Q,Value,IntegerField
from .filterset import ProductFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# def getDatafilter(model, filter_field, filter_value):
#     try:
#         # filter_kwargs = {filter_field: filter_value}
#         queryset = model.objects.filter(filter_field=filter_value)
#     except model.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProductSerializer(queryset,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getAllProduct(request):
#     product=Product.objects.all()
#     print("count==================")
#     # for pr in product:
#     #    print(f"Product ID: {pr.pr_id}, Favorite: {pr.fav}")
#     serialize=ProductSerializer(product,many=True)
#     return Response(serialize.data)

# @api_view(['GET'])
# def getOneProduct(request, cat_fk):
#     try:
#         # filter_kwargs = {filter_field: filter_value}
#         queryset = Product.objects.get(pr_id=3)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProductSerializer(queryset)
#     print("===================",queryset.name)
#     return Response(serializer.data)

# # 3. إنشاء منتج جديد
# @api_view(['POST'])
# def createProduct(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # 4. تحديث منتج
# @api_view(['PUT'])
# def product_update(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProductSerializer(product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # 5. حذف منتج
# @api_view(['DELETE'])
# def product_delete(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     product.delete()
#     return Response(status=status.HTTP_401_UNAUTHORIZED)

# class product_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSubSerializer
#     filterset_class=ProductFilter
#     permission_classes=[IsAuthenticated]
#     filter_backends=[DjangoFilterBackend]
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
    
# class product_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     def get(self,request,pk):
#         return self.retrieve(request)
#     def put(self,request,pk):
#         return self.update(request)
#     def delete(self,request,pk):
#         return self.destroy(request)
    
    

# @api_view(['GET'])
# def getFilterProduct(request):
#    try:
#        filter_product=Product.objects.all()
#        filterset=ProductFilter(request,queryset=filter_product)
       
#     #    resPage=3
#     #    pagenator=PageNumberPagination()
#     #    pagenator.page_size=resPage

#     #    queryset=pagenator.paginate_queryset(filterset.qs,request)

#    except filter_product.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
   
#    serializer=ProductSubSerializer(filterset.qs,many=True)
#    return Response(serializer.data)



class Product_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSubSerializer
    # permission_classes=[IsAuthenticated]
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)  # يجعل التعديل جزئي بشكل افتراضي
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
class Product_list(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSubSerializer
    # permission_classes=[IsAuthenticated]

