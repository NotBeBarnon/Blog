

from django.shortcuts import render

# Create your views here.
from backweb.models import Article


def index(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        return render(request, 'web/index.html', {'arts': arts})


def about(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')


def gbook(request):
    if request.method == 'GET':
        return render(request, 'web/gbook.html')


def info(request):
    if request.method == 'GET':
        return render(request, 'web/info.html')


def info_pic(request):
    if request.method == 'GET':
        return render(request, 'web/infopic.html')


def list(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        py_count = Article.objects.filter(tag='python').count()
        web_count = Article.objects.filter(tag='前端').count()
        alg_count = Article.objects.filter(tag='算法').count()
        return render(request, 'web/list.html', {'arts': arts, 'py_count': py_count, 'web_count': web_count, 'alg_count':alg_count})


def share(request):
    if request.method == 'GET':
        return render(request, 'share.html')