from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.userLogin, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^request/', views.add_request, name='request'),
    url(r'^requestlist/', views.RequestListView.as_view(), name='requestlist'),
    url(r'^thankyou/', views.thank_you, name='thankyou'),
]
