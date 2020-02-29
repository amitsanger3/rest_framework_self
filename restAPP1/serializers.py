from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    gender = serializers.CharField(max_length=2)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    registration_date = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Student.objects.create(validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.registration_date = validated_data.get('registration_date', instance.registration_date)
        instance.save()
        return instance
