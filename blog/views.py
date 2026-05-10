from django.views.generic import (CreateView, 
                                  ListView, 
                                  DetailView, 
                                  UpdateView, 
                                  DeleteView)
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_single.html'
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'excerpt', 'body', 'photo']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
class PostNewView(CreateView):    
    template_name = 'post_new.html'
    model = Post
    success_url = reverse_lazy('home')
    form_class = PostForm