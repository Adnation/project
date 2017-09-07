from django.db import models


# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=1000, blank=False, unique=False)
    api_key = models.CharField(max_length=32, blank=False, unique=True)
    last_request_ts = models.DateTimeField()
    daily_request_counter = models.IntegerField()

    def save(self, *args, **kwargs):
        self.api_key = self.api_key.lower().replace(' ', '')
        super(Tenant, self).save(*args, **kwargs)

    # String Override method
    def __str__(self):
        return self.name