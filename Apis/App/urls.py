from django.urls import path, include
from .routers import ethnicRouter
from .swagger import swaggerRouter

urlpatterns = [
    path('apis/', include(swaggerRouter)), 
    path('api/', include(ethnicRouter)), 
]
