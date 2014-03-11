from django.conf.urls import patterns, url

from Cafe import views

urlpatterns = patterns('',
    url(r'index', views.index, name='index'),
    url(r'menu', views.menu, name='menu'),
    url(r'signup', views.index, name='index'),
    url(r'signin', views.signin, name='signin'),
    url(r'order', views.order, name='order'),
    url(r'profile/(?P<userid>\w{0,50})/$', views.profile, name='profile'),
)