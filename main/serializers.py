from rest_framework import serializers
from .models import *

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','first_name','last_name','phone_number','age')
