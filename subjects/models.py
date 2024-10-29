from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    """Subjects model."""

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Student(models.Model):

    name = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=True, default= None)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null = True)
    completed = models.BooleanField(default=False) 

    class Meta:
        unique_together = ('name', 'subject')

    def __str__(self):
        return self.name
    