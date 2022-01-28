from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

# from .views import pointSearch

app_name = "food_points"

urlpatterns = [
    path('', views.APIUrls.as_view()), # List of API's Links
    path('pub-list/', views.PubList.as_view()), # List of all publicities
    path('categories/', views.CategoriesList.as_view()), # List of all categories and category creation
    path('times/', views.TimeList.as_view()), # List of all times and time creation
    path('points/', views.PointList.as_view()), # List off all disponible points and point creation
    path('categories/<str:category_id>/', views.CategoryPointList.as_view()), # List of all disponible points by category and point creation
    path('times/<str:time_id>/', views.TimePointList.as_view()), # List of all disponible points by time and point creation
    path('points/<int:pk>/', views.PointDetail.as_view()), # Point Detail page
    path('posts/<str:point_id>/', views.PostsList.as_view()), # List of all comments by point and comment creation
]
