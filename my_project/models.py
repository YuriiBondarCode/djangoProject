from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Thread(models.Model):

    participants = models.JSONField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, default=None)

    def clean(self):
        if not isinstance(self.participants, list):
            raise ValidationError("Participants must be a list.")
        if len(self.participants) != 2:
            raise ValidationError("A thread must have exactly 2 participants.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Runs clean() before saving
        super().save(*args, **kwargs)

class Message(models.Model):
    sender = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    thread = models.ForeignKey("Thread", on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField()