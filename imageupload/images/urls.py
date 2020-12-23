from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='images_index'),
    path('int/<int:br>', views.broj, name='images_broj'),
    path('int/', views.broj, name='images_broj'),
    path('rec/<str:str>', views.rec, name='images_rec'),
    path('params/', views.params, name='images_params'),
    path('hello/', views.hello, name='images_hello'),
    re_path(r'^regex/(?:godina-(?P<godina>[0-9]{4}))/(?:mesec-(?P<mesec>[0-9]{2}))', views.regex, name='images_regex'),
]