from django.urls import path,include
from main import views
from .views import *

app_name = "main"


urlpatterns = [
    # Diller URLs
    path('diller/', views.Diller_View.as_view(), name='diller_list'),
    path('diller/<int:pk>/', views.Diller_Id.as_view(), name='diller_detail'),
    path('diller/<int:pk>/delete/', views.Diller_Delete.as_view(), name='diller_delete'),
    path('diller/<int:pk>/update/', views.Diller_Update.as_view(), name='diller_update'),
    path('diller/create/', views.Diller_Create.as_view(), name='diller_create'),

    # Product URLs
    path('product/', views.Product_View.as_view(), name='product_list'),
    path('product/<int:pk>/', views.Product_Id.as_view(), name='product_detail'),
    path('product/<int:pk>/delete/', views.Product_Delete.as_view(), name='product_delete'),
    path('product/<int:pk>/update/', views.Product_Update.as_view(), name='product_update'),
    path('product/create/', views.Product_Create.as_view(), name='product_create'),

    # User URLs
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('users/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]