from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^register$', views.register),
        # url(r'^display$', views.display),
        # url(r'^new$', views.new),
        url(r'^login$', views.login),
        # url(r'^create$', views.create),
        # url(r'^show$', views.show),
        # url(r'^join/(?P<trip_id>\d+)$', views.join),
        # url(r'^leave/(?P<trip_id>\d+)$', views.leave),
        # url(r'^info/(?P<trip_id>\d+)$', views.info),
        url(r'^logout$', views.logout)
        
]