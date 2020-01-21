from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactView(APIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, pk=None, *args, **kwargs):
        instances = self.queryset.all()
        serializer = self.serializer_class(instances, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
