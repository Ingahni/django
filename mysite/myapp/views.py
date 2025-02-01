
# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect



# def index(request):
#     return HttpResponse("основная страница, на которой будет список всех статей.")
def myfeed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("страница, на которой будут только статьи по темам, на которые подписан пользователь.")
 
def create(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, на которой мы будем создавать новые статьи.")

def profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, с данными пользователя и перечнем его подписок")

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, регистрацией нового пользователя")



def article_id(request, article_id):
    return render(request, 'Cтраница, на которой будет отображаться статья по id.')

def comment(request, comment):
    return render(request, 'Адрес, который мы будем использовать для написания комментариев к статье.')

def article_update(request, article_id):
    
    return render(request, 'Страница, которую мы будем использовать для изменения существующей статьи.')

def article_delete(request, article_id):
    
    article.delete('Адрес, который мы будем использовать для удаления статьи')
    return redirect('/')  # После удаления перенаправляем на главную страницу