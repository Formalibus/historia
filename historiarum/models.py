from django.db import models
from django.contrib.auth.models import User


class Fabula(models.Model):
    titulus = models.CharField(max_length=255)
    contentus = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulus
