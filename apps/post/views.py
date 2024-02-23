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

# Category count view
def get_tag_count():
	# 1. Get all the post objects
	# queryset = Post.objects.all()
	# 2. Get the tag names from the post objects
	# queryset = Post.objects.values('tags') # <-- it will return only tags fields of each post
	# 3. Count the number of times of each tag occured
	queryset = Post.objects.values('tags__title').annotate(Count('tags__title')) # <-- it will return only tags fields of each post
	return queryset

def blog_view(request):
	post_list = Post.objects.all()
	# print(post_list)
	latest_posts = Post.objects.order_by('-timestamp')[0:3]
	# print(latest_posts)
	category_count = get_category_count()
	'''
	print(category_count)
	# result
	<QuerySet [
		{'categories__title': '_Business', 'categories__title__count': 2}, 
		{'categories__title': '_Technology', 'categories__title__count': 2}, 
		{'categories__title': '_Culture', 'categories__title__count': 1}, 
		{'categories__title': '_Urban', 'categories__title__count': 3}]>
	'''
	tag_count = get_tag_count()
	'''
	# print(tag_count)
	# result
	<QuerySet [
		{'tags__title': '_AI', 'tags__title__count': 1}, 
		{'tags__title': '_walking', 'tags__title__count': 2}, 
		{'tags__title': '_Wifi', 'tags__title__count': 1}, 
		{'tags__title': '_Time', 'tags__title__count': 2}]>
		[23/Feb/2024 11:21:46] "GET /blog/ HTTP/1.1" 200 24587
	'''
	
	data = {
		'post_list':post_list,
		'latest_posts':latest_posts,
		'category_count':category_count,
		'tag_count':tag_count,
	}
	return render(request, 'post/blog.html', data)

def post_view(request):
	return render(request, 'post/post.html')

def contact_view(request):
	return render(request, 'post/contact.html')