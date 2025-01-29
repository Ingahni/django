
from django.urls import path
from views import article_comment, article_delete, article_update, article_detail

urlpatterns = [
    path('<int:article_id>/', article_detail, name='article_detail'),
    path('<int:article_id>/comment/', article_comment, name='article_comment'),
    path('<int:article_id>/update/', article_update, name='article_update'),
    path('<int:article_id>/delete/', article_delete, name='article_delete'),
]