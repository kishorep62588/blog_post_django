from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blogapp/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blogapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by= 2

class UserPostListView(ListView):
    model = Post
    template_name = 'blogapp/user_posts.html'
    context_object_name = 'posts'
    paginate_by= 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blogapp/about.html', {'title':'about'})

def search(request):
    search_key = get_object_or_404(User, username=request.GET["Search"])
    objects = Post.objects.filter(author__exact=search_key).order_by('-date')

    context = {
        "posts":objects,
        "length":objects.count(),
        "search_key":search_key
    }

    return render(request, 'blogapp/search_posts.html', context)
