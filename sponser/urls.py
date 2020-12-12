from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sponser'
urlpatterns = [
    path('sponser_profile/', views.sponser_profile, name='sponser_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static('./static', document_root = settings.STATIC_ROOT)