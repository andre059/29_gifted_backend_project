from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contacts.apps import ContactsConfig
from .views import ContactPageViewSet

app_name = ContactsConfig.name
router = DefaultRouter()

router.register(r"", ContactPageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
