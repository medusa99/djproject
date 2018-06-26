# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.
def index(request):
#    return HttpResponse('HELLO FROM POSTS')
#so now our view should be getting posts that come from the model
#go to html index page and loop the posts
    posts = Posts.objects.all()[:10]
    context = {
      'title': 'Latest Posts',
      'posts': posts
    }
    return render(request, 'posts/index.html', context)
 #got rid of the dictionary and pased in var context.

def details(request, id):
   post = Posts.objects.get(id=id)

   context = {
     'post': post
   }
   return render(request, 'posts/details.html', context)
