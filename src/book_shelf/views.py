from django.shortcuts import render
from .models import BookAuthor, Category,Publisher,NeedToRead


def index(request):
    book_auth = BookAuthor.objects.all()
    book_category = Category.objects.all()
    book_publisher = Publisher.objects.all()
    need_read = NeedToRead.objects.all()
    

    context = {
        "book_auth":book_auth,
        "book_category":book_category,
        "book_publisher":book_publisher,
        "need_read":need_read

    }
    return render(request, 'index.html',context);
    

def author_book(request,book_auth):
    auth_books = NeedToRead.objects.filter(book_author__name = book_auth)
    context = {
        "auth_books":auth_books,
        "book_autor_name":book_auth
    }
    return render(request,'book_shelf/author_book.html',context)



def publication_book(request,book_pub):
    pub_books = NeedToRead.objects.filter(publisher__name = book_pub)
    context = {
        "pubs_books" : pub_books,
        "pub_name" : book_pub
    }
    return render(request,'book_shelf/pub_book.html',context)




def category_book(request,book_cate):
    cate_books = NeedToRead.objects.filter(category__name = book_cate)
    context = {
        "cate_books":cate_books,
        'cate_name':book_cate
    }
    return render(request,'book_shelf/cate_book.html',context)

def book_details(request,id):
    books = NeedToRead.objects.get(id=id)
    context = {
        "book" : books
    }
    return render(request,'book_shelf/single.html',context)



def profile(request):
    return render(request, 'profile.html');

def single_book(request):
    return render(request,'single.html');

