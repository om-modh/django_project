from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Elias',
        'title' : 'Blog Post 0',
        'content' : 'Zeroth Blog Content',
        'date_posted' : 'September 13, 2023',
    },
    {
        'author' : 'Harold Wren',
        'title' : 'Blog Post 1',
        'content' : 'First Blog Content',
        'date_posted' : 'September 12, 2023',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})