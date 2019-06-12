from rest_framework import serializers
from .models import *


class BookTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = '__all__'


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
