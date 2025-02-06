
# Create your views here.
from django.http import HttpResponse, HttpRequest


def myfeed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("страница, на которой будут только статьи по темам, на которые подписан пользователь.")
 
def create(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, на которой мы будем создавать новые статьи.")

def profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, с данными пользователя и перечнем его подписок")

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, регистрацией нового пользователя")

def article_id(request: HttpRequest ):
    return HttpResponse(request, 'Cтраница, на которой будет отображаться статья по id.')

def article_comment(request: HttpRequest, article_id):
    return HttpResponse(request, 'Адрес, который мы будем использовать для написания комментариев к статье. {article_id}')

def article_update(request: HttpRequest):
    return HttpResponse(request, 'Страница, которую мы будем использовать для изменения существующей статьи.')

def article_delete(request: HttpRequest):
    return HttpResponse('Адрес, который мы будем использовать для удаления статьи')

def topics(request: HttpRequest):
    return HttpResponse('Страница, с перечнем всех тем на сайте')

#def topics(request: HttpRequest):
#  /topics/<topic_id>/ - Страница, со всеми статьями по определенной теме

#def topics(request: HttpRequest):
#  /topics/<topic_id>/subscribe/ - Адрес для подписки на конкретную тему

#def topics(request: HttpRequest):
#  /topics/<topic_id>/unsubscribe/ - Адрес для отписки от конкретной темы

def profile (request: HttpRequest):
   return HttpResponse('Страница, с данными пользователя и перечнем его подписок')

def register(request: HttpRequest):
    return HttpResponse ('Страница, регистрацией нового пользователя')

# def set=pasword(request: HttpRequest):
#     return HttpResponse ('Страница, с изменением пароля')

def login(request: HttpRequest):
    return HttpResponse ('Страница, для входа на сайт')

def logout(request: HttpRequest):
    return HttpResponse ('Адрес для выхода с сайта')

# def topics(request: HttpRequest):
# /<int:year>/<int:month>/ - страница, на которой будут статьи созданные в конкретный месяц. В случае запроса не настоящей даты, должна быть ошибка.