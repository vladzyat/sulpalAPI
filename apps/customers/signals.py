from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def generate_qr_code(sender, instance=None, created=False, **kwargs):
    if created:
        instance.generate_qr()

