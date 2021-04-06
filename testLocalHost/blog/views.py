# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from blog.models import *

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader, Context,RequestContext
from django.views.generic.base import TemplateView

# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()[:10]
    # {'posts': posts,'form':BlogPostForm()}是传给html的参数
    return render_to_response('archive.html', {'posts': posts,'form':BlogPostForm()}, RequestContext(request))

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')