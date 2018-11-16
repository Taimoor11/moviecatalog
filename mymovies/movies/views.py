from django.conf import settings
from django.shortcuts import render
from .models import Genre, Director, Actor, Movie, RATING_CHOICES
from .forms import MovieFilterForm


def movie_list(request):
    qs = Movie.objects.order_by("title")
    form = MovieFilterForm(data=request.GET)
    facets = {
        "selected": {},
        "categories": {
            "genres": Genre.objects.all(),
            "directors": Director.objects.all(),
            "actors": Actor.objects.all(),
            "ratings": RATING_CHOICES,
        }, }
    if form.is_valid():
        filters = (
            ("genre", "genres",),
            ("director", "directors",),
            ("actor", "actors",),
            ("rating", "rating",),
        )
        qs = filter_facets(facets, qs, form, filters)
    if settings.DEBUG:
        # Let's log the facets for review when debugging
        import logging
        logger = logging.getLogger(__name__)
        logger.info(facets)
    context = {
        "form": form,
        "facets": facets,
        "object_list": qs,
    }
    return render(request, "movies/movie_list.html", context)


def filter_facets(facets, qs, form, filters):
    for facet, key in filters:
        value = form.cleaned_data[facet]
        if value:
            selected_value = value
            if facet == "rating":
                rating = int(value)
                selected_value = (rating,
                                  dict(RATING_CHOICES)[rating])
                filter_args = {
                    f"{key}__gte": rating,
                    f"{key}__lt": rating + 1,
                }
            else:
                filter_args = {key: value}
            facets["selected"][facet] = selected_value
            qs = qs.filter(**filter_args).distinct()
    return qs
