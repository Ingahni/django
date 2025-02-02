
from django.urls import path, include
from myapp.views import comment, delete, update

article_patterns = [path('int:article_id/', include('myapp.urls')),  # Подключаем маршруты из приложения 
 = [path('<int:article_id>', include([
    path('comment/', comment, name='comment'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
]))
]
]