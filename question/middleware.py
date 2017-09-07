from tenant.models import Tenant


# API usage middlware
class ApiUsageMiddlware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.META.get('HTTP_AUTHORIZATION'))
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    def authenticate_request(self, api_key):
        pass