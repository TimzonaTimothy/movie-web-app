from django.contrib import admin
from .models import *
# Register your models here.

class MoviesCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(MoviesCategory, MoviesCategoryAdmin)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    
admin.site.register(Movies, MoviesAdmin)