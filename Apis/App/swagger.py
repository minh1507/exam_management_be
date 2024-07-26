from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import environ
env = environ.Env()
environ.Env.read_env()

schema_view = get_schema_view(
    openapi.Info(
        title=env("SWAGGER_TITLE"),
        default_version=env("SWAGGER_VERSION"),
    ),
    public=True,
)

swaggerRouter = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
