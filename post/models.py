from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/post/',blank=True)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
