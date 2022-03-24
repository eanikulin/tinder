from rest_framework.permissions import IsAuthenticated
from .models import User, Likes
from rest_framework import permissions, generics
from .serializers import UsersRegisterSerializer, MatchSerializer, UsersListSerializer
from rest_framework import mixins, viewsets


class UsersRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersRegisterSerializer


class UsersListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UsersListSerializer
    filterset_fields = ['first_name', 'last_name', 'gender']


class LikesAPIView(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MatchSerializer
