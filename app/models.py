from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    class Meta:
        db_table = "artist"

    def __str__(self):
        return f"{self.id} {self.name}"

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, blank=True, null=True, on_delete=models.CASCADE)
    # artist = models.CharField(max_length=20, choices=Artist, default='')
    release_date = models.DateField()
    GENRE_CHOICES = [
        ('blues', 'Blues'),
        ('classical', 'Classical'),
        ('country', 'Country'),
        ('jazz', 'Jazz'),
        ('other', 'Other'),
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('r&B', 'R&B'),
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='other')
    producer_name = models.CharField(max_length=30)
    record_label = models.CharField(max_length=30)
    comment = models.TextField(max_length=600, null=True, blank=True)
    
    class Meta:
        db_table = "album"

    def __str__(self):
        return f"{self.name} {self.artist.name} ({self.release_date.strftime('%d-%B-%Y')})"

