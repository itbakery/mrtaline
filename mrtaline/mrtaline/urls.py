from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from home.views import IndexView, MapView, SignUpView, LoginView, LogOutView
from home.views import ThemesView, SuccessView
from reports.models import Place
from django.conf.urls.static import static
from djgeojson.views import GeoJSONLayerView
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import permission_required

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'mrtaline.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', include('home.urls'), name='home'),
    url(r'^$', IndexView.as_view(), name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^themes$', ThemesView.as_view(), name='themes'),
    url(r'^map/$', MapView.as_view(), name='map'),
    url(r'^report/$', login_required(MapView.as_view()), name='report'),
    url(r'accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^save_issue/$', 'home.views.save_issue', name='save_issue'),
    url(r'^remove_issue/$', 'home.views.remove_issue', name='remove_issue'),
    url(r'^post_message/$', 'notes.views.post_message', name='post_message'),
    url(r'^success/$', SuccessView.as_view(), name='success_add'),
    url(r'^map/place$',
        GeoJSONLayerView.as_view(model=Place,
                                 properties=('title', 'popupContent', 'marker')),
                                 name='place'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'MRTA LINE  administration'
