from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters
from .serializers import PointSerializer, PublicitySerializer

from .models import Point, Publicity

# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List' : '/points-list/',
        'List By Category' : '/points-category/<str:category_id>/',
        'List By Opened Hours' : '/points-hours/<str:time_id>/',
        'List By Category and Opened Hours': '/point-cat-hours/<str:category_id>/<str:time_id>',
        'Detail View' : '/point-detail/<str:pk>/',
        'Create' : '/point-create/',
        'Update' : '/point-update/<str:pk>/',
        'Delete' : '/point-delete/<str:pk>',
        'Search' : '/points-search/',
    }

    return Response(api_urls)

@api_view(['GET'])
def pointList(request):
    points = Point.objects.filter(point_disponibility = True)
    serializer = PointSerializer(points, many = True)

    pubs = Publicity.objects.filter(publicity_disponibility = True)
    pub_serializer = PublicitySerializer(pubs, many = True)

    context = {
        'Points' : serializer.data,
        'Pubs' : pub_serializer.data,
    }
    
    return Response(context)

@api_view(['GET'])
def pointCategory(request, category_id):
    points = Point.objects.filter(point_disponibility = True, category = category_id)
    serializer = PointSerializer(points, many = True)

    pubs = Publicity.objects.filter(publicity_disponibility = True)
    pub_serializer = PublicitySerializer(pubs, many = True)

    context = {
        'Points' : serializer.data,
        'Pubs' : pub_serializer.data,
    }
    
    return Response(context)

@api_view(['GET'])
def pointHours(request, time_id):
    points = Point.objects.filter(point_disponibility = True, time = time_id)
    serializer = PointSerializer(points, many = True)

    pubs = Publicity.objects.filter(publicity_disponibility = True)
    pub_serializer = PublicitySerializer(pubs, many = True)

    context = {
        'Points' : serializer.data,
        'Pubs' : pub_serializer.data,
    }
    
    return Response(context)

@api_view(['GET'])
def pointCatHours(request, category_id, time_id):
    points = Point.objects.filter(point_disponibility = True, category = category_id, time = time_id)
    serializer = PointSerializer(points, many = True)

    pubs = Publicity.objects.filter(publicity_disponibility = True)
    pub_serializer = PublicitySerializer(pubs, many = True)

    context = {
        'Points' : serializer.data,
        'Pubs' : pub_serializer.data,
    }
    
    return Response(context)

@api_view(['GET'])
def pointDetail(request, pk):
    # point = Point.objects.get(point_disponibility = True, id = pk)
    point = get_object_or_404(Point, point_disponibility = True, id = pk)
    serializer = PointSerializer(point, many = False)

    pubs = Publicity.objects.filter(publicity_disponibility = True)
    pub_serializer = PublicitySerializer(pubs, many = True)

    context = {
        'Point' : serializer.data,
        'Pubs' : pub_serializer.data,
    }
    
    return Response(context)

@api_view(['POST'])
def pointCreate(request):
    serializer = PointSerializer(data = request.POST)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def pointUpdate(request, pk):
    point = get_object_or_404(Point, point_disponibility = True, id = pk)
    serializer = PointSerializer(instance = point, data = request.POST)

    pubs = Publicity.objects.filter(publicity_disponibility = True)
    pub_serializer = PublicitySerializer(pubs, many = True)

    if serializer.is_valid():
        serializer.save()

    context = {
        'Point' : serializer.data,
        'Pubs' : pub_serializer.data,
    }
    
    return Response(context)

@api_view(['GET'])
def pointDelete(request, pk):
    point = get_object_or_404(Point, point_disponibility = True, id = pk)
    point.point_disponibility = False

    point.save()
    
    return redirect('/food_points/points-list')

class pointSearch(generics.ListAPIView):
    queryset = Point.objects.all().filter(point_disponibility = True)
    serializer_class = PointSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name', '$description']
