from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CafeProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^Cafe/', include('Cafe.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
