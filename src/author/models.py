from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    details = models.TextField()

    def __str__(self):
        return self.name.username