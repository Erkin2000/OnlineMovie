from django.contrib import admin
from .models import *


@admin.register(Category, Actor, Genre, Movie, Movie_shots,
                RatingStar, Rating, Reviews)
class MovieAdmin(admin.ModelAdmin):
    pass




