from django.urls import include, path
from rest_framework import routers
from App.views import ImageView

router = routers.DefaultRouter()
router.register(r'image',ImageView,basename="image")

imageRouter = [
    path('', include(router.urls)),
]