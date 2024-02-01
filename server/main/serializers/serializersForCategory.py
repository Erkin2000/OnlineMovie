from rest_framework import serializers

from main.serializers import *


# class CategorySerializers(serializers.ModelSerializer):
#     class Meta:
#
#         model = Category
#         fields = "__all__"
#


class CategorySerializers(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    director = serializers.CharField()
    url = serializers.SlugField(max_length=160)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.director = validated_data.get("director", instance.director)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance



#
