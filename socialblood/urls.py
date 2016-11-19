from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.userLogin, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^request/', views.add_request, name='request'),
    url(r'^delete/(?P<pk>\d+)/$', views.RequestDelete.as_view(), name='deleterequest'),
    url(r'^userrequests/', views.UserRequestsListView.as_view(), name='userrequestlist'),
    url(r'^requestlist/', views.RequestListView.as_view(), name='requestlist'),
    url(r'^thankyou/', views.thank_you, name='thankyou'),
]
