from django import views
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url 
from django.views.static import serve
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('sign_in/', signin, name='sign_in'),
    path('signin/', signin, name='sign_in'),
    path('login/', signin, name='login'),

    
    path('profile/', profile, name='profile'),
    path('logout/<int:id>/', log_out, name='logout'),
    path('movies/', movies_list),
    path('movies/<int:pk>/',movie_detial),
    path('movies_category/',movies_category_list),
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
