from django.urls import include, path
from rest_framework import routers
from App.views import RoleView

router = routers.DefaultRouter()
router.register(r'role',RoleView,basename="role")

roleRouter = [
    path('', include(router.urls)),
]