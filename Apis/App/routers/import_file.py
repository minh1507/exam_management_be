from django.urls import include, path
from rest_framework import routers
from App.views import ImportView

router = routers.DefaultRouter()
router.register(r'import_file',ImportView,basename="import")

imageRouter = [
    path('', include(router.urls)),
]