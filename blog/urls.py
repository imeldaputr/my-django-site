from django.urls import path

from . import views


urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # / (home page)
    path("posts", views.posts, name="posts-page"),  # /posts (list of all posts)
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page") # /posts/my-first-post (search engine friendly identifier)
]