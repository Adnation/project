from tenant.models import Tenant

# Cron method to reset daily counter
def reset_daily_counter():
	Tenant.objects.all().update(daily_request_counter=0)