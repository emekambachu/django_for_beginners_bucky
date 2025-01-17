from django.db import models
from django.urls import reverse


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=100, null=False)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(null=True, blank=True)

    # for redirecting to detail page with primary key
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    # string representation
    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    # string representation
    def __str__(self):
        return self.song_title + ' - ' + self.album.artist
