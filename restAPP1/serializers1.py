from rest_framework import serializers
from .models import Student

# Model view


class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ['id', 'first_name', 'last_name', 'gender', 'age', 'email']  # for selective fields
        fields = '__all__'
