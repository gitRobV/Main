from django.conf.urls import url
from . import views

urlpatterns = [
    ## Index Routes
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^process_register$', views.process),
    url(r'^authenticate$', views.authenticate),
    url(r'^logout$', views.logout),
]
