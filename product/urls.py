from django.conf.urls import url
import product.views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [


    url(r'^product/(?P<category_id>\d+)/(?P<product_id>\d+)/$', product.views.product),
    
    url(r'^products_all/$', product.views.products_all),
   
    url(r'^(?P<category_id>\d+)/$', product.views.products),
   
    url(r'^supports/$', product.views.supports),
    
    url(r'^support/(?P<support_id>\d+)/$', product.views.support),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
