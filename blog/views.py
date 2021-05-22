from django.shortcuts import render
from django.views.generic import *
from blog.models import Post
from django.urls import reverse_lazy
# Create your views here.

class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post

class PostCV(CreateView):
    model = Post
    fields = ['title','description','image']
    template_name_suffix = '_create'
    success_url = reverse_lazy('blog')

class PostUV(UpdateView):
    model = Post
    fields = ['title','description','image']
    template_name_suffix = '_update'
    success_url = reverse_lazy('blog')

class PostRV(DeleteView):
    model = Post
    success_url = reverse_lazy('blog')