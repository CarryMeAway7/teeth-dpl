"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from endo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/endo/', EndoAPIList.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
# import requests
# a = requests.post('http://127.0.0.1:8000/auth/token/login/', data={'username':'root','password':'1234'})
# a.json()
# {'auth_token': 'e89d7eb4eef9a28136124a9a4cd1d206ab717f52'}
# b = requests.post('http://127.0.0.1:8000/api/v1/endo/', headers={'Authorization':f'Token {a.json()["auth_token"]}'})
# b.json()
# {'name': ['Обязательное поле.']}
# b = requests.post('http://127.0.0.1:8000/api/v1/endo/', headers={'Authorization':f'Token {a.json()["auth_token"]}'}, data={'name':'anton', 'surname':'antonov','cat':3})
# b.json()
# {'name': 'aaa', 'cat_id': None}
# python requests