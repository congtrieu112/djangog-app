from django.contrib import admin
from django_use_email_as_username.admin import BaseUserAdmin

from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(User, BaseUserAdmin)
