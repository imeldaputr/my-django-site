from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm

# Create your views here.

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]  # Fetch all posts from the database, ordered by date in descending order
#     return render(request, "blog/index.html", { # Render the index.html template and return it as a view
#         "posts": latest_posts
#     })    
class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]  # order posts by date in descending order
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset() # fetch all posts
        data = queryset[:3]
        return data



# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")  # Fetch all posts from the database, ordered by date in descending order
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })
class AllPostView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    ordering = ["-date"]  # Order posts by date in descending order
    context_object_name = "all_posts"



# def post_detail(request, slug): # A single post detail view
#     identified_post = get_object_or_404(Post, slug=slug)  # Fetch the post with the given slug from the database
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()  # Fetch all tags associated with the post
#     })
class SinglePostView(View):    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  # Create a comment instance but don't save it to the database yet
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)