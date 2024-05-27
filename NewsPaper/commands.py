from news.models import Author, Category, Post, PostCategory, Comment, User

# Создание двух пользователей
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

# Создание объектов модели Author, связанных с пользователями
author1 = Author.objects.create(user=user1, rating=0)
author2 = Author.objects.create(user=user2, rating=0)

# Добавление 4 категорий
Category.objects.create(name='Спорт')
Category.objects.create(name='Космос')
Category.objects.create(name='Гороскоп')
Category.objects.create(name='Искусство')

# Создание 2 статей и 1 новости
post1 = Post.objects.create(author=author1, post_type='article', title='Статья 1', content='Тестовая версия статьи 1', rating=0)
post2 = Post.objects.create(author=author1, post_type='article', title='Статья 2', content='Тестовая версия статьи 2', rating=0)
post3 = Post.objects.create(author=author2, post_type='news', title='Новость 1', content='Текст новости 1', rating=0)

# Присвоение категорий статьям/новости
post1.categories.add(Category.objects.get(name='Спорт'))
post2.categories.add(Category.objects.get(name='Космос'))
post3.categories.add(Category.objects.get(name='Искусство'))

# Создание комментариев
comment1 = Comment.objects.create(post=post1, user=user1, text='Отличная статья!', rating=0)
comment2 = Comment.objects.create(post=post2, user=user2, text='Интересная новость!', rating=0)
comment3 = Comment.objects.create(post=post1, user=user1, text='Выглядит потрясающе!', rating=0)
comment4 = Comment.objects.create(post=post2, user=user2, text='Супер!', rating=0)

# Применение like() и dislike() к объектам
post1.like()
comment1.like()
comment4.dislike()

# Обновление рейтингов
author1.update_rating()
author2.update_rating()

# Вывод username и рейтинга лучшего пользователя
best_user = User.objects.all().order_by('-author__rating').first()
print(best_user.username, best_user.author.rating)

# Вывод информации о лучшей статье
best_post = Post.objects.filter(post_type='article').order_by('-rating').first()
print(best_post.created_at, best_post.author.user.username, best_post.rating, best_post.title, best_post.preview())

# Вывод всех комментариев к лучшей статье
comments_to_best_post = Comment.objects.filter(post=best_post)
for comment in comments_to_best_post:
    print(comment.created_at, comment.user.username, comment.rating, comment.text)