from django.urls import path, include
from .routers import ethnicRouter, authRouter, roleRouter, userRouter, subjectRouter, questionRouter, answerRouter
from .swagger import swaggerRouter

urlpatterns = [
    path('apis/', include(swaggerRouter)), 
    path('api/', include(ethnicRouter+authRouter+roleRouter+userRouter+subjectRouter+questionRouter+answerRouter)), 
]
