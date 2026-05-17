from django.views.generic import (View,
                                  CreateView, 
                                  ListView, 
                                  DetailView, 
                                  UpdateView, 
                                  DeleteView)
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, CommentForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
    
class CommentGet(DetailView):
    model = Post
    template_name = 'post_single.html'
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context 

    
class PostDetailView(View):
    
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    
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