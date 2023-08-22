from django.urls import path, include
from src.app.controller import TestController

urlpatterns = [
    path('test/', TestController.as_view({'get': 'get_result'})),
]