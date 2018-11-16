from django.contrib import admin
from .models import  Actor,RATING_CHOICES,Director,Movie, Genre

# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')



class DirectorAdmin(admin.ModelAdmin):
    ist_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', )



admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Director,DirectorAdmin)
admin.site.register(Genre,GenreAdmin)


