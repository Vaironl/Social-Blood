from django.shortcuts import render
from socialblood.models import Post
from socialblood.forms import RequestForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


# def index(request):
# 	return render(request, 'blood/post_list.html', {})
#    # return HttpResponse("<h1>Social Blood</h1>")

def index(request):
    # Queryset
    posts = Post.objects.all()
    return render(request, 'blood/post_list.html', {'posts': posts})


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('')  # return to index page
    else:
        print "INVALID LOGIN"  # PRINT TO TERMINAL
    return render(request, 'blood/login.html', {})


def register(request):
    return render(request, 'blood/register.html', {})


def add_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            newRequest = form.save(commit=True)
            print newRequest
            return HttpResponseRedirect('')
    else:
        form = RequestForm()
    return render(request, 'blood/request.html', {'form': form})
