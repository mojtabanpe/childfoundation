from childfoundation.admin import custom_admin_site
from childs.views import manage_admin
from django.contrib import admin
from django.db import models
from .models import Donation, Events, Family, House, News, Office, Child, Requirements, SponsoredChild
from django.conf.urls import url



class NewsAdmin(admin.ModelAdmin):
    list_editable = ('status',)
    list_display = ('title', 'writer', 'publish_date', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    
    prepopulated_fields = {'slug': ('title',)}

class ChildAdmin(admin.ModelAdmin):
    pass

class EventsAdmin(admin.ModelAdmin):
    list_editable = ('status',)
    list_display = ('title', 'writer', 'publish_date', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'body')
    
    prepopulated_fields = {'slug': ('title',)}

class FamilyAdmin(admin.ModelAdmin):
    pass

class HouseAdmin(admin.ModelAdmin):
    pass

class RequirementsAdmin(admin.ModelAdmin):
    pass

class OfficeAdmin(admin.ModelAdmin):
    pass

class DonationAdmin(admin.ModelAdmin):
    list_display = ('amount', 'email', 'date')
    search_fields = ('email',)
    list_filter = ('date',)

class SponsoredChildAdmin(admin.ModelAdmin):
    pass

custom_admin_site.register(News, NewsAdmin)
custom_admin_site.register(Events, EventsAdmin)
custom_admin_site.register(Child, ChildAdmin)
custom_admin_site.register(Family, FamilyAdmin)
custom_admin_site.register(House, HouseAdmin)
custom_admin_site.register(Requirements, RequirementsAdmin)
custom_admin_site.register(Office, OfficeAdmin)
custom_admin_site.register(Donation, DonationAdmin)
custom_admin_site.register(SponsoredChild, SponsoredChildAdmin)
