from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='media')
    title = models.CharField(max_length=30)
    description = models.TextField()
    ongoing = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

