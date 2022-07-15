from dataclasses import fields
from pkgutil import extend_path
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes

from accounts.models import *
from movies.models import *
from payments.models import *
from seasonals.models import *
from trailers.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
            
        instance.save()
        return instance

    class Meta:
        model = Account
        extra_kwargs = {'password': {'write_only':True}}
        fields = ('first_name','last_name','password','email','phone','profile_picture','city','state','country')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name','last_name','password','email','phone','profile_picture','city','state','country')


class MoviesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesCategory
        fields = ['category_name', 'slug','description', 'cat_image',]
    


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['title', 'slug','category','description', 'video', 'created_at']
    
    
