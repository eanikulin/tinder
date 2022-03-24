from rest_framework.permissions import IsAuthenticated
from .models import User, Likes
from rest_framework import permissions, generics
from .serializers import UsersRegisterSerializer, MatchSerializer
from rest_framework import mixins, viewsets


class UsersRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersRegisterSerializer


class LikesAPIView(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MatchSerializer
