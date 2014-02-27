from django.conf import settings

from django.conf.urls import patterns, include, url

from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hgp_2.views.home', name='home'),
    # url(r'^hgp_2/', include('hgp_2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'gallery.views.index'),
    url(r'^about$', 'gallery.views.about'),
    url(r'^album/([a-z|-]+)$', 'gallery.views.for_album'),
    url(r'^album/([a-z|-]+)/(\d+)$', 'gallery.views.for_album'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
