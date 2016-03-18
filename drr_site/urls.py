
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^prepare/$', views.avatars_and_nickname,name="avatar_and_nickname"),
    url(r'^chat/$', views.chat,name="chat"),
    url(r'^chat_load/$', views.chat_load),
]
