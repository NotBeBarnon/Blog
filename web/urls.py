

from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^about/', views.about),
    url(r'^gbook/', views.gbook),
    url(r'^info/', views.info),
    url(r'^info_pic/', views.info_pic),
    url(r'^list/', views.list),
    url(r'^share/', views.share),

]
