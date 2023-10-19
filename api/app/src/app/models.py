from django.db import models
import uuid
from django.utils import timezone


class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now())
    user_ip = models.CharField(max_length=15)
