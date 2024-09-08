from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Gifted Hearts",
        default_version='v1',
        description="Gifted Hearts Backend API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/about-us/', include('about_us_app.urls', namespace='about-us')),
    path('api/event/', include('events_app.urls', namespace='event')),
    path('api/feedback/', include('feedback_app.urls', namespace='feedback')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/news/', include('news_app.urls', namespace='news_app')),
    path('api/project/', include('projects_app.urls', namespace='project')),
    path('api/friends/', include('friends_app.urls', namespace='friends')),
    path('api/team/', include('team.urls', namespace='team')),
    
]
if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
