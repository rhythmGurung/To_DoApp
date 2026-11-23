from django.contrib import admin
from django.http import FileResponse
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from todoApp.sitemap import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('todoApp.urls')),

    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        'robots.txt',lambda request: FileResponse(open('robots.txt', 'rb'), content_type='text/plain')
    ),
    path(
        'llms.txt',lambda request: FileResponse(open('llms.txt', 'rb'), content_type='text/plain')
    )
]