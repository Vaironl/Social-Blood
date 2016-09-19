from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import UserForm, UserProfileForm

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.set_password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['pictures']

				profile.save()
				registered = True
			else:
				print user_form.errors, profile_form.errors
		else:
			user_form = UserForm()
			profile_form = UserProfileForm()

	return render(request, './templates/blog/register.html',
	 {'user_form': user_form,
	  'profile_form':profile_form,
	  'registered':registered})


# def index(request):
# 	return render(request, 'blog/post_list.html', {})
#    # return HttpResponse("<h1>Social Blood</h1>")

def index(request):
	# Queryset
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def register(request):
	return render(request, 'blog/register.html', {})