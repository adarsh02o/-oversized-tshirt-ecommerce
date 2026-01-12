from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
