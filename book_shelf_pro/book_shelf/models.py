from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    details = models.TextField()

    def __str__(self):
        return self.name.username


class BookAuthor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HaveToRead(models.Model):
    name = models.CharField(max_length=100)
    pictur = models.ImageField()
    book_author = models.ForeignKey(BookAuthor,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE) 
    target_date = models.DateField()
   
    status_choices = (
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low'),
        ('Done','Done')
    )

    status = models.CharField(max_length=6,choices=status_choices)
    posted_on = models.DateTimeField(auto_now=False,auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True,auto_now_add=False)
    

    def __str__(self):
        return self.name