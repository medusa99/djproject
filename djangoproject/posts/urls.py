from django.conf.urls import url
from . import views
#we want to load an index method in the views file. we want a route for just /post (not posts/something)
# ^$ start with and end with nothing. second param looks into the views file for an index method, and then give it a name. this is
#the first route..
urlpatterns = [  
      url ( r'^$', views.index, name='index'),
      url(r'^details/(?P<id>\d+)/$', views.details, name='details')
        ];
