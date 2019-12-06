from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from teacher.models import Teacher
from teacher.serializers import TeacherSerializer


class TeacherView(APIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                instance = self.queryset.get(id=pk)
            except Teacher.DoesNotExist:
                raise Http404
            else:
                serializer = self.serializer_class(instance)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        instances = self.queryset.all()
        serializer = self.serializer_class(instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
