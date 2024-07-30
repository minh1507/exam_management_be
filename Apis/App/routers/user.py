from django.urls import include, path
from rest_framework import routers
from App.views import UserView

router = routers.DefaultRouter()
router.register(r'user',UserView,basename="user")

userRouter = [
    path('', include(router.urls)),
]