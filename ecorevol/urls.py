from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('partner/', views.partner, name='partner'),
    path('profile/', views.profile, name='profile'),
    path('projects/', views.projects, name='projects'),
]

