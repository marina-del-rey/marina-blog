from blog.views import homepage, post, category_posts, about_me, search_results
from django.urls import path

urlpatterns = [
    path('', homepage, name='home'),
    path('posts/<str:slug>/', post, name='post'),
    path('category/<slug:slug>/', category_posts, name='category_posts'),
    path('about/', about_me, name="about"),
    path('search/', search_results, name="search"),
]

