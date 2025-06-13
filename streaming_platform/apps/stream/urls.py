from django.urls import path
from .views import TestCeleryView, TestEmailView

app_name = "stream"

urlpatterns = [
    path("test-celery/", TestCeleryView.as_view(), name="test-celery"),
    path("test-email/", TestEmailView.as_view(), name="test-email"),
]
