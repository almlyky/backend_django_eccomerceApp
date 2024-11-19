from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status,generics,mixins,viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class pro(APIView):
    def get(self,request):
        pr=Product.objects.all()
        serial=ProductSerializer(pr,many=True)
        return Response(serial.data)


@api_view(["GET","POST","DELETE"])
def product(request,pk):
    if request.method=='GET':
        pr2=Product.objects.all()
        serial=ProductSerializer(pr2,many=True)
        return Response(serial.data)
    elif request.method=='POST':
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        try:
            pro=Product.objects.get(pr_id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        pro.delete()
        return Response(status=status.HTTP_200_OK)

    # pr=[
    #     {'prid':1,'prname':"ali"},
    #     {'prid':2,'prname':"ali"},
    #     {'prid':3,'prname':"ali"},
    #     {'prid':4,'prname':"ali"},
    #     {'prid':5,'prname':"ali"}
    # ]


class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)
    

class generic_list(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # authentication_classes=[TokenAuthentication]
    # authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]


class geneeic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
# class users_pk(generics.ListCreateAPIView):
#     queryset=Users.objects.all()
#     serializer_class=UsersSerializer


class viewsets_products(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer 