from django.contrib import admin
from django.urls import path, include  
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendList, FriendEdit, friends_books, BookList, book_edit, books_list, book_increment, book_decrement, publishing, index

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls', namespace='common')), # пути приложения с профилями пользователя
    path('accounts/', include('allauth.urls')),
    # path('', books_list), # books_list - метод, который будет исполнятся при запросе URL в первом аргументе
    path('index/', index, name='all_book'),
    path('index/book_increment/', book_increment),
    path('index/book_decrement/', book_decrement),
    path('index/publishing/', publishing),
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'), #books_authors_create_many вызываем метод из файла view.py
    path('friends/', FriendList.as_view(), name='friend_list'), # выводим список друзей и переходим в форму создания друга и форму выдачи книг друзьям
    path('friend/create', FriendEdit.as_view(), name='friend_create'), # формма создания друга
    path('friends/books', friends_books, name='friends_books'), # формма создания друга
    path('books', BookList.as_view(), name='books_list'), # форма просмотра всех книг с уточнением, у кого книга. 
    path('book/edit/<int:book_id>/', book_edit, name='book_edit'), # форма редактирования книги, можно отдать книгу другу
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # для статических медиа файлов
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # для файлов стилей
