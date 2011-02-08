from django.conf.urls.defaults import *
#from mysite.vie import hello, current_datetime, hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('reg_img.views',
   # (r'^search-form/$', views.search_form),
   # (r'^search/$', views.search),
   #(r'^1/$', views.upload_photo),
    (r'^$', 'valid', {}, 'reg_img_index'),
    (r'^add_inf/$', 'albumentry', {}, 'reg_img_add_inf'),
    (r'^ph_add_inf/$', 'ph_add', {}, 'reg_img_ph_add_inf'),
   # (r'^hello/$', hello),
   # (r'^time/$', current_datetime),
   # (r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
