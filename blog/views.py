from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]  # Fetch all posts from the database, ordered by date in descending order
    return render(request, "blog/index.html", { # Render the index.html template and return it as a view
        "posts": latest_posts
    }) 


def posts(request):
    all_posts = Post.objects.all().order_by("-date")  # Fetch all posts from the database, ordered by date in descending order
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug): # A single post detail view
    identified_post = get_object_or_404(Post, slug=slug)  # Fetch the post with the given slug from the database
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()  # Fetch all tags associated with the post
    })