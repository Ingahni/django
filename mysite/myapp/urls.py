
from django.urls import path
from myapp.views import article_comment, article_delete, article_update, article_id

urlpatterns = [
    path('<int:article_id>/', article_id),
    path('<int:article_id>/comment/', comment, name='comment'),
    path('<int:article_id>/update/', article, name='update'),
    path('<int:article_id>/delete/', article, name='delete'),
]