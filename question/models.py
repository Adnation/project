from user.models import User
from django.db import models


# Create your models here.
class Question(models.Model):
    column_title = models.CharField(max_length=2000, blank=False, unique=False)
    is_private = models.BooleanField()
    user = models.ForeignKey(User)

    # String Override method
    def __str__(self):
        return self.column_title
