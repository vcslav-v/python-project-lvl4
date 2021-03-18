from django.urls import path
from .views import CreateUser, UpdateUser

urlpatterns = [
    path('create/', CreateUser.as_view(), name='create'),
    path('update/', UpdateUser.as_view(), name='update'),
]
