from django.db import models
from django.utils import timezone


class Genre(models.Model):  # "Genre" inherits class Model functionality from models package
    # charfield specifies a character field; with max lenght of 255
    name = models.CharField(max_length=255)

    # this function overrider the str method to display the item name instead of Object x
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    numbers_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # ForeignKey adds a "many to one" relationship between movies and genre.
    # Cascade specifies that, if Foreignkey is deleted, so are all movies related.
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
