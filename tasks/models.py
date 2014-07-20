from django.db import models


class Priority(models.Model):
    name = models.CharField(max_length=50, unique=True)


class State(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    priority = models.ForeignKey('Priority')
    status = models.ForeignKey('State')
