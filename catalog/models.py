from django.db import models
from django.urls import reverse
import uuid


class Director(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular director')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    objects = models.Manager()

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular director instance."""
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Genre(models.Model):
    """Model representing a movie genre."""
    name = models.CharField(primary_key=True, max_length=200, help_text='Enter a movie genre (e.g. Science Fiction)')
    objects = models.Manager()

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        ordering = ['name']


class Country(models.Model):
    """Model representing a movie country"""
    name = models.CharField(primary_key=True, max_length=200, help_text='Enter a movie country (e.g. Spain)')
    objects = models.Manager()

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    class Meta:
        ordering = ['name']


class Movie(models.Model):
    """Model representing a movie"""
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular movie')
    title = models.CharField(max_length=200)

    # Foreign Key used because movie can only have one author, but authors can have multiple books
    # Director is a string rather than an object because it hasn't been declared yet in the file
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the movie')

    # ManyToManyField used because genre can contain many movies. Movies can cover many genres.
    # Genre class has already been defined, so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this movie')

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,
                                help_text='Select a country for this movie')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this movie."""
        return reverse('movie-detail', args=[str(self.id)])

    class Meta:
        ordering = ['title']
