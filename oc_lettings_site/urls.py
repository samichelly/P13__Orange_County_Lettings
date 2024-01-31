from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0


handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("sentry-debug/", trigger_error),
    path("admin/", admin.site.urls),
]
