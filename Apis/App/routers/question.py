from django.urls import include, path
from rest_framework import routers
from App.views import QuestionView

router = routers.DefaultRouter()
router.register(r'question',QuestionView,basename="question")

questionRouter = [
    path('', include(router.urls)),
]