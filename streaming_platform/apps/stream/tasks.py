from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import time
import logging

logger = logging.getLogger(__name__)


@shared_task
def process_stream_data(stream_id, data):
    """
    Example background task for processing stream data.
    This demonstrates Celery functionality.
    """
    logger.info(f"Starting to process stream {stream_id}")

    # Simulate some processing time
    time.sleep(2)

    # Simulate data processing
    processed_data = {
        "stream_id": stream_id,
        "original_data": data,
        "processed_at": time.time(),
        "status": "completed",
    }

    logger.info(f"Completed processing stream {stream_id}")
    return processed_data


@shared_task
def cleanup_old_streams():
    """
    Example periodic task for cleaning up old stream data.
    This would be scheduled to run periodically.
    """
    logger.info("Starting cleanup of old streams")

    # Simulate cleanup work
    time.sleep(1)

    # Return cleanup results
    result = {"cleaned_streams": 5, "cleanup_time": time.time(), "status": "completed"}

    logger.info("Completed cleanup of old streams")
    return result


@shared_task
def send_notification_email(recipient_email, subject, message, stream_id=None):
    """
    Background task to send notification emails.
    This demonstrates integration between Celery and email functionality.
    """
    logger.info(f"Starting to send notification email to {recipient_email}")

    try:
        # Add stream context to the message if provided
        if stream_id:
            message += f"\n\nStream ID: {stream_id}\nTimestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}"

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False,
        )

        logger.info(f"Successfully sent notification email to {recipient_email}")
        return {
            "status": "success",
            "recipient": recipient_email,
            "subject": subject,
            "sent_at": time.time(),
        }

    except Exception as e:
        logger.error(f"Failed to send notification email: {str(e)}")
        return {
            "status": "failed",
            "recipient": recipient_email,
            "error": str(e),
            "failed_at": time.time(),
        }
