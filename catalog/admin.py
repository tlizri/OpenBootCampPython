from django.contrib import admin
from .models import Director, Genre, Movie, Country


class MovieInline(admin.TabularInline):
    model = Movie
    exclude = ('id',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'date_of_birth', 'date_of_death')
    list_filter = ('date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    exclude = ('id',)
    inlines = [MovieInline]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    list_display = ('id', 'title', 'director', display_genre, 'country')
    list_filter = ('country', 'genre', 'director')
    exclude = ('id',)


# Register your models here.
admin.site.register(Genre)
admin.site.register(Country)
