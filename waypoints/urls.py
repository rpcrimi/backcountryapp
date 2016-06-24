# Import django modules
from django.conf.urls import *


urlpatterns = patterns('waypoints.views',
    url(r'^$', 'index', name='waypoints-index'),
)