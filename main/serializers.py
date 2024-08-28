from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

# Diller serializer
class DillerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Diller
        fields = ('id','company_name','foto','ball')

# Product serializer
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','diller','product_name','product_weight','product_price','product_quantity')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']