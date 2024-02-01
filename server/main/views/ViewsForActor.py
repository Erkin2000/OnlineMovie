from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Actor
from main.serializers.serializersForActor import SerializersForGetActor, SerializerActor


def getWithId(request, pk):
    oneData = Actor.objects.get(id=pk)
    context = {
        'name': oneData.name,
        'age': oneData.age,
        'description': oneData.description,
        # 'image': oneData.image
    }
    return JsonResponse(context)


class AllActor(APIView):
    def get(self, request):
        queryset = Actor.objects.all()
        return Response(SerializersForGetActor(queryset, many=True).data)

    def post(self, request):
        serializer = SerializersForGetActor(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data, 'message': 'data added successful'})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Method PUT is not allowed'})

        try:
            instance = Actor.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializers = SerializersForGetActor(data=request.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({'post': serializers.data}, {'message': 'data changed successful'})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Method DELETE is not allowed'})

        try:
            instance = Actor.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializers = SerializersForGetActor(data=request.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.delete()
        return Response({'post': serializers.data}, {'message': 'data deleted successful'})

