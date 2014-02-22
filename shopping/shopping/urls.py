from django.conf.urls import patterns, include, url
from demo.views import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^api/item/$', ItemList.as_view(), name='item-list'),
    url(r'^api/item/(?P<pk>\d+)/$',ItemDetail.as_view(), name='item-detail')
)
