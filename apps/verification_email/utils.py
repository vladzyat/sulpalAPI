from random import randrange
from django.conf import settings
from django.core.mail import send_mail

def generate_code():
    return randrange(100000, 999999)

def send_verificatiom_code(email, code):
    subject = "Authentication code"
    message = f"Your verification code: {code}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    print(f"Code sent successfully for {email}")