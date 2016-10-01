from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.userLogin, name='login'),
    url(r'^request/', views.add_request, name='request'),
]
