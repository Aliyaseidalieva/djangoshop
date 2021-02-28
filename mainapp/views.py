from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import *
from .models import *


class CategoryListView(generics.ListAPIView):
    """Вывод категорий товаров"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(generics.ListAPIView):
    """Вывод списка товаров"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    """Вывод товара"""
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductCreateView(generics.CreateAPIView):
    """ Создание товара"""
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ProductItemListView(generics.ListAPIView):
    """Позиции товаров"""
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


# class UserListView(generics.ListAPIView):
#     """Cписок пользователей"""
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return User.objects.filter(username = user)


# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """Пользователь детально"""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserCreateView(generics.CreateAPIView):
#     """Создание пользователей"""
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer

#     def perform_create(self, serializer):
#         cart = Cart.objects.get_or_new(self.request)
#         user = serializer.save()
#         cart.user = user
#         cart.save()
