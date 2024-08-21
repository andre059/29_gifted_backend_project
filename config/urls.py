from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/about-us/', include('about_us_app.urls', namespace='about-us')),
    path('api/event/', include('events_app.urls', namespace='event')),
]
