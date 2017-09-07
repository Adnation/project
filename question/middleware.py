import json
from tenant.models import Tenant
from django.utils import timezone
from django.http import HttpResponse


# API usage middlware
class ApiUsageMiddlware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response

    # Method to handle usage limit of api ket
    def is_limit_exceeded(self, tenant):
        if tenant.daily_request_counter > 100 and \
            (timezone.now() - tenant.last_request_ts).total_seconds() < 10:
            return True
        return False


    def __call__(self, request):
        
        # Bypass middleware for admin requests
        if request.path.startswith('/admin/') or request.path == '/' :
            response = self.get_response(request)
            return response
        
        # Extract api key from request header
        api_key = request.META.get('HTTP_AUTHORIZATION')
        
        # Validate api key
        try:
            tenant = Tenant.objects.get(api_key=api_key)
        except Tenant.DoesNotExist:
            return HttpResponse(json.dumps({'error': 'Invalid API Key'}), status=401)

        # Check api usage limit
        limit_flag = self.is_limit_exceeded(tenant)

        # Reset last request timestamp
        tenant.last_request_ts = timezone.now()
        
        # Increase the daily and total counter
        tenant.daily_request_counter += 1
        tenant.total_request_counter += 1
        
        # Save the tenant object
        tenant.save()

        # Return status code 429 for if limit exceeded
        if limit_flag:
            return HttpResponse(json.dumps({'error': 'Too many requests'}), status=429)

        # Execute request
        response = self.get_response(request)

        # Return response
        return response
