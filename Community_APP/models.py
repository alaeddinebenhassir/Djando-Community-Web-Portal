from django.db import models 
from django.utils import timezone 

class Post(models.Model): 

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    descreption = models.CharField(max_length=200) 
    text = models.TextField() 
    title = models.CharField(max_length=200) 
    published_date = models.DateTimeField(blank=True, null=True)
    comment = models.TextField()
    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self):
        return self.title
        