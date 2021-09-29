from rest_framework import viewsets, exceptions
from .permissions import AuthorOrReadOnly
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from posts.models import Post, Follow, Group
from .serializers import PostSerializer, CommentSerializer
from .serializers import FollowSerializer, GroupSerializer
from rest_framework import filters


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post_id = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        # И отбираем только нужные комментарии
        # new_queryset = Comment.objects.filter(post=post_id)
        new_queryset = post_id.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied('Изменение чужого контента '
                                              'запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(CommentViewSet, self).perform_destroy(instance)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)
    #
    # def get_queryset(self):
    #     return Follow.objects.filter(user=self.request.user)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        new_queryset = user.follower.all()
        return new_queryset

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        # following = get_object_or_404(User, username=serializer.instance)
        # if Follow.objects.filter(user=self.request.user).filter(
        #         following=serializer.instance).count != 0:
        #     return Response(
        #         data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user)
        super(FollowViewSet, self).perform_create(serializer)
