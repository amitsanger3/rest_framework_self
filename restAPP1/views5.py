from .serializers1 import *
from .models import *

from rest_framework import mixins
from rest_framework import viewsets


class StudentViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):

    serializer_class = StudentSerializers  # Initialization of serializer object
    queryset = Student.objects.all()

