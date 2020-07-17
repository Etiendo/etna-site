from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('language/<str:language>/', views.index, name='index'),
]
