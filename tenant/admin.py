from django.contrib import admin

# Register your models here.
from tenant.models import Tenant

admin.site.register(Tenant)