
# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect



def index(request):
    return HttpResponse("основная страница, на которой будет список всех статей.")
def myfeed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("страница, на которой будут только статьи по темам, на которые подписан пользователь.")
 


def article_detail(request, article_id):
    return render(request, 'article_detail.html',)

def article_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_comment.html', {'article': article})

def article_update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_update.html', {'article': article})

def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('/')  # После удаления перенаправляем на главную страницу