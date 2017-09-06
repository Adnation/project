from django.db import models


# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=1000, blank=False, unique=False)
    api_key = models.CharField(max_length=32, blank=False, unique=True)

    # String Override method
    def __str__(self):
        return self.name