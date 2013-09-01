from django.conf.urls import patterns, include, url
from django.contrib import admin
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home'),
    url(r'^blog', 'blog.views.index'),
    url(r'^blog/(?P<slug>[\w\-]+)/$', 'blog.views.post'),
)