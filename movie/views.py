from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import *


def home(request):
    movies = Movies.objects.all()
    return render(request, "index.html", {'movies':movies})