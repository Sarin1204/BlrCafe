from django.conf.urls import patterns, url

from Cafe import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'menu', views.menu, name='menu'),
    url(r'signup', views.index, name='index'),
    url(r'signin', views.signin, name='signin')
)