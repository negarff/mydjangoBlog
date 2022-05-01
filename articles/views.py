from django.shortcuts import render , HttpResponse
from . import models

# Create your views here.
def articles_list(request):
    articles = models.Articles.objects.all().order_by('date')

    return render(request, 'articles/articleslist.html', {'articles':articles})

def articles_detail (request , slug):
    return HttpResponse(slug)
