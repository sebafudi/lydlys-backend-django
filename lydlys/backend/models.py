from django.db import models

# Create your models here.


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=100)
    song_artist = models.CharField(max_length=100)
    source = models.CharField(max_length=100)


class Show(models.Model):
    show_id = models.AutoField(primary_key=True)
    show_name = models.CharField(max_length=100)
    show_time = models.DateTimeField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
