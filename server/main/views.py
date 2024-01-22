from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import AllMovieSerializers



@api_view(['POST'])
@parser_classes([JSONParser])
def example_view(request, format=None):
    AllObjects = Movie.objects.all()
    serializers = AllMovieSerializers(AllObjects, many=True)
    return Response({'received data': serializers.data})
