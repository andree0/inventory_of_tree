from allauth.socialaccount.models import SocialApp

from django.contrib import admin

@admin.register(SocialApp)
class SocialAppAdmin(admin.ModelAdmin):
    pass