from django.conf.urls import patterns, url
from views import BlogListing, BlogCreate, BlogDetail, BlogUpdate, BlogDelete

urlpatterns = patterns(
    '',
    url(r'^$', BlogListing.as_view(), name='listing'),
    url(r'create/$', BlogCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', BlogUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', BlogDelete.as_view(), name='delete'),
)
