from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/items/', views.ProductItemListView.as_view(), name='product-items'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    # path('user-list/', views.UserListView.as_view(), name='user-list'),
    # path('user/create/', views.UserCreateView.as_view(), name='user-create'),
    # path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]
