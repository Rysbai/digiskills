from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


from course.models import Category,\
    Teacher,\
    Course,\
    ProgramItem
from course.serializers import CategorySerializer,\
    TeacherSerializer,\
    CourseSerializer,\
    ProgramItemSerializer


class CategoryView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk=None,  *args, **kwargs):
        lang = request.query_params.get('lang', None)
        if pk:
            try:
                instance = self.queryset.get(id=pk)
            except Course.DoesNotExist:
                raise Http404
            else:
                serializer = self.serializer_class(instance, lang=lang)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        serializer = self.serializer_class(self.queryset.all(), lang=lang, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TeacherView(APIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, pk=None, *args, **kwargs):
        lang = request.query_params.get('lang', None)
        if pk:
            try:
                instance = self.queryset.get(id=pk)
            except Teacher.DoesNotExist:
                raise Http404
            else:
                serializer = self.serializer_class(instance, lang=lang)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        instances = self.queryset.all()
        serializer = self.serializer_class(instances,lang=lang, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CourseView(APIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk=None, *args, **kwargs):
        lang = request.query_params.get('lang', None)
        if pk:
            try:
                instance = self.queryset.get(id=pk)
            except Course.DoesNotExist:
                raise Http404
            else:
                serializer = self.serializer_class(instance, lang=lang)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        teacher_id = request.query_params.get('teacher_id', None)
        if teacher_id:
            instances = self.queryset.filter(teacher_id=teacher_id)
        else:
            instances = self.queryset.filter()

        serializer = self.serializer_class(instances, lang=lang, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProgramItemView(APIView):
    queryset = ProgramItem.objects.all()
    serializer_class = ProgramItemSerializer

    def get(self, request, *args, **kwargs):
        course_id = request.query_params.get('course_id', None)
        if course_id:
            instances = self.queryset.filter(course_id=course_id)
        else:
            instances = self.queryset.all()

        serializer = self.serializer_class(instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
