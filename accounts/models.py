from django.db import models
from django.contrib.auth.models import User


class UserRegister(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='user_register'
    )
    uuid = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email