from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('music_app.views',
	url(r'^music_app/$', 'index'),
	url(r'^music_app/improvisation/$', 'improvisation'),
	url(r'^music_app/counterpoint$', 'counterpoint'),
	url(r'^music_app/orchestration$', 'orchestration'),
	url(r'^music_app/documentation$', 'documentation'),
    #url(r'^music_app/contact/$', 'contact'),
    
    # Examples:
    # url(r'^$', 'music_app_site.views.home', name='home'),
    # url(r'^music_app_site/', include('music_app_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
