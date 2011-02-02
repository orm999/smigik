from django.conf.urls.defaults import *
#from mysite.vie import hello, current_datetime, hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns( 'help_info.views',
   # (r'^search-form/$', views.search_form),
   # (r'^search/$', views.search),
   #(r'^1/$', views.upload_photo),
    ( r'^$', 'albumentry' ),
 )
