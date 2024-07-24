from django.urls import path, include
from .routers.ethnic import ethnicRouter
from .swagger import swaggerRouter

urlpatterns = [
    path('apis/', include(swaggerRouter)), 
    path('api/', include(ethnicRouter)), 
]
