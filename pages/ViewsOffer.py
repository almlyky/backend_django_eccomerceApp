from rest_framework import generics,status
from .models import *
from .serializers import *
from rest_framework.response import Response

class OfferCreateList(generics.ListCreateAPIView):
    queryset=Offer.objects.all()
    serializer_class=OfferSerializer

class OfferRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Offer.objects.all()
    serializer_class=OfferSerializer
