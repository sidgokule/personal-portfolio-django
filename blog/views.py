from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    #blogs = Blog.objects.order_by('-date')[:5] # -date is to sort date most recent [:5] is show top 5
    blogs = Blog.objects.order_by('-date') # -date is to sort date most recent [:5] is show top 5
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #pk is Primary key, if found return object else return 404 page
    return render(request, 'blog/detail.html', {'blog':blog})
