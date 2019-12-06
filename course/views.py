from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


from course.models import Category,\
    Course,\
    ScheduleItem,\
    ProgramItem,\
    Material,\
    VideoLesson
from course.serializers import CategorySerializer,\
    CourseSerializer,\
    ScheduleItemSerializer,\
    ProgramItemSerializer,\
    MaterialSerializer,\
    VideoLessonSerializer


class CategoryListView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk=None,  *args, **kwargs):
        if pk:
            try:
                instance = self.queryset.get(id=pk)
            except Course.DoesNotExist:
                raise Http404
            else:
                serializer = self.serializer_class(instance)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CourseView(APIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                instance = self.queryset.get(id=pk)
            except Course.DoesNotExist:
                raise Http404
            else:
                serializer = self.serializer_class(instance)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        teacher_id = request.query_params.get('teacher_id', None)
        if teacher_id:
            instances = self.queryset.filter(teacher_id=teacher_id)
        else:
            instances = self.queryset.filter()

        serializer = self.serializer_class(instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ScheduleView(APIView):
    queryset = ScheduleItem.objects.all()
    serializer_class = ScheduleItemSerializer

    def get(self, request, *args, **kwargs):
        course_id = request.query_params.get('course_id', None)
        if course_id:
            instances = self.queryset.filter(course_id=course_id)
        else:
            instances = self.queryset.all()

        serializer = self.serializer_class(instances, many=True)
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


class MaterialView(APIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get(self, request, *args, **kwargs):
        course_id = request.query_params.get('course_id', None)
        if course_id:
            instances = self.queryset.filter(course_id=course_id)
        else:
            instances = self.queryset.all()

        serializer = self.serializer_class(instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class VideoLessonView(APIView):
    queryset = VideoLesson.objects.all()
    serializer_class = VideoLessonSerializer

    def get(self, request, *args, **kwargs):
        course_id = request.query_params.get('course_id', None)
        if course_id:
            instances = self.queryset.filter(course_id=course_id)
        else:
            instances = self.queryset.all()

        serializer = self.serializer_class(instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
