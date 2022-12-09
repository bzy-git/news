from django.db import models

class News(models.Model):
    image=models.ImageField(upload_to ='blog')
    heading=models.CharField(max_length=255)
    reporter=models.CharField(max_length=25)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.heading
