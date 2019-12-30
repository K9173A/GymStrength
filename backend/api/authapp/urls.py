"""
Module for authapp URLs.
"""
from django.urls import path, include

import api.authapp.views as authapp_api


app_name = 'authapp'

urlpatterns = [
    path('jwt/create/', authapp_api.login),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
]
