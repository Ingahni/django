
from django.urls import include, path
from myapp.views import article_comment, article_delete, article_update
from . import views

article_urlpatterns =  [path('<int:article_id>', include([
    path('comment', article_comment, name='article_comment'),
    path('update', article_update, name='update'),
    path('delete', article_delete, name='delete'),
])),
]
