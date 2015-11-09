from django.db import models
#from django.contrib.auth.models import User

class Author(models.Model):
    user = models.CharField(max_length=30)
    #AuthorID = models.CharField(max_length = 50)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length = 50)
    Country = models.CharField(max_length=50)
    
class Book(models.Model):
    user = models.CharField(max_length=30)
    ISBN = models.CharField(max_length = 50)
    Title = models.CharField(max_length=30)
    Author = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 50)
    PublishDate = models.CharField(max_length = 50)
    Price = models.CharField(max_length = 50)



