from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, 'blog/post_list.html', {})
#    return HttpResponse("<h1>Social Blood</h1>")
