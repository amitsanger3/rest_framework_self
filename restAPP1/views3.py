from .serializers1 import *
from .models import *

from rest_framework import generics
from rest_framework import mixins


class StudentGenericView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = StudentSerializers  # Initialization of serializer object
    queryset = Student.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class EditStudentGenericView(generics.GenericAPIView,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin):

    serializer_class = StudentSerializers  # Init
    queryset = Student.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk=None):
        return self.retrieve(request)

    def put(self, request, pk=None):
        return self.update(request)

    def delete(self, request, pk=None):
        return self.delete(request)