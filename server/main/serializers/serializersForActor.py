from rest_framework import serializers
from main.models import Actor


class SerializerActor(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class SerializersForGetActor(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(default=0)
    description = serializers.CharField()
    image = serializers.ImageField()

    def create(self, validate_data):
        return Actor.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.age = validated_data.get("age", instance.age)
        instance.description = validated_data.get("description", instance.description)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance


