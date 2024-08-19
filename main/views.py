from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import *
from .serializers import *


# Diller Serializer
class Diller_View(generics.ListAPIView):
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

class Diller_Id(generics.RetrieveAPIView):
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

class Diller_Delete(generics.DestroyAPIView):
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

class Diller_Update(generics.UpdateAPIView):
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

class Diller_Create(generics.CreateAPIView):
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers


# Product Serializer
class Product_View(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_Id(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_Delete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_Update(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_Create(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers