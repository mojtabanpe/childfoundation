from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'helpers'
urlpatterns = [
    path('send_email', views.send_email, name='send_email'),
]