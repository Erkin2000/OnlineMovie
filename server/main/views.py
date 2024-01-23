from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import AllMovieSerializers

from .models import Movie


@api_view(['GET'])
def get(request):
    queryset = Movie.objects.all().values()
    # serializer = AllMovieSerializers(queryset, many=True)
    return Response(queryset)