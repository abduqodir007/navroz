from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import *
from .serializers import *

class ListApiView2(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class =PersonSerializers

class Id(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

class Delete(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

class Update(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

class Create(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers