from django.urls import include, path
from rest_framework import routers
from App.views import ExamView

router = routers.DefaultRouter()
router.register(r'exam',ExamView,basename="exam")

examRouter = [
    path('', include(router.urls)),
]