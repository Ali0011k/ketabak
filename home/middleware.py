from django.utils.translation import activate
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class AdminLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith("/admin/"):
            if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
                activate('fa')
                translation.activate('fa')
