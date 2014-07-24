from django.db import models
from django.contrib.auth.models import User


class Priority(models.Model):
    name = models.CharField(max_length=50, unique=True)

    user = models.ForeignKey(User)


class State(models.Model):
    name = models.CharField(max_length=50, unique=True)

    user = models.ForeignKey(User)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    priority = models.ForeignKey(Priority)
    status = models.ForeignKey(State)
