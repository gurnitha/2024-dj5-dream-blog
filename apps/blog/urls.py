# apps/blog/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from apps.blog import views

# namespace
app_name = 'blog'

# urlpatterns
# urlpatterns = [
#     path("", views.home_view, name="home_view"),
#     path("blog/", views.blog_view, name="blog_view"),
#     path("post/", views.post_view, name="post_view"),
#     path("contact/", views.contact_view, name="contact_view"),
# ]