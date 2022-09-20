from django.urls import path
from .views import *
urlpatterns = [
    path('', FilmsView.as_view(), name='main'),
]