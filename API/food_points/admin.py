from django.contrib import admin
from .models import Category, Time, Point, Post, Publicity

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
     list_display = ['title']

class TimeAdmin(admin.ModelAdmin):
    list_display = ['hours']

class PointAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'latitude', 'longitude', 'creation_date', 'point_disponibility')
    list_filter = ('category', 'time', 'creation_date', 'update_date')
    list_editable = ['point_disponibility']
    list_per_page = 200

class PostAdmin(admin.ModelAdmin):
    list_display = ('creation_date', 'post', 'note')
    list_filter = ('creation_date', 'note', 'point')
    list_per_page = 200

class PublicityAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'pub_date', 'mod_date', 'publicity_disponibility')
    list_editable = ('url', 'publicity_disponibility')
    list_per_page = 200

admin.site.site_header = 'Foods Point Localisation - Admin Panel'
admin.site.site_title = 'Foods Point Localisation - Admin Panel'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Publicity, PublicityAdmin)
