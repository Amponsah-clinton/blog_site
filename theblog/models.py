from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    title_tag = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)   # adds ckeditor
    post_date = models.DateTimeField(auto_now_add=True)       # automatically add the date
    category = models.CharField(max_length=223, default= 'coding')
    snippet = models.CharField(max_length=223)
    likes = models.ManyToManyField(User, related_name='blog_posts')         # for many-to-many relations
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    
    def total_likes(self):
        return self.likes.count()
      
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    
# doing the new blog post
    def get_absolute_url(self):
        # return reverse("article-detail", args=(str(self.id))) this directs it to details page  but home directs it to the homepage
         return reverse("home")
    
class Category(models.Model):
    name = models.CharField(max_length=225)  
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    bio = models.TextField()
    
    
    def __str__(self):
        return str(self.user)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments' , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    