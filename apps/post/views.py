# apps/post/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals
from apps.post.models import Post

# Create your views here.

def home_view(request):
	featured_posts = Post.objects.filter(featured=True).order_by('-timestamp')[0:3]
	# print(post_lists)
	latest_posts = Post.objects.order_by('-timestamp')[0:3]
	# print(latest_posts)
	data = {
		'featured_posts':featured_posts,
		'latest_posts':latest_posts,
	}
	return render(request, 'post/index.html', data)

def blog_view(request):
	post_list = Post.objects.all()
	# print(post_list)
	latest_posts = Post.objects.order_by('-timestamp')[0:3]
	# print(latest_posts)
	data = {
		'post_list':post_list,
		'latest_posts':latest_posts,
	}
	return render(request, 'post/blog.html', data)

def post_view(request):
	return render(request, 'post/post.html')

def contact_view(request):
	return render(request, 'post/contact.html')