from django.shortcuts import render
from .models import Movie, Director
from django.views import generic


def index(request):
    """View function for home page of site."""

    # Generate counts of some main objects
    num_movies = Movie.objects.all().count()
    num_directors = Director.objects.count()
    num_action = Movie.objects.filter(genre__exact='Acción').count()
    num_animation = Movie.objects.filter(genre__exact='Animación').count()
    num_romance = Movie.objects.filter(genre__exact='Romance').count()
    num_fantasy = Movie.objects.filter(genre__exact='Fantasía').count()
    num_terror = Movie.objects.filter(genre__exact='Terror').count()
    num_scifi = Movie.objects.filter(genre__exact='Ciencia Ficción').count()
    num_adventure = Movie.objects.filter(genre__exact='Aventura').count()
    num_mistery = Movie.objects.filter(genre__exact='Misterio').count()
    num_thriller = Movie.objects.filter(genre__exact='Suspense').count()
    num_drama = Movie.objects.filter(genre__exact='Drama').count()
    context = {
        'num_movies': num_movies,
        'num_directors': num_directors,
        'num_action': num_action,
        'num_animation': num_animation,
        'num_romance': num_romance,
        'num_fantasy': num_fantasy,
        'num_terror': num_terror,
        'num_scifi': num_scifi,
        'num_adventure': num_adventure,
        'num_mistery': num_mistery,
        'num_thriller': num_thriller,
        'num_drama': num_drama,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 2

    def get_queryset(self):
        return Movie.objects.all().order_by('title')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(MovieListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class MovieDetailView(generic.DetailView):
    model = Movie


class DirectorListView(generic.ListView):
    model = Director
    paginate_by = 2

    def get_queryset(self):
        return Director.objects.all().order_by('last_name', 'first_name')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(DirectorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class DirectorDetailView(generic.DetailView):
    model = Director
