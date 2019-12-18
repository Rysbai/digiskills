from django.http import Http404
from django.utils.timezone import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from news.models import News
from news.serializers import NewsSerializer


class NewsListView(APIView):
    queryset = News.objects.filter(pub_date__lte=datetime.now())
    serializer_class = NewsSerializer

    def get(self, request, pk=None, *args, **kwargs):
        lang = request.query_params.get('lang', None)

        instances = self.queryset.all()
        serializer = self.serializer_class(instances, lang=lang, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class NewsDetailView(APIView):
    queryset = News.objects.filter(pub_date__lte=datetime.now())
    serializer_class = NewsSerializer

    def get(self, request, pk=None, *args, **kwargs):
        lang = request.query_params.get('lang', None)
        try:
            instance = self.queryset.get(id=pk)
        except self.queryset.model.DoesNotExist:
            raise Http404
        else:
            instance.views += 1
            instance.save()
            serializer = self.serializer_class(instance, lang=lang)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
