from django.urls import include, path
from rest_framework import routers
from App.views import AuthView

router = routers.DefaultRouter()
router.register(r'auth',AuthView,basename="auth")

authRouter = [
    path('', include(router.urls)),
]