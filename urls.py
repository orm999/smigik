from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = staticfiles_urlpatterns()

urlpatterns += patterns( '',
    # Example:
    # (r'^smigik2/', include('smigik2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
#    ( r'^user_info/', include( 'user_info.urls' ) ),
    ( r'^$', include( 'home.urls' ) ),
    ( r'^dev_info/', include( 'dev_info.urls' ) ),
    ( r'^img_subj/', include( 'img_subj.urls' ) ),
    ( r'^req_proc/', include( 'req_proc.urls' ) ),
    ( r'^reg_img/', include( 'reg_img.urls' ) ),
 )

#if settings.DEBUG:
#    urlpatterns += patterns( 'django.contrib.staticfiles.views',
#                            url( r'^static/(?P<path>.*)$', 'serve' ) )
