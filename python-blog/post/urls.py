from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'in/$', views.index, name='index'),
    url(r'in/post/(?P<pk>\d+)/$', views.post, name='post'),
]