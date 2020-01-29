"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('paranuara.companies.urls', 'companies'), namespace='companies')),
    path('', include(('paranuara.citizens.urls', 'citizens'), namespace='citizens')),
    path('', include(('paranuara.foods.urls', 'foods'), namespace='foods')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
