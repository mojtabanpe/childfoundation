from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sponsor'
urlpatterns = [
    path('sponsor_profile/', views.sponsor_profile, name='sponsor_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('sponsored_childs', views.sponsored_childs, name='sponsored_childs'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static('./static', document_root = settings.STATIC_ROOT)