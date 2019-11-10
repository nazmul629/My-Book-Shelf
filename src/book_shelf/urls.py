from django.urls import path
from .views import index,profile,single_book

urlpatterns = [
    path('',index),
    path('profile',profile),
    path('single_book',single_book)
]

