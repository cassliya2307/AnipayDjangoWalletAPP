from django.conf import settings
from django.db import models

# Create your models here.

class Notification(models.Model):
    CHANNEL_TYPE = (
    ('EMAIL', 'Email'),
    ('SMS', 'SMS')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    reference = models.CharField(max_length=40, blank=True , unique=True)
    message = models.TextField()
    channel = models.CharField(max_length=10, choices=CHANNEL_TYPE, default='EMAIL')
    created_at = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=35)