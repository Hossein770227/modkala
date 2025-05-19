from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('website.urls')),
    path('mobile/', include('mobile.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + debug_toolbar_urls()

