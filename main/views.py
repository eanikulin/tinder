from .models import User
from rest_framework import permissions
from .serializers import UsersRegisterSerializer
from rest_framework import mixins, viewsets


class UsersRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersRegisterSerializer
