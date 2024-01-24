from django.forms import model_to_dict
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import CategorySerializers
from rest_framework.views import APIView
from .models import *


class ApiCategory(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        return Response(CategorySerializers(queryset, many=True).data)

    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data, 'message': 'data added successful'})

    def put (self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Category.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = CategorySerializers(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data}, {'message': "data changed successfully "})














# @api_view(['GET'])
# def get(request):
#     queryset = Movie.objects.all().values()
#     # serializer = AllMovieSerializers(queryset, many=True)
#     return Response(queryset)
#
#
# @api_view(['POST'])
# def post(request):
#     post_new = Movie.objects.create(

    # )