from django.urls import path

from .views import register_auth

urlpatterns = [
    path('register_auth/', register_auth, name='register_auth'),
]
