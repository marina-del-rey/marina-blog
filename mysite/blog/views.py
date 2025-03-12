from django.shortcuts import render
from django.db.models import Count
from .models import Post, Category, Author
from lockdown.decorators import lockdown

# homepage view
@lockdown()
def homepage(request):
    #categories = Category.objects.all()
    categories = Category.objects.annotate(post_count = Count("post_category")).all()
    latest_posts = Post.objects.order_by('-timestamp')[0:2]
    context = {
        'categories': categories,
        'latest': latest_posts,
    }

    return render(request, 'base.html', context)


# individual posts view
@lockdown()
def post(request, slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.annotate(post_count = Count("post_category")).all()
    context = {
        'categories': categories,
        'post': post,
    }
    return render(request, 'post_full.html', context)


# posts in specific category view
@lockdown()
def category_posts(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(categories__in=[category]).order_by('timestamp')
    categories = Category.objects.annotate(post_count = Count("post_category")).all()
    context = {
        'category': category,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'category_posts.html', context)


# about me page
@lockdown()
def about_me(request):
    categories = Category.objects.annotate(post_count = Count("post_category")).all()
    users = Author.objects.first()
    context = {
        'categories': categories,
        'users': users,
    }
    return render(request, 'about_me.html', context)


# search results
@lockdown()
def search_results(request):
    query = request.GET.get('search')
    print(f"Query: {query}")
    categories = Category.objects.annotate(post_count = Count("post_category")).all()
    post_results = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    print(f"Number of posts: {post_results.count()}")
    for post in post_results:
        print(f"Title: {post.title}")
        print(f"Content: {post.content}")
    context = {
        'categories': categories,
        'query': query,
        'post_results': post_results,
    }
    return render(request, 'search.html', context)


