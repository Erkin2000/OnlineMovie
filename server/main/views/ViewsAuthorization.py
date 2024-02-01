from django.contrib.auth.models import User
from rest_framework.views import APIView, Response
from main.serializers.serializersForUser import UserSerializers


class Auth(APIView):
    def Auth(self, request):
        queryset = User.objects.all()
        serializers = UserSerializers(queryset, many=True)
        return Response(serializers.data)