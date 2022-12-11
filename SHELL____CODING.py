python manage.py makemigrations
python manage.py migrate


from NewsPortal.models import *

1
user1 = User.objects.create_user(username="Aleksey Serov")
user2 = User.objects.create_user(username="Maxim Kashin")
user3 = User.objects.create_user(username="Edik Yablokov")

2
Author.objects.create(author_user=User.objects.get(id=1))
Author.objects.create(author_user=User.objects.get(id=2))

3
categoty1 = Category.objects.create(name_category="Business")
categoty2 = Category.objects.create(name_category="Auto")
categoty3 = Category.objects.create(name_category="IT")
categoty4 = Category.objects.create(name_category="Games")
categoty5 = Category.objects.create(name_category="Sport")

4
post1 = Post.objects.create(post_author=Author.objects.get(id=1), event="news", title="Русский голос Ви в Cyberpunk 2077 намекнул на возвращение в дополнении Phantom Liberty",
                            post_text="Актер Егор Васильев, исполнивший роль персонажа Ви в Cyberpunk 2077, намекнул на возвращение к работе над русским дубляжом игры. О судьбе локализации после анонса дополнения Phantom Liberty он рассказал на стриме блогера Владимира Братишкина."
                                      "Ожидайте официальных заявлений. Все-таки ничего не отменяли, но правда ничего пока и не возвращали. Ладно, скажем так, увидимся в Найт-Сити, - отметил он.Дебютный трейлер Phantom Liberty был представлен на церемонии The Game Awards. Дополнение выйдет только на ПК, PlayStation 5 и Xbox Series, пропустив консоли прошлого поколения."
                                      "В мае этого года актриса Юлия Горохова, исполнившая женскую версию Ви в русской локализации Cyberpunk 2077, заявляла, что не будет принимать участия в озвучке нового дополнения для игры CD Projekt RED."
                                      "Польская студия CD Projekt официально сообщала, что русская локализация их будущих проектов под вопросом. Однако пока разработчики официально не подтвердили, что отказались от русской локализации дополнения для Cyberpunk 2077.")
post2 = Post.objects.create(post_author=Author.objects.get(id=2), event="papers", title="Лионель Месси: Аргентине в матче с Нидерландами «пришлось пострадать»",
                            post_text="Форвард и капитан сборной Аргентины Лионель Месси после победы над Нидерландами в 1/4 финала чемпионата мира в Катаре заявил, что его команде «пришлось пострадать». Слова футболиста приводит Marca."
                                      "Нападающий назвал счастьем победу Аргентины в серии послематчевых пенальти. Месси также считает, что встреча должна была завершиться в основное время."
                                      "«Нам пришлось пострадать. Но мы идем дальше, и это огромная радость», — сказал игрок."
                                      "Основное время матча между Аргентиной и Нидерландами завершилось со счетом 2:2. При этом аргентинцы вели походу встречи 2:0. В серии пенальти голландцы все-таки потерпели поражение, 4:3."
                                      "В полуфинале Аргентина встретится с хорватами. Матч пройдет 13 декабря. Начало в 22:00 мск."
                                      "Ранее Общественная Служба Новостей сообщала, что главный тренер национальной команды Бразилии Тите заявил, что уходит с поста после вылета южноамериканцев с мундиаля в Катаре.")
post3 = Post.objects.create(post_author=Author.objects.get(id=1), event="papers", title="Дешевле «Ларгуса»: обзор фургона Lada Granta Kub",
                            post_text= "Фургон Lada Granta Kub построен по проверенной схеме. К передней части от «Гранты» присоединяется надстройка, представляющая собой силовой металлический каркас, обшитый цельноформованными панелями из композитных материалов с внешней стороны и АБС-пластиком с внутренней. Задняя стенка кабины при этом служит передней стенкой кузова, превращая автомобиль в единое целое и увеличивая его жесткость. Распашные двери предусмотрены с обоих бортов. Это не только упрощает процесс разгрузки при адресной доставке товаров, но и позволяет использовать такой кузов как универсальный. Например, при создании пассажирских версий с числом пассажирских мест до 8."
                                        "Распашные двери по бокам и «ворота» сзади — хороший доступ."
                                       "Полезный объем грузового отсека составляет 4,9 м3. Внутренняя высота — 1385 мм, длина — 2450 мм. При этом ширина между арками 1050 мм, т. е. внутрь можно продольно поставить два стандартных европоддона. Чтобы добиться таких показателей, колесная база фургона увеличена до 3050 мм."
                                       "Передняя часть салона осталась без изменений. Обратите внимание на руль от Lada Priora: он ставился на упрощенные Lada Granta без подушек безопасности."
                                       "Доработанная задняя подвеска представляет собой сочетание трехлистовых рессор и пневмобаллонов. Давление воздуха в «подушках» можно менять прямо из кабины, увеличивая жесткость при полной загрузке или уменьшая погрузочную высоту до 600 мм. Итоговая грузоподъемность «каблучка» достигает 700 кг."
                                       "Сзади у фургона рессоры и пневмоподушки, а вот амортизаторов нет."
                                       "Пару слов стоит сказать про двигатель. Слабым местом Granta относительно популярной Largus считался менее мощный 90‑сильный мотор. Специально для тех, кому нужно больше, «Промтех» готов предложить тюнинг — вариант ВАЗ-11182 на 116 л. с. Запаса надежности там хватит, а прыти заметно прибавляется. По реальным ощущениям, полученным при сравнительных заездах между 106‑сильной Lada Largus и 116‑сильной Lada Granta, последняя вчистую выигрывает по динамике разгона, которая на порожней машине даже кажется избыточной для коммерческого фургона."
                                       "Lada Granta Kub. Полная масса: 2160 кг. Начало продаж: 2022 г. Цена: 1,64 млн руб."
                                       "Базовая версия фургона Lada Granta Kub будет стоить от 1,64 млн рублей. Это на 300 тыс. меньше, чем Kub на базе Lada Largus. С учетом того, что продажи последнего даже в этом непростом году исчисляются сотнями, а по вместимости он немного проигрывает новому «каблучку», перспективы нового фургона кажутся весьма радужными.")

5
Post.objects.get(id=1).categories.add(Category.objects.get(id=1))
Post.objects.get(id=1).categories.add(Category.objects.get(id=3))
Post.objects.get(id=1).categories.add(Category.objects.get(id=4))

Post.objects.get(id=2).categories.add(Category.objects.get(id=1))
Post.objects.get(id=2).categories.add(Category.objects.get(id=5))

Post.objects.get(id=3).categories.add(Category.objects.get(id=1))
Post.objects.get(id=3).categories.add(Category.objects.get(id=2))

6
Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=Author.objects.get(id=2).author_user,comment_text="Хорошая работа")
Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=Author.objects.get(id=1).author_user,comment_text="Если волк молчит то лучше его не перебивай.")
Comment.objects.create(comment_post=Post.objects.get(id=2),comment_user=Author.objects.get(id=1).author_user,comment_text="Иногда жизнь — это жизнь, а ты в ней иногда.")
Comment.objects.create(comment_post=Post.objects.get(id=3),comment_user=Author.objects.get(id=2).author_user,comment_text="Лучше один раз упасть, чем сто раз упасть.")

7
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



8
Author.objects.get(id=1).update_rating()
Author.objects.get(id=1).author_rating

Author.objects.get(id=2).update_rating()
Author.objects.get(id=2).author_rating


9
Author.objects.all().order_by('-author_rating').values('author_user__username', 'author_rating')[0]

10
q=1
list10 = [Author.objects.get(id=q).author_user.date_joined,
          Author.objects.get(id=q).author_user.username,
          Author.objects.get(id=q).author_rating,
          Post.objects.filter(post_author = Author.objects.get(id=q)).order_by('-post_rating').first().title
          ]



11
Post.objects.all().order_by('-post_rating')[0].comment_set.values('time_in_comment', 'comment_user', 'comment_rating', 'comment_text')






