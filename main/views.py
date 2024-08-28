# Django va DRF importlari
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, serializers

# Loyiha importlari
from .models import Diller, Product
from django.contrib.auth.models import User
from .serializers import UserSerializer, DillerSerializers, ProductSerializers


# Diller Views
class Diller_View(generics.ListAPIView):
    """Diller ro'yxati."""
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

class Diller_Id(generics.RetrieveAPIView):
    """Muayyan Diller."""
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

class Diller_Delete(generics.DestroyAPIView):
    """Diller o'chirish."""
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

class Diller_Update(generics.UpdateAPIView):
    """Diller yangilash."""
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

class Diller_Create(generics.CreateAPIView):
    """Diller yaratish."""
    queryset = Diller.objects.all()
    serializer_class = DillerSerializers

# Product Views
class Product_View(generics.ListAPIView):
    """Product ro'yxati."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_Id(generics.RetrieveAPIView):
    """Muayyan Product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_Delete(generics.DestroyAPIView):
    """Product o'chirish."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_Update(generics.UpdateAPIView):
    """Product yangilash."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_Create(generics.CreateAPIView):
    """Product yaratish."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializers



# User List View
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User Id View
class UserId(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User Create View
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User Detail View
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User Update View
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User Delete View
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

