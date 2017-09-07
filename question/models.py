from user.models import User
from django.db import models


# Create your models here.
class Question(models.Model):

	# Member variables
    column_title = models.CharField(max_length=2000, blank=False, unique=False)
    is_private = models.BooleanField()
    user = models.ForeignKey(User)

    # Override save method to prevent any special character from being part of question
    def save(self, *args, **kwargs):
        self.column_title = self.column_title.replace('?', '.')
        super(Question, self).save(*args, **kwargs)

    # String Override method
    def __str__(self):
        return self.column_title
