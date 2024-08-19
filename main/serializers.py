from rest_framework import serializers
from .models import *


class DillerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Diller
        fields = ('id','company_name','foto','ball')

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','diller','product_name','product_weight','product_price','product_quantity')