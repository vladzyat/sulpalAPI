from django.db import models


class VerificationEmail(models.Model):
    email = models.EmailField()
    code = models.IntegerField()

    def __str__(self):
        return self.email
