from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.home_view, name=''),
    path('home/', views.home_view, name='register'),

]