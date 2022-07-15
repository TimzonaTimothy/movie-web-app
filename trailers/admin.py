from django.contrib import admin
from .models import *
# Register your models here.

class TrailerCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(TrailerCategory, TrailerCategoryAdmin)

class TrailerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    
admin.site.register(Trailer, TrailerAdmin)