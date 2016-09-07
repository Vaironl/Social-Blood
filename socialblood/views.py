from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Social Blood</h1>")