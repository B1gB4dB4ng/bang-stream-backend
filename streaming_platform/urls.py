from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # JWT authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path(
        "redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),  # API endpoints
    path("api/auth/", include("streaming_platform.apps.authentication.urls")),
    path("api/chat/", include("streaming_platform.apps.chat.urls")),
    path("api/stream/", include("streaming_platform.apps.stream.urls")),
    path("api/moderation/", include("streaming_platform.apps.moderation.urls")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
