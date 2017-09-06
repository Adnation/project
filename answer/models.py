from user.models import User
from django.db import models
from question.models import Question


# Create your models here.
class Answer(models.Model):
    column_body = models.CharField(max_length=2000, blank=False, unique=False)
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)

    # String Override method
    def __str__(self):
        return self.column_body
