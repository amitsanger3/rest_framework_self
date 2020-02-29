from .serializers1 import *
from .models import *

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404


class StudentApiView(APIView):

    def get(self, request):
        students = Student.objects.all()
        sr = StudentSerializers(students, many=True)

        return Response(sr.data)

    def post(self, request):
        sr = StudentSerializers(data=request.data)

        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_201_CREATED)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)


class EditStudentApiView(APIView):

    def get_student(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sr = StudentSerializers(self.get_student(pk))

        return Response(sr.data)

    def put(self, request, pk):
        sr = StudentSerializers(self.get_student(pk), data=request.data)

        if sr.is_valid():
            sr.save()
            return Response(sr.data)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        this_student = self.get_student(pk)
        this_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
