# apps/post/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals
from apps.post.models import Post

# Create your views here.

def home_view(request):
	post_lists = Post.objects.filter(featured=True)
	# print(post_lists)
	data = {
		'post_lists':post_lists,
	}
	return render(request, 'post/index.html', data)

def blog_view(request):
	return render(request, 'post/blog.html')

def post_view(request):
	return render(request, 'post/post.html')

def contact_view(request):
	return render(request, 'post/contact.html')