from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify


# Create your models here.
STATUS = (
    (0,"Active"),
    (1,"Not Active")
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
    image = models.ImageField(upload_to='images/', default='images/daughter-s-rank_5KBBAcB.png')

    def __str__(self):
        return self.title
    

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True, default='Book Title')
    book_slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/daughter-s-rank_5KBBAcB.png')
    active = models.BooleanField(default=True)
    
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



class WebNovel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    novel_slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    image = models.ImageField(upload_to='images/')


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.novel_slug:
            self.novel_slug = slugify(self.title)
        super().save(*args, **kwargs)
    

class Chapter(models.Model):
    chapter_number = models.IntegerField()
    title = models.CharField(max_length=200, unique=True)
    chapter_slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    web_novel = models.ForeignKey(WebNovel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.web_novel.title + " " + self.title
    
    def save(self, *args, **kwargs):
        if not self.chapter_slug:
            self.chapter_slug = slugify(self.title)
        super().save(*args, **kwargs)