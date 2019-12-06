from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from news.models import News
from news.serializers import NewsSerializer


class NewsView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, pk=None, *args, **kwargs):
        instances = self.queryset.all()
        serializer = self.serializer_class(instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
