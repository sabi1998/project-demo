from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register/two/', views.register_two_view, name='register_two'),
    path('register/three/', views.register_three_view, name='register_three'),
    path('firstpage/', views.firstpage_view, name='firstpage'),
    path('profiles/', views.profiles_view, name='profiles'),


]
