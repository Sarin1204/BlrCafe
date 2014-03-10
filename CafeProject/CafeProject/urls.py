from django.conf.urls import patterns, include, url
import Cafe.views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from CafeProject import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CafeProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^Cafe/', include('Cafe.urls')),
     url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
