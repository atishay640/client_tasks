from django.db import models
from django.db.models.deletion import CASCADE
import uuid


class Message(models.Model):
    message = models.TextField(null=False, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return str(self.id) + " " + self.message