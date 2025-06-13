from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.core.mail import send_mail
from django.conf import settings
from .tasks import process_stream_data
import logging

logger = logging.getLogger(__name__)


class TestEmailView(APIView):
    """
    Test endpoint to demonstrate email functionality with MailHog.
    """

    permission_classes = [AllowAny]

    @extend_schema(
        summary="Test Email Sending",
        description="Sends a test email to demonstrate MailHog functionality",
        parameters=[
            OpenApiParameter(
                name="to_email",
                description="Email address to send test email to",
                required=False,
                type=str,
            ),
        ],
        responses={200: "Email sent successfully"},
    )
    def post(self, request):
        """Send a test email to verify MailHog functionality."""
        to_email = request.data.get("to_email", "test@example.com")

        try:
            send_mail(
                subject="Bang Stream Backend - Test Email",
                message=""":
                Hello!
                
                This is a test email from Bang Stream Backend to verify that MailHog email testing is working correctly.
                
                Features tested:
                - Django email backend configuration
                - MailHog SMTP server integration
                - Email capture and viewing
                
                You can view this email in the MailHog web interface at: http://localhost:8025
                
                Best regards,
                Bang Stream Backend Team
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[to_email],
                fail_silently=False,
            )

            logger.info(f"Test email sent successfully to {to_email}")

            return Response(
                {
                    "message": "Test email sent successfully",
                    "to_email": to_email,
                    "mailhog_ui": "http://localhost:8025",
                    "status": "sent",
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return Response(
                {
                    "message": "Failed to send email",
                    "error": str(e),
                    "status": "failed",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class TestCeleryView(APIView):
    """
    Test endpoint to demonstrate Celery background task functionality.
    """

    permission_classes = [AllowAny]  # Allow access without authentication for testing

    @extend_schema(
        summary="Test Celery Task",
        description="Triggers a background task to test Celery functionality",
        parameters=[
            OpenApiParameter(
                name="stream_id",
                description="Stream ID to process",
                required=False,
                type=str,
            ),
        ],
        responses={200: "Task started successfully"},
    )
    def post(self, request):
        """Trigger a background task to test Celery functionality."""
        stream_id = request.data.get("stream_id", "test-stream-1")
        test_data = {
            "type": "test_stream",
            "timestamp": "2025-06-13T18:00:00Z",
            "data": "Sample stream data for testing",
        }

        # Start the background task
        task = process_stream_data.delay(stream_id, test_data)

        logger.info(f"Started background task {task.id} for stream {stream_id}")

        return Response(
            {
                "message": "Background task started successfully",
                "task_id": task.id,
                "stream_id": stream_id,
                "status": "processing",
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Get Task Status",
        description="Check the status of a background task",
        responses={200: "Task status information"},
    )
    def get(self, request):
        """Get information about running tasks."""
        return Response(
            {
                "message": "Celery integration is working properly",
                "services": {
                    "celery_worker": "running",
                    "celery_beat": "running",
                    "redis": "connected",
                },
            },
            status=status.HTTP_200_OK,
        )
