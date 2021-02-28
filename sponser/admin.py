from sponser.models import Sponser
from django.contrib import admin

@admin.register(Sponser)
class SponserAdmin(admin.ModelAdmin):
    pass

