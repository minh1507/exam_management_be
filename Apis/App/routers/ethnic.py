from django.urls import include, path
from rest_framework import routers
from App.views import EthnicView

router = routers.DefaultRouter()
router.register(r'ethnic',EthnicView,basename="ethnic")

ethnicRouter = [
    path('', include(router.urls)),
]