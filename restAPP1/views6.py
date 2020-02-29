from .serializers1 import *
from .models import *

from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):

    serializer_class = StudentSerializers  # Initialization of serializer object
    queryset = Student.objects.all()
