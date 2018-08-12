from django.db import models


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.city} - ({self.code})"
