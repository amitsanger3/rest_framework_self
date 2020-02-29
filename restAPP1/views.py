from django.shortcuts import render
from .models import *
from .serializers1 import *

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


def index(request):

    context = {
        "students": Student.objects.all(),
    }

    return render(request, 'pages/index.html', context)


@csrf_exempt
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        sr = StudentSerializers(students, many=True)

        return JsonResponse(sr.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        sr = StudentSerializers(data=data)

        if sr.is_valid():
            sr.save()
            return JsonResponse(sr.data, status=201)
        return JsonResponse(sr.errors, status=400)


@csrf_exempt
def edit_student(request, pk):

    try:
        this_student = Student.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        sr = StudentSerializers(this_student)

        return JsonResponse(sr.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        sr = StudentSerializers(this_student, data=data)

        if sr.is_valid():
            sr.save()
            return JsonResponse(sr.data)
        return JsonResponse(sr.errors, status=400)

    elif request.method == 'DELETE':

        this_student.delete()
        return HttpResponse(status=204)