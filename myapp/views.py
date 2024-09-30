from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *

# Create your views here.
def blogPost(request):
    blog_post = Post.objects.all()
    post_dictionary = {'post_key': blog_post}
    return render(request, 'index.html', context=post_dictionary)