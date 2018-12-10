

from django.conf.urls import url

from backweb import views

urlpatterns = [
    url(r'^register/', views.register),
    url(r'^login/', views.login, name='login'),
    url(r'^index/', views.index),
    url(r'^add_art/', views.add_art, name='add'),
    url(r'^art_list/', views.art_list, name='art_list'),

]
