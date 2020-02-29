from .serializers1 import *
from .models import *

from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from  rest_framework.permissions import IsAuthenticated


class StudentGenericView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):

    serializer_class = StudentSerializers  # Initialization of serializer object
    queryset = Student.objects.all()
    lookup_field = 'pk'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request)

    def delete(self, request, pk=None):
        return self.delete(request)
