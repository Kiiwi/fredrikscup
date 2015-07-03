# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home', name='home'),
    url(r'^takk/$', 'website.views.thanks', name='thanks'),
    #(r'^takk/$', TemplateView.as_view(template_name='takk.html')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #(r'^$', TemplateView.as_view(template_name="index.html")),
)