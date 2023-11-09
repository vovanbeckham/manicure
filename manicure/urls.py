

from django.urls import path

from manicure import views


urlpatterns = [
    path('', views.index),
    path('upload/', views.upload, name='updated'),
    
]