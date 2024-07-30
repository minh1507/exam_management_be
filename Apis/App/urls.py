from django.urls import path, include
from .routers import ethnicRouter, AuthRouter, roleRouter, userRouter, subjectRouter
from .swagger import swaggerRouter

urlpatterns = [
    path('apis/', include(swaggerRouter)), 
    path('api/', include(ethnicRouter+AuthRouter+roleRouter+userRouter+subjectRouter)), 
]
