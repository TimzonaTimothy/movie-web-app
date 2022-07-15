from django.contrib import admin
from .models import *
# Register your models here.

class SeasonalCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(SeasonalCategory, SeasonalCategoryAdmin)


class SeasonalVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
admin.site.register(Episode, SeasonalVideoAdmin)



class SeasonalInline(admin.TabularInline):
    model = Episode
    extra = 1

class SeasonalAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    inlines = [SeasonalInline]
    
admin.site.register(Seasonal, SeasonalAdmin)