from sponser.models import Sponser
from django.contrib import admin
from childfoundation.admin import custom_admin_site

class SponserAdmin(admin.ModelAdmin):
    pass

custom_admin_site.register(Sponser, SponserAdmin)