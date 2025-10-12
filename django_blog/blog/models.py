from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    
class Meta:
        ordering = ['-published_date'] 
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

def __str__(self):
    return self.title
    

