from .models import Tenant
from datetime import timedelta
from django.utils import timezone


# Cron method to reset daily counter
def reset_daily_counter():
    print({'message': 'reseting daily counter for ' + str(timezone.now() - timedelta(days=1))})
    try:
        Tenant.objects.all().update(daily_request_counter=0)
    except Exception as e:
        print({'error': str(e)})
