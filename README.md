# HW-D7-oauth
Home Work for module D7 (work with SocialAccount)

Разворачиваем проект:
1) скачайте репозиторий в вирутальное окружение

2) установите пакеты, используемые в проекте командой
pip install -r requirements.txt

3) запустите проект командой
python manage.py runserver

Описание функционала
1) для входа под администратором используйте данные
Логин: admin
Пароль: django
(если будут ошибки, попробуйте создать своего суперпользователя - как это сделать, описано в курсе)

Войдя под администратором, можно создавать все объекты проекта - авторов, книги, издательства и друзей
и редактировать профили пользователей - добавлен возраст.

2) Страртовая страница проекта http://127.0.0.1:8000/
Отображаются ссылки на вход\выход, профиль GitHub, страницу регистрации.
Отображение ссылок настроено на наличие авторизации пользователя.

3) После регистрации пользователя происходит переадресация на форму создания профиля пользователя, где можно указать возраст

