from django.shortcuts import render
from .models import Post
from django.utils import timezone


# def index(request):
# 	return render(request, 'blog/post_list.html', {})
#    # return HttpResponse("<h1>Social Blood</h1>")

def index(request):
	# Queryset
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def register(request):
	return render(request, 'blog/register.html', {})