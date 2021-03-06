from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from pangolinfog.views import *
from django.contrib import admin
from django.views.generic import TemplateView
from . import views
admin.autodiscover()

urlpatterns = [

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^adminpangolin/', include(admin.site.urls)),
    url(r'jq_subsc/$', jq_subsc),
    url(r'^', include('product.urls')),
    url(r'^home/$', main),
    url(r'products/', include('product.urls')),
    url(r'support/', include('product.urls')),
    url(r'news/$',news),
    url(r'about/$',about),
    url(r'contact/$',contact),
    url(r'download/', download_file),
    url(r'download_mp3/', download_mp3),
    
    url(r'^success/$', TemplateView.as_view(template_name="success.html"), {},
        name="success"),
    

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url('', include('social.apps.django_app.urls', namespace='social')),
]


if settings.DEVELOPMENT and settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)))

if settings.DEVELOPMENT or settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}))
