from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from io import BytesIO
import qrcode
from PIL import Image
from django.core.files import File

class CustomUserManager(BaseUserManager):
    def create(self, **extra_fields):
        return self.create_user(**extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be provided!')
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(**extra_fields)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15, unique=True)
    qr_code = models.ImageField(upload_to='qr_customers/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"

    def generate_qr(self):
        qrcode_image = qrcode.make('{"user_id": "%s"}' % self.pk)
        canvas = Image.new('RGB', (330, 330), 'white')
        canvas.paste(qrcode_image)
        file_name = f"qr_code-{self.username}.png"
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(file_name, File(buffer))
        canvas.close()
        super().save()
