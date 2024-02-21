# dreamblog/urls.py

# Django and third parties modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # blog
    path("", include("apps.blog.urls", namespace="blog")),

    # admin
    path("admin/", admin.site.urls),
]
