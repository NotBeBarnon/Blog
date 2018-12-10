from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

from backweb.models import User, Article


class LoginStatusMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('tese1 request')
        # 在访问登录注册的时候不用进行下面的登录校验（都没注册或者登录，还用判断是否登录？）
        if request.path in ['/backweb/login/', '/backweb/register/','/web/*']:
            return None

        user_id = request.session.get('user_id')   # 这句话实现了上面3个功能
        if user_id:
            user = User.objects.filter(pk=user_id).first()  # 这两句是为了在页面上展示 ：user.username
            request.user = user
            return None
        else:
            return HttpResponseRedirect('/backweb/login/')



    def process_response(self, request, response):
        print('test2 response')
        return response

class BaseStatusMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 在访问登录注册的时候不用进行下面的登录校验（都没注册或者登录，还用判断是否登录？）
        arts = Article.objects.all()
        py_count = Article.objects.filter(tag='python').count()
        web_count = Article.objects.filter(tag='前端').count()
        alg_count = Article.objects.filter(tag='算法').count()
        render(request, 'web/base_copy.html',
                      {'arts': arts, 'py_count': py_count, 'web_count': web_count, 'alg_count': alg_count})

        return None



    def process_response(self, request, response):
        print('test3 response')
        return response




