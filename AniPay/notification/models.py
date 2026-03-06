from django.conf import settings
from django.db import models

# Create your models here.

class Notification(models.Model):
    CHANNEL_TYPE = (
    ('EMAIL', 'Email'),
    ('SMS', 'SMS')
    )

    wallet = models.CharField(max_length = 10, null = True, blank = True)
    reference = models.CharField(max_length=40, blank=True , unique=True)
    message = models.TextField()
    channel = models.CharField(max_length=10, choices=CHANNEL_TYPE, default='EMAIL')
    created_at = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=35)
    is_read = models.BooleanField(default=False)