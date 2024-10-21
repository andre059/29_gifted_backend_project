from django.urls import include, path
from rest_framework.routers import DefaultRouter
from news_app.apps import NewsAppConfig
from .views import NewsViewSet

app_name = NewsAppConfig.name
router = DefaultRouter()

router.register(
    r"", NewsViewSet,
    )


urlpatterns = [
    path("", include(router.urls)),
    
]
