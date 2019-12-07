from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from aboutus.models import AboutUs
from aboutus.serializers import AboutUsSerializer


class AboutUsView(APIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', None)
        instances = self.queryset.all()
        serializer = self.serializer_class(instances, lang=lang, many=True)

        try:
            data = serializer.data[0]
        except IndexError:
            data = []

        return Response(data=data, status=status.HTTP_200_OK)
