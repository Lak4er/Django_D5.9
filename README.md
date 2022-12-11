# Django_D5.9
D5.9. Итоговое задание. Проект News Portal
Django_D5.9/NewsPaper/NewsPortal/models.py

Список всех команд, запускаемых в Django Shell
from NewsPortal.models import *

Создать пользователей (с помощью метода User.objects.create_user).
user1 = User.objects.create_user(username="Petr Petrovich")
user2 = User.objects.create_user(username="Maxim Karimov")
user3 = User.objects.create_user(username="Edik Dofozen")

Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(author_user=User.objects.get(id=1))
Author.objects.create(author_user=User.objects.get(id=2))

Добавить категории в модель Category.
categoty1 = Category.objects.create(name_category="Business")
categoty2 = Category.objects.create(name_category="Auto")
categoty3 = Category.objects.create(name_category="IT")
categoty4 = Category.objects.create(name_category="Games")
categoty5 = Category.objects.create(name_category="Sport")

Добавить 2 статьи и 1 новость.
post1 = Post.objects.create(post_author=Author.objects.get(id=1), event="news", title="Русский голос Ви в Cyberpunk 2077 намекнул на возвращение в дополнении Phantom Liberty", post_text="Актер Егор Васильев, исполнивший роль персонажа Ви в Cyberpunk 2077, намекнул на возвращение к работе над русским дубляжом игры. О судьбе локализации после анонса дополнения Phantom Liberty он рассказал на стриме блогера Владимира Братишкина.")
post2 = Post.objects.create(post_author=Author.objects.get(id=2), event="papers", title="Лионель Месси: Аргентине в матче с Нидерландами «пришлось пострадать»",post_text="Форвард и капитан сборной Аргентины Лионель Месси после победы над Нидерландами в 1/4 финала чемпионата мира в Катаре заявил, что его команде «пришлось пострадать». Слова футболиста приводит Marca.")                                      
post3 = Post.objects.create(post_author=Author.objects.get(id=1), event="papers", title="Дешевле «Ларгуса»: обзор фургона Lada Granta Kub",post_text= "Фургон Lada Granta Kub построен по проверенной схеме. К передней части от «Гранты» присоединяется надстройка, представляющая собой силовой металлический каркас, обшитый цельноформованными панелями из композитных материалов с внешней стороны и АБС-пластиком с внутренней. Задняя стенка кабины при этом служит передней стенкой кузова, превращая автомобиль в единое целое и увеличивая его жесткость. Распашные двери предусмотрены с обоих бортов. Это не только упрощает процесс разгрузки при адресной доставке товаров, но и позволяет использовать такой кузов как универсальный. Например, при создании пассажирских версий с числом пассажирских мест до 8.")
                                      

Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
Post.objects.get(id=1).categories.add(Category.objects.get(id=1))
Post.objects.get(id=1).categories.add(Category.objects.get(id=3))
Post.objects.get(id=1).categories.add(Category.objects.get(id=4))
Post.objects.get(id=2).categories.add(Category.objects.get(id=1))
Post.objects.get(id=2).categories.add(Category.objects.get(id=5))
Post.objects.get(id=3).categories.add(Category.objects.get(id=1))
Post.objects.get(id=3).categories.add(Category.objects.get(id=2))

Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=Author.objects.get(id=2).author_user,comment_text="Хорошая работа")
Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=Author.objects.get(id=1).author_user,comment_text="Если волк молчит то лучше его не перебивай.")
Comment.objects.create(comment_post=Post.objects.get(id=2),comment_user=Author.objects.get(id=1).author_user,comment_text="Иногда жизнь — это жизнь, а ты в ней иногда.")
Comment.objects.create(comment_post=Post.objects.get(id=3),comment_user=Author.objects.get(id=2).author_user,comment_text="Лучше один раз упасть, чем сто раз упасть.")

Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(id=1).like_post()
Post.objects.get(id=1).like_post()
Post.objects.get(id=1).like_post()
Post.objects.get(id=1).like_post()
Post.objects.get(id=1).like_post()
Post.objects.get(id=2).dislike_post()
Post.objects.get(id=2).dislike_post()
Post.objects.get(id=2).dislike_post()
Post.objects.get(id=3).dislike_post()
Post.objects.get(id=3).dislike_post()
Post.objects.get(id=1).post_rating
Post.objects.get(id=2).post_rating
Post.objects.get(id=3).post_rating
Comment.objects.get(id=1).like_comment()
Comment.objects.get(id=2).like_comment()
Comment.objects.get(id=1).like_comment()
Comment.objects.get(id=3).like_comment()
Comment.objects.get(id=4).like_comment()
Comment.objects.get(id=1).like_comment()
Comment.objects.get(id=4).like_comment()
Comment.objects.get(id=3).like_comment()
Comment.objects.get(id=4).like_comment()
Comment.objects.get(id=1).like_comment()
Comment.objects.get(id=1).dislike_comment()
Comment.objects.get(id=2).dislike_comment()
Comment.objects.get(id=3).dislike_comment()
Comment.objects.get(id=1).comment_rating
Comment.objects.get(id=2).comment_rating
Comment.objects.get(id=3).comment_rating
Comment.objects.get(id=4).comment_rating

Обновить рейтинги пользователей.
Author.objects.get(id=1).update_rating()
Author.objects.get(id=2).update_rating()


посмотрели рейтинг автора
Author.objects.get(id=1).author_rating
Author.objects.get(id=2).author_rating

Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.all().order_by('-author_rating').values('author_user__username', 'author_rating')[0]

Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
q=1
list10 = [Author.objects.get(id=q).author_user.date_joined,
          Author.objects.get(id=q).author_user.username,
          Author.objects.get(id=q).author_rating,
          Post.objects.filter(post_author = Author.objects.get(id=q)).order_by('-post_rating').first().title
          ]
list10

Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Post.objects.all().order_by('-post_rating')[0].comment_set.values('time_in_comment', 'comment_user', 'comment_rating', 'comment_text')


