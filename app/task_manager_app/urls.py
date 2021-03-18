from django.urls import path
from .views import IndexView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),  name='logout'),
]
