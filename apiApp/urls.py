from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.khatam),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^register/', views.register),
    url(r'^movie/(?P<movieid>\d+)/$', views.movie),
    url(r'^tv/(?P<tvid>\d+)/$', views.tv),
    url(r'^search/', views.search),
]
