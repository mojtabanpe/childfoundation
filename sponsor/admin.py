from sponsor.models import Sponsor
from django.contrib import admin
from childfoundation.admin import custom_admin_site

class SponsorAdmin(admin.ModelAdmin):
    pass

custom_admin_site.register(Sponsor, SponsorAdmin)