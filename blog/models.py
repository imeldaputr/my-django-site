from django.db import models
from datetime import date
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.


# M:N with Post (many posts can have many tags, and many tags can be associated with many posts)
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return self.caption



# 1:N with Post
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()



# M:N with Tag
# 1:N with Author (1 author can write many posts)
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)  # Automatically set the date when the post is created or updated
    slug = models.SlugField(unique=True, db_index=True)  # Unique identifier for the post, used in URLs
    content = models.TextField(validators=[MinLengthValidator(10)])  # Content of the post with a minimum length of 10 characters
    
    tags = models.ManyToManyField(Tag)  # Many-to-many relationship with Tag
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts') 
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])
    
    
    def __str__(self):
        return self.title
    
