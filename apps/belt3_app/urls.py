from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^show$', views.show),     
    url(r'^addwish/(?P<item_id>\d+)$', views.addwish),
    url(r'^remove/(?P<item_id>\d+)$', views.remove),
    url(r'^info/(?P<item_id>\d+)$', views.info),
    url(r'^delete/(?P<item_id>\d+)$', views.delete),
            
]