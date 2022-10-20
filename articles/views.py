from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles

# Create your views here.

def home(request):
 articles = Articles.objects
 return render(request, 'articles/article.html', {'articles': articles})

def detail(request, articles_id):
 article = get_object_or_404(Articles, pk=articles_id)
 return render(request, 'articles/detail.html', {'article': article})