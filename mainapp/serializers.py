from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError

from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'name', 'description', 'categories')


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description', 'categories', 'image')


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductItem
        fields = ('url', 'size', 'qty', 'price', 'product')


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Product
        fields = ( 'title', 'slug')


# class UserSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'cart')


# class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
#     email = serializers.EmailField(required= True, validators = [UniqueValidator(queryset = User.objects.all())])
#     password1 = serializers.CharField(max_length = 8, write_only = True, label = 'Password', style = {'input_type': 'password'})
#     password2 = serializers.CharField(max_length = 8, write_only = True, label = 'Confirm Password', style = {'input_type' : 'password'} )

#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'password1', 'password2')

#     def create(request, validated_data):
#         username = validated_data['username']
#         email = validated_data['email']
#         password1 = validated_data['password1']
#         user = User(username = username, email = email)
#         if password1 != validated_data['password2']:
#             return ValidationError('passwords do not match')
#         else:
#             user.set_password(password1)
#             user.save()
#         return user
#         fields = ('url', 'username', 'email', 'cart')