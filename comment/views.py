from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from comment.models import Comment
from comment.serializers import CommentSerializers
from comment import utils


class CommentViews(APIView):
    queryset = Comment.objects.filter(available=True)
    serializer_class = CommentSerializers

    def get(self, request, *args, **kwargs):
        return Response(
            data=self.serializer_class(self.queryset.all(), many=True).data,
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        utils.send_comment_to_admin_email(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
