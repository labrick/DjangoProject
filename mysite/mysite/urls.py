from django.conf.urls import patterns, include, url
from mysite.views import hello,current_time,hours_ahead
from mysite.mysql import book_list

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    #('^hello/',hello), 
    (r'^hello/$',hello),
    (r'^time/$',current_time),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    (r'^book_list/$',book_list),
    (r'^search/$','mysite.books.views.search'),
    (r'^contact/$','mysite.books.views.contact'),
)
