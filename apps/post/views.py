# apps/post/views.py

# Django and third parties modules
from django.shortcuts import render
from django.db.models import Count

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


# Category count view
def get_category_count():
	# 1. Get all the post objects
	# queryset = Post.objects.all()
	# 2. Get the category names from the post objects
	# queryset = Post.objects.values('categories') # <-- it will return only categories fields of each post
	# 3. Count the number of times of each category occured
	queryset = Post.objects.values('categories__title').annotate(Count('categories__title')) # <-- it will return only categories fields of each post
	return queryset

def blog_view(request):
	post_list = Post.objects.all()
	# print(post_list)
	latest_posts = Post.objects.order_by('-timestamp')[0:3]
	# print(latest_posts)
	category_count = get_category_count()
	print(category_count)
	data = {
		'post_list':post_list,
		'latest_posts':latest_posts,
		'category_count':category_count,
	}
	return render(request, 'post/blog.html', data)

def post_view(request):
	return render(request, 'post/post.html')

def contact_view(request):
	return render(request, 'post/contact.html')