from django.db import models


class Subject(models.Model):
    """Subjects model."""

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
