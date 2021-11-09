from django.urls import path
from . import views

from .views import pointSearch

app_name = "food_points"

urlpatterns = [
    path('', views.apiOverview, name = "api-overview"),
    path('points-list/', views.pointList, name = "points-list"),
    path('points-category/<str:category_id>/', views.pointCategory, name = "points-category"),
    path('points-hours/<str:time_id>/', views.pointHours, name = "points-hours"),
    path('points-cat-hours/<str:category_id>/<str:time_id>/', views.pointCatHours, name = "points-cat-hours"),
    path('point-detail/<str:pk>/', views.pointDetail, name = "point-detail"),
    path('point-create/', views.pointCreate, name = "point-create"),
    path('point-update/<str:pk>/', views.pointUpdate, name = "point-update"),
    path('point-delete/<str:pk>/', views.pointDelete, name = "point-delete"),
    path('points-search/', pointSearch.as_view(), name = "points-search"),
]
