from django.urls import include, path
from rest_framework import routers
from App.views import SubjectView

router = routers.DefaultRouter()
router.register(r'subject',SubjectView,basename="subject")

subjectRouter = [
    path('', include(router.urls)),
]