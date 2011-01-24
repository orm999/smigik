from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns( 'dev_info.views',
    # Example:
    # (r'^smigik/', include('smigik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    ( r'^$', 'index', {}, 'dev_info' ),
    ( r'^add/$', 'add', {}, 'dev_info_add' ),
    ( r'^edit/$', 'edit', {}, 'dev_info_edit' ),
    ( r'^delete/$', 'delete', {}, 'dev_info_delete' ),
 )
