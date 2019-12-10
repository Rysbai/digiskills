from django.http import Http404
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from news.models import News
from news.serializers import NewsSerializer


class NewsView(APIView):
    queryset = News.objects.filter(pub_date__gt=datetime.datetime.now())
    serializer_class = NewsSerializer

    def get(self, request, pk=None, *args, **kwargs):
        lang = request.query_params.get('lang', None)
        if pk:
            try:
                instance = self.queryset.get(id=pk)
            except self.queryset.model.DoesNotExist:
                raise Http404
            else:
                instance.views += 1
                instance.save()
                serializer = self.serializer_class(instance, lang=lang)
                return Response(data=serializer.data, status=status.HTTP_200_OK)

        instances = self.queryset.all()
        serializer = self.serializer_class(instances, lang=lang, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
