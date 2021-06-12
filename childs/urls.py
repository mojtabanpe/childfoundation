from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'childs'
urlpatterns = [
    path('', views.landing, name="landing"),
    path('all_news', views.all_news, name='all_news'),
    path('last_news', views.last_news, name='last_news'),
    path('news_one/<int:id>/<slug:slug>/', views.news_details, name='news_one'),
    path('sponsor_a_child', views.sponsor_a_child, name='sponsor_a_child'),
    path('donate_child/<int:child_id>', views.donate_child, name='donate_child'),
    path('child_details/<int:id>', views.child_details, name='child_details'),
    path('become_sponsor/<int:child_id>/<int:amount>', views.become_sponsor, name='become_sponsor'),
    path('donate', views.donate, name='donate'),
    path('volunteers', views.volunteers, name='volunteers'),
    path('newsandevents', views.newsandevents, name='newsandevents'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('privacy_statement', views.privacy_statement, name='privacy_statement'),
    path('terms_of_use', views.terms_of_use, name='terms_of_use'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static('./static', document_root = settings.STATIC_ROOT)