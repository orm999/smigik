from django.conf.urls.defaults import *
from django.views.generic import list_detail

from dev_info.models import InputDev, OutputDev

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

devices_info = {
    'queryset': InputDev.objects.all(),
    'template_name': 'dev_info/base_dev_info.html',
    'template_object_name': 'input_devs',
    'extra_context': {'output_devs': OutputDev.objects.all()}
}

urlpatterns = patterns( 'dev_info.views',
    # Example:
    # (r'^smigik/', include('smigik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    ( r'^$', list_detail.object_list, devices_info ),
    ( r'^add/$', 'add' ),
    ( r'^(?P<type>(input|output))/(?P<dev_id>\d+)/edit/$', 'edit' ),
    ( r'^(?P<type>(input|output))/(?P<dev_id>\d+)/updated/$', 'updated' )
 )
