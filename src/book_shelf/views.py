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
    



def profile(request):
    return render(request, 'profile.html');

def single_book(request):
    return render(request,'single.html');