from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_email(customer_email, property_name):
    subject = 'Booking Confirmation - ALX Travel App'
    message = f'Thank you for booking with us! Your reservation for {property_name} has been confirmed.'
    from_email = 'noreply@alxtravel.com'

    return send_mail(subject, message, from_email, [customer_email])