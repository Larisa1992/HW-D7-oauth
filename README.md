# HW-D6-Library
Home Work for module d6 (static and base.html)

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

2) Главная страница проекта расположена по пути "index/" (http://127.0.0.1:8000/index/)

В базовом шаблоне задана шапка сайтас тремя ссылками:
My personal library
My friends
My books

3) для проверки пункта 3 домашнего задания ("Добавьте в модель книги возможность загружать картинки к книгам (в этом задании допускается сделать это через панель администратора)")
перейдите по ссылке "My books" в шапке проекта с любой страницы и нажмите "Редактировать" для любой книги. Перед кнопкой "Сохранить" есть действие "Выберите файл" для загрузки изображения.

4) После сохранения книги выполняется переадресация на список книг (My books)