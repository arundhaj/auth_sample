from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth_sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/login/$', 'auth_sample_app.views.login'),
    url(r'^accounts/auth/$', 'auth_sample_app.views.auth_view'),
    url(r'^accounts/logout/$', 'auth_sample_app.views.logout'),
    url(r'^accounts/loggedin/$', 'auth_sample_app.views.loggedin'),
    url(r'^accounts/invalid/$', 'auth_sample_app.views.invalid_login'),
)
