from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pages.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', 'events.views.home', name = 'home'),
    url(r'^landing/', 'landing.views.home', name = 'home'),
    url(r'^shippingapi/(?P<parcel>[0-9A-Z]{13})/$','shipping.views.home', name = 'home'),
    url(r'^shippingapi/', 'shipping.views.home', name = 'home'),
    url(r'^celery_test/', 'celery_test.views.start_celery_task'),
    url(r'^celery_progress/', 'celery_test.views.monitor_celery_task'),
    url(r'^weather/(?P<parm>[A-Za-z]{0,25})/$', 'weather.views.home', name = 'home'),
    url(r'^$', 'main.views.home', name = 'home'),

)
