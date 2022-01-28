from rest_framework import serializers
from .models import Category, Time, Point, Post, Publicity

class PostSerializer(serializers.ModelSerializer):
    point = serializers.ReadOnlyField(source = 'point.id')

    class Meta :
        model = Post
        fields = (
            'point',
            'post',
            'note',
            )

class PointSerializer(serializers.ModelSerializer):
    posts_set = PostSerializer(many = True, read_only = True)

    class Meta :
        model = Point
        fields = (
            'id',
            'name',
            'description',
            'latitude',
            'longitude',
            'image1',
            'image2',
            'category',
            'time',
            'posts_set',
            )

class CategorySerializer(serializers.ModelSerializer):
    points_set = PointSerializer(many = True, read_only = True)

    class Meta :
        model = Category
        fields = (
            'id',
            'title',
            'points_set',
            )

class TimeSerializer(serializers.ModelSerializer):
    points_set = PointSerializer(many = True, read_only = True)

    class Meta :
        model = Time
        fields = (
            'id',
            'hours',
            'points_set',
            )

class PublicitySerializer(serializers.ModelSerializer):
    class Meta :
        model = Publicity
        fields = (
            'get_image',
            'url',
            )
