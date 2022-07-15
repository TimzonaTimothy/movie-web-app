from django.shortcuts import render
from .models import *

# Create your views here.

def movie(request):
    movie = Movies.objects.all()
    return render(request, 'movie-details.html',{'movie':movie})
