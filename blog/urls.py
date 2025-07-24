from django.urls import path

from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),  # / (home page)
    path("posts", views.AllPostView.as_view(), name="posts-page"),  # /posts (list of all posts)
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page") # /posts/my-first-post (search engine friendly identifier)
]