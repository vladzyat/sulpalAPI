from rest_framework.viewsets import ModelViewSet
from .models import Comment, Stars
from .serializers import CommentSerializer, StarsSerializer


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class StarsModelViewSet(ModelViewSet):
    queryset = Stars.objects.all()
    serializer_class = StarsSerializer

