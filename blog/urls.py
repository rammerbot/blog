"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import EntrySitemap, Sitemap

urlpatterns_main = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('', include('applications.entrada.urls')),
    path('', include('applications.favoritos.urls')),
    path('', include('applications.users.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))
]

sitemaps = {
    'site':Sitemap(
        [
            'home_app:index'
        ]
    ),
    'entradas': EntrySitemap
}

urlpatterns_sitemap = [
    path('sitemap.xml/', sitemap,{'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
