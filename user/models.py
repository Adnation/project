from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=False)

    # String Override method
    def __str__(self):
        return self.name
