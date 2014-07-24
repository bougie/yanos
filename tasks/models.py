from django.db import models
from django.contrib.auth.models import User


class Priority(models.Model):
    name = models.CharField(max_length=50)

    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('name', 'user')


class State(models.Model):
    name = models.CharField(max_length=50)

    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('name', 'user')


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    priority = models.ForeignKey(Priority)
    status = models.ForeignKey(State)
