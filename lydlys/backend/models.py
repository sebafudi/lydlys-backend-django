from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    source = models.CharField(max_length=100)


class Show(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
