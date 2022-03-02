from django.contrib import admin
from .models import *

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass