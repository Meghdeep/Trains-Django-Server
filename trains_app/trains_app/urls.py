from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # This is going to be our home view.
    # We'll uncomment it later
    # url(r'^$', 'mysite.myapp.views.home', name='home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^data/', include('data.urls')),
    url(r'^admin/', include(admin.site.urls)),
    )


#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'trains_app.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
#    url(r'^admin/', include(admin.site.urls)),
#)
