from django.shortcuts import render
from . import models

def post_view(request):
    if request.method == "GET":
        data = models.Post.objects.all()
        return render(request, 'post.html', {'post_key': data})
