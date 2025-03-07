from rest_framework import generics,status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


class OrderCreateList(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

# class OrderItemCreateList(generics.ListCreateAPIView):
#     queryset=OrderItem.objects.all()
#     serializer_class=OrderItemSerializer
#     def get_queryset(self):
#         orderId= self.kwargs.get('orderId')
#         order=OrderItem.objects.filter(order=orderId)
#         return order
    
#     def create(self, request, *args, **kwargs):
#         if isinstance(request.data, list):  # تحقق إذا كان الإدخال عبارة عن قائمة
#             serializer = self.get_serializer(data=request.data, many=True)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             return Response(serializer.data, status=201)
#         else:  # إدخال فردي
#             return super().create(request, *args, **kwargs)

@api_view(['POST'])
def addorderItem(request):
    data=request.data
    if isinstance(data, list):
        serializer=OrderItemSerializer(data=data,many=True)
    else:
        serializer=OrderItemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getOrderItem(request,orderId):
    orderItem=OrderItem.objects.filter(order=orderId)
    serializer=OrderItemSerializer(orderItem,many=True)
    return Response(serializer.data)




class OrderItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer

