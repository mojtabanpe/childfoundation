from django.conf.urls import url
from django.contrib.admin import AdminSite
from childs.views import manage_admin
from django.contrib.auth.models import Group, User


class CustomAdminSite(AdminSite):

    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            url(r'^manage_admin', self.admin_view(manage_admin), name="manage_admin")
        ]

        return custom_urls + urls
        # urls = super(CustomAdminSite, self).get_urls()
        # custom_urls = [
        #     url(r'^manage_admin/$', self.admin_view(manage_admin), name="manage_admin"),
        # ]
        # return custom_urls + urls 

custom_admin_site = CustomAdminSite()
custom_admin_site.register(User)
custom_admin_site.register(Group)