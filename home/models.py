from django.db import models

# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='Images', blank=True)


class Glimpses(models.Model):
    name = models.TextField()


class GlimpsesImage(models.Model):
    glimpses = models.ForeignKey(
        Glimpses, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='glimpses', blank=True)
