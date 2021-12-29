from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class APIError:
    def __init__(self, error: dict, extra=None):
        self.error = error
        self.extra = extra or None
        raise ValidationError(**error)
        
        
class Errors:
    DEFAULT = {"code": -100, "detail": _("Oops!. Something went wrong, please contact us")}


