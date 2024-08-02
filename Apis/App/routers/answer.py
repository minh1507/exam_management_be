from django.urls import include, path
from rest_framework import routers
from App.views import AnswerView

router = routers.DefaultRouter()
router.register(r'answer',AnswerView,basename="answer")

answerRouter = [
    path('', include(router.urls)),
]