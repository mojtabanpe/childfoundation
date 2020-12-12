from django.contrib import admin
from .models import Family, House, News, Office, UserProfile, Requirements

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_editable = ('status',)
    list_display = ('title', 'writer', 'publish_date', 'status')
    list_filter = ('writer', 'status')
    search_fields = ('title', 'body')
    
    prepopulated_fields = {'slug': ('title',)}

@admin.register(UserProfile)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Family)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(House)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Requirements)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    pass