from django.shortcuts import render
from socialblood.models import Post
from socialblood.forms import RequestForm, UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


# def index(request):
# 	return render(request, 'blood/index.html', {})
#    # return HttpResponse("<h1>Social Blood</h1>")

def index(request):
    # Queryset
    posts = Post.objects.all()
    return render(request, 'blood/index.html', {'posts': posts})


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponse("Your account is disabled")
        else:
            # bad login details provided
            print "Invalid login {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details provided")
    else:
        return render(request, 'blood/login.html', {})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render(request, 'blood/register.html', {'user_form': user_form, 'registered': registered})


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
