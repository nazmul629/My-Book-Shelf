from django.urls import path
from .views import index,profile,single_book,author_book,publication_book,category_book,book_details

urlpatterns = [
    path('',index,name='index'),
    path('book/author/<book_auth>',author_book,name="author_book"),
    path('book/pub/<book_pub>',publication_book,name="publisar_book"),
    path('book/category/<book_cate>',category_book,name="category_book"),
    path('book/details/<int:id>',book_details,name= "book_details"),

    path('profile',profile),
    path('single_book',single_book)


]

