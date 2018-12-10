from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from backweb.Artform import AddArtForm, RegisterForm
from backweb.models import Article, User


def register(request):
    if request.method == 'GET':
        # return HttpResponseRedirect(reverse('register'))
        return render(request, 'backweb/register.html')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            truename = form.data['truename']
            username = form.data['username']
            tel = form.data['usertel']
            password = form.data['password']
            new_password = form.data['new_password']
            if password == new_password:
                User.objects.create(truename=truename, username=username, tel=tel, password=password)
                return HttpResponseRedirect('/backweb/login/')
            else:
                return HttpResponseRedirect(reverse('backweb/register'))

        else:
            # 失败
            return render(request, 'backweb/register.html', {'form': form})



def login(request):
    if request.method == 'GET':
       return render(request, 'backweb/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')

        user = User.objects.filter(Q(username=username) | Q(tel=username)).first()
        if user:
            if user.password != password:
                err_login_pwd = '密码错误！请重新输入'
                data = {
                    'err_login_pwd': err_login_pwd
                }
                return render(request, 'backweb/login.html', data)
        else:
            err_login_pwd = '没有这个用户，请注册'
            data = {
                'err_login_pwd': err_login_pwd
            }
            return render(request, 'backweb/login.html', data)

        request.session["user_id"] = user.id    # 缓存
        res = HttpResponseRedirect('/backweb/index/')
        # 4.跳转到首页
        return res


def index(request):
    if request.method == 'GET':
        user = User.objects.filter(pk=request.session["user_id"]).first()
        return render(request, 'backweb/index.html', {'user': user})



def add_art(request):
    if request.method == 'GET':
        return render(request, 'backweb/add-article.html')

    if request.method == 'POST':
        form = AddArtForm(request.POST)

        if form.is_valid():
            # 成功
            title = form.data['title']
            keyword = form.data['keywords']
            tag = form.data['tags']
            desc = form.data['describe']
            # icon = form.cleaned_data['titlepic']
            content = form.data['content']
            Article.objects.create(title=title, keyword=keyword, tag=tag, desc=desc, content=content)

            # return HttpResponseRedirect('/articles/art/') # 方法一
            return HttpResponseRedirect(reverse('art:art_list'))     #   跳转页面  方法二

        else:
            # 失败
            return render(request, 'backweb/add-article.html', {'form': form})


def art_list(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))

        articles = Article.objects.all()
        paginator = Paginator(articles, 2)
        page = paginator.page(page)
        return render(request, 'backweb/article.html', {'page': page})