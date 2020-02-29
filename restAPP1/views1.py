from django.shortcuts import render
from .models import *
from .serializers1 import *

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        sr = StudentSerializers(students, many=True)

        return Response(sr.data)

    elif request.method == 'POST':
        sr = StudentSerializers(data=request.data)

        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_201_CREATED)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def edit_student(request, pk):

    try:
        this_student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sr = StudentSerializers(this_student)

        return Response(sr.data)

    elif request.method == 'PUT':
        sr = StudentSerializers(this_student, data=request.data)

        if sr.is_valid():
            sr.save()
            return Response(sr.data)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        this_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)