from rest_framework import generics
from rest_framework.response import Response

from main.serializers.serializersForCategory import CategorySerializers
from rest_framework.views import APIView
from main.models import *


class ApiCategory(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        return Response(CategorySerializers(queryset, many=True).data)

    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data, 'message': 'data added successful'})

    def put(self, request, *args, **kwargs):
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

    def delete(self,request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance =Category.objects.all()
        except:
            return Response({"error": "Object does not exist"})
        serializer = CategorySerializers(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.delete()
        return Response({"post": serializer.data}, {'message': "data changed successfully "})
""" Этот класс для GET и POST запроса"""


class ApiCategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ApiCategoryUpdate(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ApiCategoryDestroy(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers










