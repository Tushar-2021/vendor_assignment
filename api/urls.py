from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("vendor.urls")),  # Adjust the path to include your app's URL configuration
]
