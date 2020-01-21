from factory import DjangoModelFactory

from comment.models import Comment


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    name = 'Example name'
    phone = 'Example phone'
    text = 'Example text'
    available = True

    @staticmethod
    def create_many(count=3):
        comments = []
        for i in range(count):
            comments.append(CommentFactory())
        return comments
