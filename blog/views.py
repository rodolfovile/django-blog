from django.shortcuts import render
#pontinho antes do model que dizer que os arquivos model e manager estao no mesmo dir
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):


    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
