from django.shortcuts import render
from socialblood.models import Post, Request
from socialblood.forms import RequestForm, UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


# def index(request):
# 	return render(request, 'blood/index.html', {})
#    # return HttpResponse("<h1>Social Blood</h1>")

def index(request):
    # Queryset
    posts = Post.objects.all()
    return render(request, 'blood/index.html', {'posts': posts})

def thank_you(request):
    return render(request, 'blood/thank_you_request.html', {})


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
            return HttpResponse("Invalid login details provided")
    else:
        return render(request, 'blood/login.html', {})

#@login_required ensues only logged in user can see the view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/')#redirect to index
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render(request, 'blood/register.html', {'user_form': user_form, 'registered': registered})

@login_required
def add_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            # Commit=False doesn't store it in the database
            #allowing us to save the information using newRequest.save() and therefore
            #letting us set the user
            newRequest = form.save(commit=False)
            newRequest.user = request.user
            newRequest.save()
            return HttpResponseRedirect('/thankyou/')
    else:
        form = RequestForm()
    return render(request, 'blood/request.html', {'form': form})


class RequestListView(ListView):
    """Allows the user to view the blood requests made"""

    model = Request
    template_name = 'blood/requestlist.html'

    def get_context_data(self, **kwargs):
        context = super(RequestListView, self).get_context_data(**kwargs)
        return context