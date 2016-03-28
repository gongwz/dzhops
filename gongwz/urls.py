from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gongwz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app01/', include('app01.urls')),


)
