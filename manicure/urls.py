

from django.urls import path

from manicure import views


urlpatterns = [
    path('', views.index, name='main'),
    path('upload/', views.upload, name='updated'),
    path('add-cat/', views.add_cat, name='add_cat'),
    
    
]