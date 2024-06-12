from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, NewsSearch


urlpatterns = [
   path('', PostList.as_view(), name='posts'),
   path('<int:pk>/', PostDetail.as_view(), name='post'),
   path('search', NewsSearch.as_view(), name='search'),
   path('news/create/', PostCreate.as_view(), name='create'),
   path('news/<int:pk>/edit', PostUpdate.as_view(), name='edit'),
   path('news/<int:pk>/delete', PostDelete.as_view(), name='delete'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit', PostUpdate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete', PostDelete.as_view(), name='articles_delete'),

]