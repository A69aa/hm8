from django.db import models

class Cartoon(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')
