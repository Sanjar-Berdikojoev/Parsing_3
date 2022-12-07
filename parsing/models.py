from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    title_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    published_data = models.CharField(max_length=100)

    def __str__(self):
        return self.title