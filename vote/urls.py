from django.urls import path
from . import views
app_name = 'vote'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('browse/', views.browse, name='browse'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]