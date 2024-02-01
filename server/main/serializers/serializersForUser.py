from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    data_joined = serializers.DateField()
