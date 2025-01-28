
# Create your views here.
from django.http import HttpResponse, HttpRequest

def myfeed (request: HttpRequest) -> HttpResponse:
    return HttpResponse("страница, на которой будут только статьи по темам, на которые подписан пользователь.")