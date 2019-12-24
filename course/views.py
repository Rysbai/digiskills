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


class CategoryListView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', None)

        serializer = self.serializer_class(self.queryset.all(), lang=lang, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryDetailView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk=None,  *args, **kwargs):
        lang = request.query_params.get('lang', None)
        try:
            instance = self.queryset.get(id=pk)
        except self.queryset.model.DoesNotExist:
            raise Http404
        else:
            serializer = self.serializer_class(instance, lang=lang)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class TeacherListView(APIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, pk=None, *args, **kwargs):
        lang = request.query_params.get('lang', None)
        instances = self.queryset.all()
        serializer = self.serializer_class(instances, lang=lang, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TeacherDetailView(APIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, pk=None, *args, **kwargs):
        lang = request.query_params.get('lang', None)
        try:
            instance = self.queryset.get(id=pk)
        except self.queryset.model.DoesNotExist:
            raise Http404
        else:
            serializer = self.serializer_class(instance, lang=lang)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class CourseListView(APIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        category_id = request.query_params.get('category_id', None)
        teacher_id = request.query_params.get('teacher_id', None)
        lang = request.query_params.get('lang', None)

        instances = self.queryset.all()
        if teacher_id:
            instances = instances.filter(teacher_id=teacher_id)
        if category_id:
            instances = instances.filter(category_id=category_id)
        if lang:
            instances = instances.filter(language=lang)

        serializer = self.serializer_class(instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CourseDetailView(APIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk=None, *args, **kwargs):
        try:
            instance = self.queryset.get(id=pk)
        except self.queryset.model.DoesNotExist:
            raise Http404
        else:
            serializer = self.serializer_class(instance)
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
