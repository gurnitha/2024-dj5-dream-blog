# apps/blog/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from apps.blog import views

# namespace
app_name = 'blog'

# urlpatterns
urlpatterns = [
    path("", views.home_view, name="home_view"),
]