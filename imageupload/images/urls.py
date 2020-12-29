from django.urls import path, re_path
from . import views


app_name = 'images'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('images/', views.images, name='images'),
    path('images/<int:id>/', views.image, name='image'),
    path('image/edit/<int:id>/', views.edit, name='edit'),
    path('image/new/', views.new, name='new'),
    path('image/delete/<int:id>/', views.delete, name='delete'),
]