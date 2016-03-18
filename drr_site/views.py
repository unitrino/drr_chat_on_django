from os import listdir

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render, redirect


chat_body = [["../system.jpg","System", "Start chat"]]

def index(request):
    if request.GET:
        return render(request,'html/index.html',{'err_no': ''})
    elif request.POST:
        if request.POST["password"] != "drrr":
            return render(request,'html/index.html',{'err_no': "Invalid password"})
        else:
            #REDIRECT
            print "REDIRECT"
            return HttpResponseRedirect(reverse('avatar_and_nickname'))
    else:
        return render(request,'html/index.html',{'err_no': ''})


def avatars_and_nickname(request):
    list_of_avatars = listdir("./static/images/avatars")
    size_col = 3
    out_list_of_avatars = [[]]
    j = 0
    for i in range(len(list_of_avatars)):
        if i % size_col == 0 and i != 0:
            j += 1
            out_list_of_avatars.append([list_of_avatars[i]])
        else:
            out_list_of_avatars[j].append(list_of_avatars[i])
    print out_list_of_avatars

    if request.GET:
        print "GET"
        return render(request,'html/check_avatar_and_nickname.html', {'avatars_rows': out_list_of_avatars, 'errors': ''})
    elif request.POST:
        print "POST"
        avatar = request.POST["avatar"]
        nickname = request.POST["nickname"]
        err = []

        if avatar == "":
            err.append("Avatar is missing")
        if nickname == "":
            err.append("Nickname is missing")

        if err:
            return render(request,'html/check_avatar_and_nickname.html', {'avatars_rows': out_list_of_avatars, 'errors': err,'person_name': nickname,'person_avatar': avatar })
        else:
            resp = HttpResponseRedirect(reverse('chat'))
            resp.set_cookie('nickname', nickname)
            resp.set_cookie('avatar', avatar)
            return resp
    else:
        print "ELSE"
        return render(request,'html/check_avatar_and_nickname.html', {'avatars_rows': out_list_of_avatars, 'errors': ''})


def chat(request):
    if request.GET:
        return render(request,'html/chat.html', {'text_to_chat': chat_body})
    elif request.POST:
        nick = request.COOKIES['nickname']
        ava = request.COOKIES['avatar']
        texxt = request.POST['text_to_send']
        chat_body.insert(0,[ava,nick,texxt])
        return render(request,'html/chat.html', {'text_to_chat': chat_body})
    else:
         return render(request,'html/chat.html', {'text_to_chat': chat_body})


def chat_load(request):
    return render(request, 'html/new_chat.html', {'text_to_chat': chat_body})


