from django.urls import path

from .views import index, hello

urlpatterns = [
    path('', index, name='home'),
    path('hello', hello, name='hello'),
]