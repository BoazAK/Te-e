from rest_framework import serializers
from .models import Point, Publicity

class PointSerializer(serializers.ModelSerializer):
    class Meta :
        model = Point
        fields = ('name', 'description', 'latitude', 'longitude', 'image1', 'image2', 'category', 'time')

class PublicitySerializer(serializers.ModelSerializer):
    class Meta :
        model = Publicity
        fields = ('image','url')
