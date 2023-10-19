from django.urls import path, include
from app.controller import TestController, EventController

urlpatterns = [
    path('test/', TestController.as_view({'get': 'get_result'})),
    path('api/v1/event', TestController.as_view({'get': 'get_result'})),
]