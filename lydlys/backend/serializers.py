from rest_framework import serializers
from backend.models import Song, Show


# class Song(models.Model):
#     name = models.CharField(max_length=100)
#     artist = models.CharField(max_length=100)
#     source = models.CharField(max_length=100)


# class Show(models.Model):
#     name = models.CharField(max_length=100)
#     time = models.DateTimeField()
#     song = models.ForeignKey(Song, on_delete=models.CASCADE)


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "name", "artist", "source")


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ("id", "name", "time", "song")
