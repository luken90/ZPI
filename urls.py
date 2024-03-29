from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',url(r'^sklep/', include('sklep.urls')),
    # Examples:
    # url(r'^$', 'zpi.views.home', name='home'),
    # url(r'^zpi/', include('zpi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
url(r'^admin/', include(admin.site.urls)),
	(r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
