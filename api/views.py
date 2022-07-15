from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from accounts.models import *
from .serializers import *
from rest_framework.parsers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
import random
from django.contrib.auth import login, logout
import re
# Create your views here.

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters only'})

    username = request.POST['email']
    password = request.POST['password']

    if len(password) < 3:
        return JsonResponse({'error': ' Password needs to be at least 3'})

    userModel = get_user_model()

    try:
        user = userModel.objects.get(email=username)
        if user.check_password(password):
            user_dict = userModel.objects.filter(email=username).values().first()
            user_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'Previous session exists!'})
            
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token':token, 'user':user_dict})
        else:
            return JsonResponse({'error':'Invalid Password'})

    except userModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = Account.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@api_view(['POST','PUT'])
def profile(request):
    profile_picture = request.data.get('file', None)
    if profile_picture:
        prp = Account.objects.filter(user=request.user)
        prp.profile_picture = profile_picture
        prp.save
        return Response({'message':'received'}, status=200)

@api_view(['GET'])
def log_out(request, id):
    logout(request)

    
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid User ID'})

    return JsonResponse({'success':'Logout Success'})


@api_view(['GET'])
def movies_category_list(request):

    if request.method == 'GET':
        movies = MoviesCategory.objects.all()
        serializer = MoviesCategorySerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def movies_list(request):

    if request.method == 'GET':
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
@csrf_exempt
def movie_detial(request, pk):
    try:
        movie = Movies.objects.get(pk=pk)

    except Movies.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MoviesSerializer(movie)
        return JsonResponse(serializer.data)

    