from django.db import models

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

class NeedToRead(models.Model):
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
   
    # done = models.BooleanField()

    def __str__(self):
        return self.name