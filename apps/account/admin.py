from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from core.admin import BaseAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseAdmin):
    pass
