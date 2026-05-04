from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class HomeView(TemplateView):
    template_name = 'home.html'
    
class NewPostView(CreateView):
    template_name = 'post_new.html'
    model = Post
    success_url = reverse_lazy('home')
    form_class = PostForm