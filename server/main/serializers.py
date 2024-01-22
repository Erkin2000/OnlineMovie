from rest_framework import serializers

from .models import Movie

class AllMovieSerializers(serializers.Serializer):

    class Meta:
        model = Movie
        fields = '__all__'