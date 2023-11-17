from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

TYPE = (
    (0,"Web Novel"),
    (1,"Light Novel")
)

           
class Series(models.Model):
    title = models.CharField(max_length=200, unique=True, default='Series Title')
    series_slug = models.SlugField(max_length=200, unique=True, default='series-title')
    created_on = models.DateTimeField(auto_now_add=True)
    web_novel = models.IntegerField(choices=TYPE, default=1)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.title
    

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True, default='Book Title')
    book_slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    post_slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.book_id.title + " " + self.title




     