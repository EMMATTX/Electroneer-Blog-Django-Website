from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def post(request, slug=None):

    item = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post.html', {'item': item, 'title': item,})
