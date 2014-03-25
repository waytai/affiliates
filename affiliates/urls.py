from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from funfactory.monkeypatches import patch

import affiliates.base.views
from affiliates.base.admin import admin_site


# Apply funfactory monkeypatches.
patch()

admin.autodiscover()

# Set 404 and 500 handlers.
handler404 = affiliates.base.views.handler404
handler500 = affiliates.base.views.handler500


urlpatterns = patterns('',
    (r'', include('affiliates.base.urls')),
    (r'', include('affiliates.banners.urls')),
    (r'^fb/', include('affiliates.facebook.urls')),

    url(r'^404$', handler404, name='404'),
    url(r'^500$', handler500, name='500'),

    (r'', include('django_browserid.urls')),

    (r'^admin/', include('smuggler.urls')),
    (r'^admin/', include(admin_site.urls)),
)


# In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
