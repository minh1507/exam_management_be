from django.urls import include, path
from rest_framework import routers
from App.views import ExamView

router = routers.DefaultRouter()
router.register(r'user',ExamView,basename="exam")

userRouter = [
    path('', include(router.urls)),
]