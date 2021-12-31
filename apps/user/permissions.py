from rest_framework.permissions import BasePermission
from django.utils.translation import ugettext_lazy as _
from .models import *

class UserAccountAccess(BasePermission):
    message = _("You don't have access to this account")

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True
