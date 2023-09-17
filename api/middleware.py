from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class SuperUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith("/api/data/content/"):
            if not request.user.is_superuser:
               return HttpResponseForbidden()
