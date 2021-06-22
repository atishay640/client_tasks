from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Task(models.Model):
    TYPE_CHOICES = (
        (1, "Survey"), 
        (2, "Discussion"),
        (3, "Diary"),
    )
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES)
    user = models.ForeignKey(to=User, on_delete=CASCADE, null=False)
    tile = models.ForeignKey(to='Tile', on_delete=CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Tile(models.Model):
    STATUS_CHOICES = (
        (1, "Live"), 
        (2, "Pending"),
        (3, "Achieved"),
    )
    launch_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return str(self.id)

    def tasks(self):
        return self.task_set.all()
