from rest_framework import viewsets

from posts.paginations import CustomeLimitOffsetPagination
from .models import (
    Post,
    Answer,
    Comment,
    Tag
)
from .serializers import (
    PostSerializer,
    AnswerSerializer,
    CommentSerializer,
    TagSerializer
)

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomeLimitOffsetPagination

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

