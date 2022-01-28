from django.shortcuts import render
from django.http import Http404

from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from .models import Category, Time, Point, Post, Publicity
from .serializers import CategorySerializer, TimeSerializer, PointSerializer, PostSerializer, PublicitySerializer

# Create your views here.
# Routes list
class APIUrls(APIView):
    def get(self, request, format = None):
        data = {
            'List of all routes' : 'http://127.0.0.1:8000/food_points/',
            'List of all publicities' : 'http://127.0.0.1:8000/food_points/pub-list/',
            'List of all categories with categorie add and search on categories options' : 'http://127.0.0.1:8000/food_points/categories/',
            'List of all times with time add and search on times options' : 'http://127.0.0.1:8000/food_points/times/',
            'List of all points with point add and search on points options' : 'http://127.0.0.1:8000/food_points/points/',
            'List of all points by category with point add add search on points options' : 'http://127.0.0.1:8000/food_points/categories/<str:category_id>/',
            'List of all points by time with point add add search on points options' : 'http://127.0.0.1:8000/food_points/times/<str:time_id>/',
            'Point Detail' : 'http://127.0.0.1:8000/food_points/points/<int:pk>/',
            'List of comments by point with comment add option' : 'http://127.0.0.1:8000/food_points/posts/<str:point_id>/'
        }
        return Response(data)

# Publicities List
class PubList(APIView):
    def get(self, request, format = None):
        pubs = Publicity.objects.all().filter(publicity_disponibility = True).order_by('-pub_date')
        serializer = PublicitySerializer(pubs, many = True)

        return Response(serializer.data)

# Categories List and creation
class CategoriesList(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

# Times List and creation
class TimeList(generics.ListCreateAPIView):
    search_fields = ['hours']
    filter_backends = (filters.SearchFilter,)
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

    def perform_create(self, serializer):
        serializer.save()

# Points List and creation
class PointList(generics.ListCreateAPIView):
    search_fields = ('name', 'description')
    filter_backends = (filters.SearchFilter,)
    queryset = Point.objects.all().filter(point_disponibility = True).order_by('-creation_date')
    serializer_class = PointSerializer

    def perform_create(self, serializer):
        serializer.save()

# Points List by Category and creation
class CategoryPointList(generics.ListCreateAPIView):
    search_fields = ('name', 'description')
    filter_backends = (filters.SearchFilter,)
    serializer_class = PointSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        try :
            cat = Category.objects.get(id = category_id)
            return Point.objects.filter(category__id = category_id, point_disponibility = True).order_by('-creation_date')
        except ObjectDoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        category_id = self.kwargs['category_id']
        try :
            cat = Category.objects.get(id = category_id)
            serializer.save()
        except ObjectDoesNotExist:
            pass
        
# Points List by Time and creation
class TimePointList(generics.ListCreateAPIView):
    search_fields = ('name', 'description')
    filter_backends = (filters.SearchFilter,)
    serializer_class = PointSerializer

    def get_queryset(self):
        time_id = self.kwargs['time_id']
        try :
            cat = Time.objects.get(id = time_id)
            return Point.objects.filter(time__id = time_id, point_disponibility = True).order_by('-creation_date')
        except ObjectDoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        time_id = self.kwargs['time_id']
        try :
            cat = Time.objects.get(id = time_id)
            serializer.save()
        except ObjectDoesNotExist:
            pass
        
# Point Detail
class PointDetail(generics.RetrieveAPIView):
    queryset = Point.objects.all().filter(point_disponibility = True).order_by('-creation_date')
    serializer_class = PointSerializer

# Comments List and Creation
class PostsList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        point_id = self.kwargs['point_id']
        try :
            cat = Point.objects.get(id = point_id)
            return Post.objects.filter(point__id = point_id).order_by('-creation_date')
        except ObjectDoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        point = point_id = self.kwargs['point_id']
        try :
            cat = Point.objects.get(id = point_id)
            serializer.save(point_id = point)
        except ObjectDoesNotExist:
            pass
